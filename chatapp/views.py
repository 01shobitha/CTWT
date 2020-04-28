from django.shortcuts import render
from chatapp.models import User, Message
import operator
from itertools import chain
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    num_users = User.objects.filter(is_superuser=False).count()
    current_user = request.user
    curr_name = current_user.first_name
    x = Message.objects.filter(to_user_id=current_user).order_by('-id')
    y = Message.objects.filter(from_user_id=current_user).order_by('-id')
    result_list = list(chain(x, y))
    result_list.sort(key=operator.attrgetter('id'), reverse=True)

    context = {
        'num_users': num_users,
        'curr_name': curr_name,
        'result_list': result_list,
    }

    return render(request, 'index.html', context=context)
