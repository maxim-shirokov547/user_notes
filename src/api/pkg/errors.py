import traceback

from django.http import JsonResponse

from api.logging import log


def error_response(code, message, status=400):
    return JsonResponse(
        {
            'errors': [
                {
                    'code': code,
                    'message': message,
                }
            ]
        },
        status=status,
    )


def handler500(request):
    log.critical('Unexpected 500\n' + traceback.format_exc())
    return error_response('unknown', 'Something went wrong. Please try again later.', status=500)


def handler400(request, exception):
    log.error('Unexpected 400\n' + traceback.format_exc())
    return error_response('unknown', 'Something went wrong. Please try again later.', status=400)


def handler404(request, exception):
    return error_response('not_found', 'Not found.', status=404)


def handler403(request, exception):
    return error_response('forbidden', 'You are not authorized to make this request.', status=403)
