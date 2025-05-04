# tests/test_views.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from apps.enquiries.models import Enquiry

@pytest.mark.django_db
def test_send_enquiry_email_success(monkeypatch):
    def fake_send_mail(subject, message, from_email, recipient_list, fail_silently):
        return 1
    monkeypatch.setattr("apps.enquiries.views.send_mail", fake_send_mail)

    client = APIClient()
    url = reverse("send-enquiry")
    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "subject": "Test Subject",
        "message": "This is a test message.",
    }
    response = client.post(url, payload, format="json")
    assert response.status_code == 200
    assert response.data.get("success") == "Email sent successfully"
    enquiry = Enquiry.objects.get(email="test@example.com")
    assert enquiry.name == payload["name"]
    assert enquiry.subject == payload["subject"]
    assert enquiry.message == payload["message"]

@pytest.mark.django_db
def test_send_enquiry_email_failure(monkeypatch):
    def fake_send_mail_error(subject, message, from_email, recipient_list, fail_silently):
        raise Exception("Simulated email error")
    
    monkeypatch.setattr("apps.enquiries.views.send_mail", fake_send_mail_error)

    client = APIClient()
    url = reverse("send-enquiry")
    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "subject": "Test Subject",
        "message": "This is a test message.",
    }
    response = client.post(url, payload, format="json")
    assert response.status_code == 200
    assert response.data.get("fail") == "Email sending failed"

