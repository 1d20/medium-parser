from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['url', 'title', 'text']

    def validate(self, attrs):
        if 'author' in attrs:
            raise serializers.ValidationError('Author is read only field!')
        return super().validate(attrs)

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.author = self.context['request'].user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        # from ipdb import set_trace; set_trace()
        instance.author = self.context['request'].user
        instance.save()
        return instance
