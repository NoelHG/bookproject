from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

class BookView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        count = request.GET.get('count', '')
        author = request.GET.get('author', '')
        if count and count != '':
            queryset = queryset.filter(recommendationCount = count)

        if author and author != '':
            queryset = queryset.filter(author = author)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
