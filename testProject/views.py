from django.views import generic
from .models import Memo

class IndexView(generic.ListView):
    template_name = 'project/index.html'
    context_object_name = 'memoList'

    def get_queryset(self):
        """Return the all memos."""
        return Memo.objects.all()