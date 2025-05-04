import pytest
from apps.enquiries.serializers import EnquirySerializer
from tests.factories import EnquiryFactory

@pytest.mark.django_db
def test_enquiry_serializer_valid_data():
    enquiry_instance = EnquiryFactory.build()

    valid_data = {
        "name": enquiry_instance.name,
        # Replace with a valid E.164 formatted phone number
        "phone_number": "+8801767272578",
        "email": enquiry_instance.email,
        "subject": enquiry_instance.subject,
        "message": enquiry_instance.message,
    }
    
    serializer = EnquirySerializer(data=valid_data)
    assert serializer.is_valid(), f"Validation errors: {serializer.errors}"
    saved_enquiry = serializer.save()
    
    assert saved_enquiry.name == valid_data["name"]
    assert saved_enquiry.phone_number == valid_data["phone_number"]
    assert saved_enquiry.email == valid_data["email"]
    assert saved_enquiry.subject == valid_data["subject"]
    assert saved_enquiry.message == valid_data["message"]

@pytest.mark.django_db
def test_enquiry_serializer_invalid_data():
    """
    Test that the EnquirySerializer returns errors when required fields are missing.
    Here, we omit the 'email' field.
    """
    # Create a dictionary missing the required 'email' field
    invalid_data = {
        "name": "Jane Doe",
        "phone_number": "8801767272578",
        # 'email' is intentionally omitted for this negative test
        "subject": "Test Subject",
        "message": "Test message content."
    }
    
    serializer = EnquirySerializer(data=invalid_data)
    # The serializer should not be valid since 'email' is required.
    assert not serializer.is_valid()
    assert "email" in serializer.errors, "Expected an error for missing email field"
