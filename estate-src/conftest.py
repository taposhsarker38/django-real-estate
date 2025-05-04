import pytest
from pytest_factoryboy import register
from tests.factories import ProfileFactory, UserFactory, EnquiryFactory

register(ProfileFactory)
register(UserFactory)
register(EnquiryFactory)

@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user
@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user

@pytest.fixture
def profile(db, profile_factory):
    user_profile = profile_factory.create()
    return user_profile
@pytest.fixture
def enquiry(db, enquiry_factory):
    new_enquiry = enquiry_factory.create()
    return new_enquiry