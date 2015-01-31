# -*- coding: utf-8 -*-

"""
Contain serializers of snippets app.
"""

from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    """
    This serializer allow create() and update() method.
    It is linked with the model `Snippet` and map the following
    fields: `url`, `title`, `code`, `linenos`, `language`
    and `style`. It serialize also `highlight` pilinwhich link the snippet
    to the highlighted code formatted as html, and `owner` which is
    the username of the owner.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta(object):

        """
        TODO
        """

        model = Snippet
        fields = ('url', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner',)


class UserSerializer(serializers.ModelSerializer):

    """
    This serializer allow create() and update() method.
    It is linked with the model `User` and map the following
    fields: `id` and `username`. It serialize also `snippets`
    which is a link to the snippets defined by the user.
    """

    snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)

    class Meta(object):

        """
        TODO
        """

        model = User
        fields = ('id', 'username', 'snippets')
