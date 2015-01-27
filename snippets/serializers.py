from rest_framework import serializers
from snippets.models import Snippet

# ModelSerializer is simply a shortcut for creating serializer classes:
# - An automatically determined set of fields
# - Simple default implementations for the create() and update() methods
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
