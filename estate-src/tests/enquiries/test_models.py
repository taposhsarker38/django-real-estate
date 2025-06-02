import pytest

def test_enquires_str(enquiry):
    """Test the Enquiry model string representation."""
    # Assert that the __str__ method returns the email.
    assert enquiry.__str__() == enquiry.email
