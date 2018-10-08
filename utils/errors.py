import json
from django.http import JsonResponse


def bad_request(message):
    if isinstance(message, dict):
        message = json.dumps(message)
    response = JsonResponse({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    if isinstance(message, dict):
        message = json.dumps(message)
    response = JsonResponse({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    if isinstance(message, dict):
        message = json.dumps(message)
    response = JsonResponse({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def not_found(message):
    if isinstance(message, dict):
        message = json.dumps(message)
    response = JsonResponse({'error': 'notfound', 'message': message})
    response.status_code = 404
    return response


def database_error(message):
    if isinstance(message, dict):
        message = json.dumps(message)
    response = JsonResponse({'error': 'database_error', 'message': message})
    response.status_code = 500
    return response
