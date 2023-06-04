from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Follow, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Serializer class for groups"""
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', 'created')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        read_only=False,
        slug_field='username'
    )

    def validate(self, data):
        user = self.context['request'].user
        follower = data['following']
        if user == follower:
            raise serializers.ValidationError(
                'Follow himself prohibited'
            )
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')
        # Проверяет существует ли уже такая подписка на пользователя

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Такая подписка уже существует'
            )
        ]
