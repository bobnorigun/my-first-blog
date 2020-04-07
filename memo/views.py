from django.shortcuts import render, get_object_or_404, redirect

from django.views import generic

from .models import Memo

# memo
def memo_list(request):
    memos = Memo.objects.all()
    
    return render(request, 'memo/memo_list.html', {'memos': memos})

def memo_detail(request, pk):
    memo = get_object_or_404(memo, pk=pk)
    return render(request, 'memo/memo_detail.html', {'memo': memo})
