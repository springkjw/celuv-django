from django.db.models import Count
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response

from apps.celebritys.models import Celebrity
from .serializers import CelebritySerializer, CelebrityListSerializer, CelebrityLikeSerializer


class CelebrityListAPIView(ListAPIView):
    # 연예인 리스트 API
    serializer_class = CelebrityListSerializer
    queryset = Celebrity.objects.all()

    def get_query_parms(self):
        name = self.request.GET.get('name', None)
        return name

    def get_queryset(self):
        queryset = super().get_queryset().annotate(like_count=Count('like'))\
            .order_by('-like_count')

        if self.get_query_parms():
            queryset = queryset.filter(name__icontains=self.get_query_parms())
        return queryset


class CelebrityLikeListAPIView(ListAPIView):
    # 좋아요한 연예인 리스트 API
    serializer_class = CelebritySerializer

    def get_queryset(self):
        queryset = self.request.user.celebrity_set.all()
        return queryset


class CelebrityLikeAPIView(GenericAPIView):
    # 좋아요 API
    serializer_class = CelebrityLikeSerializer
    queryset = Celebrity.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance=self.get_object())
        serializer.is_valid()
        serializer.save()

        return Response()
