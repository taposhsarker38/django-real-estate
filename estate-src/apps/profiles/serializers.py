from django_countries.fields import CountryField
from rest_framework import serializers

from apps.ratings.serializers import RatingSerializer

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    full_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.CharField(source="user.email")
    country = CountryField()
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone_number",
            "about_me",
            "lincence",
            "profile_photo",
            "gender",
            "country",
            "city",
            "is_buyer",
            "is_seller",
            "top_agent",
            "rating",
            "num_reviews",
            "reviews",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_reviews(self, obj):
        reviews = obj.agent_review.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation["top_agent"] = True
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField()

    class Meta:
        model = Profile
        fields = [
            "phone_number",
            "about_me",
            "lincence",
            "profile_photo",
            "gender",
            "country",
            "city",
            "is_buyer",
            "is_seller",
            "is_agent",
        ]
