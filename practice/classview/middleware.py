def my_middleware(get_response):
    print('init被调用')
    def middleware(request):
        print('before request被调用')
        response = get_response(request)
        print('after request被调用')
        return response
    return middleware


def my_middleware2(get_response):
    print('init2被调用')
    def middleware(request):
        print('before request2被调用')
        response = get_response(request)
        print('after request2被调用')
        return response
    return middleware