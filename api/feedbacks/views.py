from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import FeedbackSerializer, ReportSerializer, ReportImageSerializer


class FeedbackAPIView(CreateAPIView):
    serializer_class = FeedbackSerializer


class ReportAPIView(CreateAPIView):
    serializer_class = ReportSerializer


class ReportImageAPIView(CreateAPIView):
    serializer_class = ReportImageSerializer
    parser_classes = parser_classes = (MultiPartParser, FormParser)
