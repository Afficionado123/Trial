from django.shortcuts import render
from markdown2 import markdown
from . import util
from django import forms
from django.http import HttpResponseRedirect
import random
from django.urls import reverse
class NewPageForm(forms.Form):
    title = forms.CharField(label = "New Title")
    content = forms.CharField(label = "Enter the document in Markdown", widget=forms.Textarea)
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
     

    })

def content(request, contentname):
    return render(request,"encyclopedia/content.html",
    {   
        "contents": markdown (util.get_entry(contentname))
        
    })


def add(request):
    q = request.GET['q']
    if (q in util.list_entries() ):
         return render(request,"encyclopedia/content.html",
    {   
        "contents": markdown (util.get_entry(q))
        
    })
    else:
         return render(request, "encyclopedia/add.html",
    {    
              
               "contentname": q,
                "li": util.list_entries()
    })

def create(request):
    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "encyclopedia/create.html", {
                "form" : form
            })

    return render(request, "encyclopedia/create.html", {
        "form": NewPageForm(),
        
        
    })
     
def rand(request):
     
        li = util.list_entries()
        n = random.randint(0, len(li) - 1)
        prandom = li[n]
        page = markdown(util.get_entry(prandom))
       
        return render(request,"encyclopedia/content.html",{
           "contents": page
        })