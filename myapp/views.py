from django.shortcuts import render, redirect
from .models import BlogPost

def hello(request):
    return render(request, 'index.html')


def createpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(f"Title: {title}")
        print(f"Content: {content}")
        
        if title and content :
            BlogPost.objects.create(title=title, content=content)
            print("Data Saved Sucessfully")
            redirect("createpost.html")

    return render(request, 'createpost.html')
