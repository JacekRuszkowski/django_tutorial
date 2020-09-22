from django.shortcuts import render

posts = [
    {
        'author': 'JacekR',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 20, 2020',
    },
    {
        'author': 'DorotaN',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 21, 2020',
    }
]



def home(request):
    context = {
        'posts': posts # zaciąganie postów z listy powyżej. Czemu w słowniku?
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
