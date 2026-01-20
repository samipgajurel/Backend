from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Intern

User = get_user_model()


class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = "__all__"
