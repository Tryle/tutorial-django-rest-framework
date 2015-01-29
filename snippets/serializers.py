from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet

# ModelSerializer is simply a shortcut for creating serializer classes:
# - An automatically determined set of fields
# - Simple default implementations for the create() and update() methods
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name = 'snippet-highlight', format = 'html')
    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner',)

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(many = True, view_name = 'snippet-detail', read_only = True)
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')