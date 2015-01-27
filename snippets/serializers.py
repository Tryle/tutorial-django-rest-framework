from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet

# ModelSerializer is simply a shortcut for creating serializer classes:
# - An automatically determined set of fields
# - Simple default implementations for the create() and update() methods
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner',)

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many = True, queryset = Snippet.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')