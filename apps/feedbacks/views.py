from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

from .models import Report


class ReportListView(ListView):
    # 제보 리스트 뷰
    template_name = 'feedbacks/list.html'
    queryset = Report.objects.all().order_by('-timestamp')
    paginate_by = 10


class ReportConfirmUpdateView(UpdateView):
    model = Report
    fields = [
        'is_confirm'
    ]
    success_url = reverse_lazy('feedback:list')