from django.utils.functional import wraps
from django.shortcuts import redirect, get_object_or_404
from models import User

def authors_only(view):
    def wrapper(request, user_id, **kwargs):
        user = get_object_or_404(User, id=user_id)
        if user == request.user:
             return view(request, user_id, **kwargs)
        else:
            return redirect('/')
    return wraps(view)(wrapper)