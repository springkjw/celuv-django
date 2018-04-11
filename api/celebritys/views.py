from rest_framework.generics import ListAPIView

from .serializers import CelebritySerializer


class CelebrityLikeListAPIView(ListAPIView):
    # 좋아요한 연예인 리스트 API
    serializer_class = CelebritySerializer

    def get_queryset(self):
        queryset = self.request.user.celebrity_set.all()
        return queryset