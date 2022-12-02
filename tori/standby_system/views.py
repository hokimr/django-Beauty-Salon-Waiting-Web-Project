from crypt import methods
from time import time
from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView
from standby_system.models import waiting
from .forms import WaitingForm
from django.db.models import Count

# Create your views here.


class HomeView(TemplateView):
    template_name = 'standby_system/home.html'


class WaitingCreate(CreateView):
    model = waiting
    form_class= WaitingForm
    initial = {'designer':'Surgery'}
    #model_form.html
    success_url = reverse_lazy('standby:home')
    context_object_name = 'waiting'


class WaitingListView(ListView):
    model = waiting
    context_object_name = 'waiting'
    template_name = 'waiting_list'
    time = 0
    # time = waiting.objects.filter(Surgery__contains='커트')
    # number_wild_books = time.count()*10

    def get_queryset(self):
        return waiting.objects.filter(designer=self.kwargs['name'])
    # queryset = waiting.objects.filter(designer="제")
    # extra_context = {'name':self.name}


    def waiting_time(self):
        queryset_1 = waiting.objects.filter(
        designer__startswith=self.kwargs['name'],
        Surgery__startswith='커트'
        )
        return queryset_1.count()*10

    
        
    def get_context_data(self, **kwargs):
        context = super(WaitingListView, self).get_context_data(**kwargs)

        cut_count_time = waiting.objects.filter(
        designer__startswith=self.kwargs['name'],
        Surgery__startswith='커트'
        )
        perm_count_time = waiting.objects.filter(
        designer__startswith=self.kwargs['name'],
        Surgery__startswith='펌'
        )
        magic_count_time = waiting.objects.filter(
        designer__startswith=self.kwargs['name'],
        Surgery__startswith='매직'
        )

        c=cut_count_time.count()*600
        p=perm_count_time.count()*3600
        m=magic_count_time.count()*1800


        total_time=c+p+m

        hours = total_time // 3600
        s = total_time - hours*3600
        mu = s // 60
    

        context.update({'designer_name': self.kwargs['name'],'time':f"예상 대기 시간 {hours} 시간 {mu} 분 "})
        return context

class WaitingDelete(DeleteView):
    model = waiting
    success_url = reverse_lazy('standby:home')
