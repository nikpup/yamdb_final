from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title, YaUser


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model data."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    def validate(self, attr):
        """There is possible to live only one review on masterpiece."""
        if self.context.get('view').request.method == 'POST':
            title_id = self.context.get('view').kwargs.get('title_id')
            author = self.context.get('view').request.user
            if Review.objects.filter(title=title_id).filter(author=author):
                raise serializers.ValidationError(
                    'Вы уже оставили отзыв на это произведение!'
                )
        return attr

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('id', 'author', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model data."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('id', 'author', 'pub_date')


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model data."""

    class Meta:
        model = Category
        exclude = ('id', )
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for Genre model data."""

    class Meta:
        model = Genre
        exclude = ('id', )
        lookup_field = 'slug'


class TitleReadSerializer(serializers.ModelSerializer):
    """Serializer to read Title model data."""
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(
        read_only=True,
        many=True
    )
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class TitleWriteSerializer(serializers.ModelSerializer):
    """Serializer to write Title model data."""
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        model = Title
        fields = '__all__'


class YaUserSerializer(serializers.ModelSerializer):
    """Serializer for YaUser model."""

    class Meta:
        model = YaUser
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )


class NotAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = YaUser
        fields = (
            'id', 'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )
        read_only_fields = ('id', 'role',)


class GetTokenSerializer(serializers.ModelSerializer):
    """Checking username and confirmation code before giving token."""
    username = serializers.CharField(
        required=True
    )
    confirmation_code = serializers.CharField(
        required=True
    )

    class Meta:
        model = YaUser
        fields = (
            'username',
            'confirmation_code'
        )


class SignUpSerializer(serializers.ModelSerializer):
    """Checking Email and username before signing up."""

    class Meta:
        model = YaUser
        fields = ('email', 'username')
