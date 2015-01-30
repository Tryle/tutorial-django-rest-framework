# coding=utf-8

"""
TODO
"""

from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from models import Snippet
from serializers import SnippetSerializer
from serializers import UserSerializer
from permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):

    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy`actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    # noinspection PyUnusedLocal
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        """
        TODO
        :param request: TODO
        :param args: TODO
        :param kwargs: TODO
        :return: TODO
        """
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        """
        TODO
        :param serializer:
        """
        serializer.save(owner=self.request.user)


@api_view(('GET',))
def api_root(request, _format=None):
    """
    TODO
    :param request:
    :param _format:
    :return:
    """
    return Response({
        'users': reverse('user-list', request=request, format=_format),
        'snippets': reverse('snippet-list', request=request, format=_format)
    })