import requests
from validate_email import validate_email

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from let_me_in.core.dbapi import create_user, get_user_by_email, \
    get_user_by_uuid


@csrf_exempt
def register(request):
    """
    Register an Email
    """
    if request.method != 'POST':
        return JsonResponse({
            'message': 'Only POST is allowed'}, status=405)
    response = request.POST.get("response")
    email = request.POST.get("email", "").strip()
    uuid = request.POST.get("uuid")
    name = request.POST.get("name", "").strip()
    if not response:
        return JsonResponse({
            'message': 'Respose from reCAPTCHA service is required!'},
            status=400)
    if not email:
        return JsonResponse({
            'message': 'Email is required!'}, status=400)
    if not validate_email(email):
        return JsonResponse({
            'message': 'Please enter a valid email address!'}, status=400)
    user = get_user_by_email(email)
    if user:
        return JsonResponse({
            'message': 'Email already registered!'}, status=400)
    referrer = get_user_by_uuid(uuid)
    # Uncomment block below for strict-referrel verification
    """
    if uuid and not referrer:
        return JsonResponse({'message': 'Invalid referrer id!'}, status=400)
    """

    # Verify with google for spam
    data = dict(respose=response, secret=settings.RECAPTCHA_SECRET)
    reply = requests.post(settings.RECAPTCHA_URL, data=data).json()
    if not reply['success']:
        return JsonResponse({
            'message': 'reCAPTCHA verification failed!',
            'error-codes': reply.get("error-codes"),
        }, status=400)

    # Everything is alright, create user!
    user = create_user(email=email, name=name, referrer=referrer)
    return JsonResponse({
        'message': 'Registration successful!',
        'uuid': str(user.uuid),
    })
