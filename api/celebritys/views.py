from django.db.models import Count
from rest_framework.generics import ListAPIView

from apps.celebritys.models import Celebrity
from .serializers import CelebritySerializer, CelebrityListSerializer


class CelebrityListAPIView(ListAPIView):
    # 연예인 리스트 API
    serializer_class = CelebrityListSerializer
    queryset = Celebrity.objects.all()

    def get_query_parms(self):
        name = self.request.GET.get('name', None)
        return name

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.get_query_parms():
            queryset = queryset.filter(name__icontains=self.get_query_parms())

        queryset_is_like = queryset.filter(like=self.request.user)\
            .annotate(like_count=Count('like'))\
            .order_by('-like_count')
        queryset_is_not_like = queryset.exclude(like=self.request.user)\
            .annotate(like_count=Count('like'))\
            .order_by('-like_count')

        return queryset_is_like.union(queryset_is_not_like)


class CelebrityLikeListAPIView(ListAPIView):
    # 좋아요한 연예인 리스트 API
    serializer_class = CelebritySerializer

    def get_queryset(self):
        queryset = self.request.user.celebrity_set.all()
        return queryset