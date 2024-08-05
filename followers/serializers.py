from rest_framework import serializers
from followers.models import followers
from django.db import IntegrityError

class followeSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    followed_name = seralizers.ReadOnlyField()

    class Meta:
        model = Follower 
        fields = [
            'id', 'owner', 'created_at',
            'followed', 'followed_name',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
    