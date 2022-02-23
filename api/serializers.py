from rest_framework import serializers
from .models import Article

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField(max_length=100)
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField(style={'base_template':'textarea.html'})
#     date_created = serializers.DateTimeField()
#     is_public = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.date_created = validated_data.get('date_created', instance.date_created)
#         instance.is_public = validated_data.get('author', instance.is_public)
#         instance.save()
#         return instance


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        # fields = ('id', 'author', 'title', 'content', 'date_created', 'is_public')
        fields = '__all__'

