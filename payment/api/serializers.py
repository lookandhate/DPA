from rest_framework import serializers

from payment.models import PaymentMethod, Discount, Payment


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class CreatePaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        exclude = ("created_by",)

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)

    def to_representation(self, instance):
        return PaymentMethodSerializer().to_representation(instance)


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class CreateDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ("created_by",)

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)

    def to_representation(self, instance):
        return DiscountSerializer().to_representation(instance)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ("created_by",)

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)

    def to_representation(self, instance):
        return PaymentSerializer().to_representation(instance)
