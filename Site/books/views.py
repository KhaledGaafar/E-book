import datetime
from imaplib import _Authenticator
from django.shortcuts import render
from.models import book
from django.views.generic import ListView, DetailView
from django.shortcuts import reverse,redirect
from django.contrib import messages
from django.views.generic.edit import  UpdateView, DeleteView
from django.contrib.auth.models import User
from django.views import View
from .forms import productModelForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    books=book.get_all_products()
    return render(request,'books/home.html',context={'book':books})

class bookShowGenericView(DetailView):
    model = book
    template_name = 'books/show.html'



class bookDeleteGenericView(DeleteView):

     model = book
     template_name = 'books/crud/delete.html'
     success_url = '/books/home/'
              
                


class CreatebookView(View):

    def get(self, request):
        form = productModelForm()
        return render(request, 'books/crud/create.html', {'form': form})

    def post(self, request):
        form = productModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'books/crud/create.html', {'form': form})
def borrowbooks(request,id):
     boo=book.get_specific_book(id)
     boo.borrow=request.user.id
     boo.updated_at=datetime.datetime.now()
     boo.save()
     return redirect('books-home')

     
def showbook(request):
    
    borrow= book.objects.filter(borrow=request.POST.get('id', None))
    return render (request,'books/book.html',context={'borrow':borrow})

def showbookUser(request):
    
    borrow= book.objects.filter(borrow=request.user.id)
    return render (request,'books/bookuser.html',context={'borrow':borrow})

class bookUpdateGenericView(UpdateView):
    model = book
    form_class = productModelForm
    template_name = 'books/crud/updated.html'
    success_url = '/books/home/'


def users(request):
     use=User.objects.all()
     return render(request,'books/users.html',context={'use':use})     



def search_user(request):
    
    if request.method == "POST":
        query_id = request.POST.get('id', None)
        if query_id:
            results = User.objects.filter(id__contains=query_id)
            return render(request, 'books/search.html', {"results":results})

    return render(request, 'books/search.html')
