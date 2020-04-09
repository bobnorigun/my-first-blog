from django.shortcuts import render, get_object_or_404, redirect

from django.views import generic

from .models import Memo
from .forms import MemoForm

# memo
def memo_list(request):
    memos = Memo.objects.all()
    
    return render(request, 'memo/memo_list.html', {'memos': memos})

def memo_detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    return render(request, 'memo/memo_detail.html', {'memo': memo})

def event(request):
    return render(request, 'memo/event.html')

def memo_new(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('memo:memo_detail', pk=memo.pk) 
    else:
        form = MemoForm()
    return render(request, 'memo/memo_edit.html', {'form': form})