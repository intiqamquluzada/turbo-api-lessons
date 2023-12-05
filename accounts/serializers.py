from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, allow_blank=False
    )

    # class Meta:
    #     model = User
    #     fields = ("username", "password")

    def validate(self, attrs):
        username = attrs.get("username")
        user = User.objects.filter(username=username)
        password = attrs.get("password")

        if not user.exists():
            raise serializers.ValidationError({"error": "not found user"})

        user = user.get()

        if not user.check_password(password):
            raise serializers.ValidationError({"error": "wrong password"})

        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, allow_blank=False
    )

    class Meta:
        model = User
        fields = ("username", "password",)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"error": "this user already registered"})

        return attrs

    def save(self):
        account = User(
            username=self.validated_data['username'],


        )
        password = self.validated_data['password']

        account.set_password(password) #sha256
        account.save()
        return account