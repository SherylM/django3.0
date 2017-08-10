from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Textbook
from .models import Prepbook

#Generic views
"""
In generic views, bascically what happened is that the normal view version was
greatly simplified. 
"""
class TextbookIndexView(generic.ListView):
    template_name = 'buytextbooks/textbooks.html'

    def get_queryset(self):
        #search feature
        return Textbook.objects.all()
            #returns object_list
    
class PrepbookIndexView(generic.ListView):
    template_name = 'buytextbooks/prepbooks.html'

    def get_queryset(self):
        #search feature
        return Prepbook.objects.all()
    
class TextbookDetailView(generic.DetailView):
     #A generic class that provides the template for viewing textbooks on the detail page
    model = Textbook
    template_name = 'buytextbooks/detailtextbook.html'

class PrepbookDetailView(generic.DetailView):
    model = Prepbook
    template_name = 'buytextbooks/detailprepbook.html'

class TextbookCreate(CreateView):
    model = Textbook
    fields = ['textbooktitle', 'textbookauthor','textbookpublisher','textbooklocation', 'textbookimage']
    
class PrepbookCreate(CreateView):
    model = Prepbook
    fields = ['prepbooktitle', 'prepbookauthor','prepbookpublisher','prepbooklocation', 'prepbookimage']

class TextbookUpdate(UpdateView):
    model = Textbook
    fields = ['textbooktitle', 'textbookauthor','textbookpublisher','textbooklocation', 'textbookimage']

class PrepbookUpdate(UpdateView):
    model = Prepbook
    fields = ['prepbooktitle', 'prepbookauthor','prepbookpublisher','prepbooklocation', 'prepbookimage']


#Normal Views: to view basic requests
def signup(request):
    return render(request, 'buytextbooks/signup.html')

def login(request):
    return render(request, 'buytextbooks/login.html')

def blog(request):
    return render(request, 'buytextbooks/blog.html')

def home(request):
    return render(request, 'buytextbooks/home.html')

def sell(request):
    return render(request, 'buytextbooks/sell.html')
