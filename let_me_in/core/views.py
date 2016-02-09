# import requests

# from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from let_me_in.core.dbapi import create_user, get_user_by_email, \
    get_user_by_uuid


@csrf_exempt
def register(request):
    """
    Register an Email
    """
    secret = request.POST.get("secret")
    response = request.POST.get("response")
    email = request.POST.get("email", "").strip()
    uuid = request.POST.get("uuid")
    name = request.POST.get("name")
    referrer = None
    if not (secret and response):
        return JsonResponse({
            'message': 'Both secret and respose data is required!'},
            status=400)
    if not email:
        return JsonResponse({
            'message': 'Email is required!'}, status=400)
    user = get_user_by_email(email)
    if user:
        return JsonResponse({
            'message': 'Email already registered!'}, status=400)
    if uuid:
        referrer = get_user_by_uuid(uuid)
        if not referrer:
            return JsonResponse({
                'message': 'Invalid referrer id!'}, status=400)
    user = create_user(email=email, name=name, referrer=referrer)
    return JsonResponse({
        'message': 'Registration successful: %s' % str(user.uuid),
        'uuid': str(user.uuid),
    })
