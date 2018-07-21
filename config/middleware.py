from re import compile
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from rest_framework.status import is_client_error, is_success

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    # 씨랩에서 로그인 필요 미들웨어
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL)
        return self.get_response(request)


class ResponseFormattingMiddleware(MiddlewareMixin):
    # API 응답 미들웨어
    METHOD = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE',)
    API_URLS = [compile(r'^api/')]

    def process_response(self, request, response):
        path = request.path_info.lstrip('/')

        if request.method in self.METHOD and \
                any(m.match(path) for m in self.API_URLS):
            response_format = {
                'result': {},
                'success': is_success(response.status_code),
                'message': None
            }

            if hasattr(response, 'data') and \
                    getattr(response, 'data') is not None:
                data = response.data
                response_format.update({'result': data})
                try:
                    for key in response_format.keys():
                        response_format[key] = data.pop(key)
                except KeyError:
                    response_format.update({'result': data})
                except TypeError:
                    response_format.update({'result': data})
                finally:
                    if is_client_error(response.status_code):
                        response_format[
                            'message'] = response_format.pop('result')
                        response_format['result'] = None
                    elif is_success(response.status_code):
                        response_format['message'] = response.status_text

                    response.data = response_format
                    response.content = response.render().rendered_content
            else:
                response.data = response_format
                try:
                    response.content = response.render().rendered_content
                except AttributeError:
                    pass

        return response