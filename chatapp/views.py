from django.shortcuts import render
from chatapp.models import User

# Create your views here.


def index(request):
    num_users = User.objects.count()

    context = {
        'num_users': num_users,
    }

    return render(request, 'index.html', context=context)
