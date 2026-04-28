"""
Users API Serializers

Handles validation and representation for:
    - User registration (RegisterSerializer)
    - User login (LoginSerializer)
    - User profile read/update (UserSerializer, ProfileUpdateSerializer)
    - Password change (PasswordChangeSerializer)
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Read-only user profile serializer.
    Exposes public fields plus role-based flags.
    """
    is_admin = serializers.BooleanField(read_only=True)
    is_recruiter = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'company', 'title', 'ai_tools_used',
            'is_admin', 'is_recruiter',
            'date_joined', 'updated_at',
        ]
        read_only_fields = ['id', 'date_joined', 'updated_at']


class RegisterSerializer(serializers.ModelSerializer):
    """
    User registration serializer.
    Validates password strength and ensures role is not ADMIN on self-registration.
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'password_confirm',
            'first_name', 'last_name', 'role', 'company', 'title'
        ]

    def validate_role(self, value):
        """Prevent self-registration as ADMIN."""
        if value == 'ADMIN':
            raise serializers.ValidationError(
                "Admin role cannot be self-assigned. Contact the site administrator."
            )
        return value

    def validate(self, attrs):
        """Ensure passwords match."""
        if attrs['password'] != attrs.pop('password_confirm'):
            raise serializers.ValidationError(
                {"password_confirm": "Passwords do not match."}
            )
        return attrs

    def create(self, validated_data):
        """Create user with hashed password."""
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    Login serializer using username + password.
    Returns the authenticated user object on success.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"username": "No account found with this username."}
            )

        if not user.check_password(password):
            raise serializers.ValidationError(
                {"password": "Incorrect password."}
            )

        if not user.is_active:
            raise serializers.ValidationError(
                {"non_field_errors": "This account has been deactivated."}
            )

        attrs['user'] = user
        return attrs


class ProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Partial profile update serializer.
    Does not allow role changes via profile endpoint.
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'company', 'title', 'ai_tools_used']


class PasswordChangeSerializer(serializers.Serializer):
    """
    Password change serializer requiring old password verification.
    """
    old_password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    new_password_confirm = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError(
                {"new_password_confirm": "New passwords do not match."}
            )
        return attrs
