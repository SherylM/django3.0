from django.shortcuts import render,get_object_or_404
from .models import Textbook
from .models import Prepbook

# Create your views here.
def index(request):
    all_textbooks = Textbook.objects.all()
    all_prepbooks = Prepbook.objects.all()
    context = {
        'all_textbooks': all_textbooks,
        'all_prepbooks': all_prepbooks,
        }
    return render(request, 'buytextbooks/index.html', context)

def detail(request, book_id):
    textbook = get_object_or_404(Textbook, pk = book_id)
    prepbook = get_object_or_404(Prepbook, pk = book_id)
    return render(request, 'buytextbooks/detail.html', {'textbook': textbook,'prepbook': prepbook})

    
def home(request):
    return render(request, 'buytextbooks/testRun.html')
