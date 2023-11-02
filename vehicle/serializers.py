from rest_framework import serializers

from vehicle.models import Car, Moto, Mileage


class MileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mileage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    last_mileage = serializers.SerializerMethodField()
    mileage = MileageSerializer(many=True)

    class Meta:
        model = Car
        fields = '__all__'

    @staticmethod
    def get_last_mileage(obj):
        first_mileage = obj.mileage.all().first().mileage

        if first_mileage:
            return first_mileage
        return None


class MotoSerializer(serializers.ModelSerializer):
    last_mileage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    @staticmethod
    def get_last_mileage(obj):
        first_mileage = obj.mileage.all().first().mileage

        if first_mileage:
            return first_mileage
        return None


class MotoMileageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Mileage
        fields = ('mileage', 'year', 'moto',)


class MotoCreateSerializer(serializers.ModelSerializer):
    mileage = MileageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'

    def create(self, validated_data):
        mileage = validated_data.pop('mileage')

        moto_item = Moto.objects.create(**validated_data)

        for m in mileage:
            Mileage.objects.create(**m, moto=moto_item)

        return moto_item
