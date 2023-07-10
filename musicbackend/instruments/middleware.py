import time
from django.core.cache import cache
from instruments.models import Request


class SaveRequest:
    def __init__(self, get_response):
        self.get_response = get_response

        # Filter to log all request to url's that start with any of the strings below.
        # With example below:
        # /example/test/ will be logged.
        # /other/ will not be logged.
        self.prefixs = [
            '/api/v1'
        ]

    def __call__(self, request):
        _t = time.time()
        response = self.get_response(request)
        _t = int((time.time() - _t)*1000)

        # если url не начинается с нужного префикса, то не сохраняем лог
        if not list(filter(request.get_full_path().startswith, self.prefixs)):
            return response 

        # создаем представление модели
        request_log = Request(
            endpoint=request.get_full_path(),
            response_code=response.status_code,
            method=request.method,
            remote_address=self.get_client_ip(request),
            exec_time=_t,
            body_response=str(response.content),
            body_request=str(request.body)
        )

        # указываем пользователя, если он не анонимный
        if not request.user.is_anonymous:
            request_log.user = request.user

        # кэшируем лог
        # request_log.save()
        cache.set('visit' + str(time.time()), request_log, 3600)

        data = cache.keys('*')
        print(1111111, data)
        return response

    # get clients ip address
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            _ip = x_forwarded_for.split(',')[0]
        else:
            _ip = request.META.get('REMOTE_ADDR')
        return _ip
