# # tests/profiles/test_serializers.py
# import pytest
# from apps.profiles.serializers import ProfileSerializer
# from tests.factories import ProfileFactory, RatingFactory

# @pytest.mark.django_db
# def test_profile_serializer_full_name():
#     # Create a profile instance with a user.
#     profile = ProfileFactory()
#     serializer = ProfileSerializer(instance=profile)
#     data = serializer.data

#     # Expected full name computation
#     expected_full_name = f"{profile.user.first_name.title()} {profile.user.last_name.title()}".strip()
#     assert data['full_name'] == expected_full_name, "The full_name should be correctly computed."

# @pytest.mark.django_db
# def test_profile_serializer_reviews():
#     # Create a profile and attach three ratings to it
#     profile = ProfileFactory()
#     for _ in range(3):
#         RatingFactory(agent=profile)
    
#     serializer = ProfileSerializer(instance=profile)
#     data = serializer.data

#     # Check that reviews are returned as a list with 3 entries
#     assert isinstance(data['reviews'], list), "Reviews should be a list."
#     assert len(data['reviews']) == 3, "There should be exactly 3 review entries."

# @pytest.mark.django_db
# def test_profile_serializer_top_agent_flag():
#     # Create a profile instance with top_agent True
#     profile = ProfileFactory(top_agent=True)
#     serializer = ProfileSerializer(instance=profile)
#     data = serializer.data

#     # Assert that the top_agent flag appears as True in the representation
#     assert data.get("top_agent") is True, "The profile should be marked as top_agent in the output."
