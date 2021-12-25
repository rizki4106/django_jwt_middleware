from django.http import JsonResponse
import jwt


class JwtMiddleWare:

    def with_cookie(self, cookie_name = 'token', jwt_key = "", algorithm = "HS256"):
        """
        Verify json web token from cookie this decorator takes 3 arguments :
        1. cookie_name -> string -> cookie name where you store the token
        2. jwt_key -> string -> jwt secret key
        3. algorithm -> string -> default is HS256
        """
        def decorator(views_func):
            def container(request, *args, **kwargs):
                cookies = request.COOKIES
                # if cookie exists will continue to check token
                # if not exists will return 403 http status code
                if cookie_name in cookies:

                    # if token valid will continue to the next request
                    # if not valid will send 403 http status code
                    try:
                        jwt.decode(str(cookies.get(cookie_name)), jwt_key, algorithm)
                        return views_func(request, *args, **kwargs)

                    except Exception as err:

                        response = JsonResponse(data={
                            "status": 403,
                            "message": str(err)
                        })
                        response.status_code = 403
                        return response
                else:

                    response = JsonResponse(data={
                        "status": 403,
                        "message": "token cookie must be sent in request cookie as  {}".format(cookie_name)
                    })
                    response.status_code = 403
                    return response
            return container
        return decorator


    def with_header(self, header_name = 'token', jwt_key = "", algorithm = "HS256"):
        """
        Verify json web token from cookie this decorator takes 3 arguments :
        1. header_name -> string -> header name where you store the token
        2. jwt_key -> string -> jwt secret key
        3. algorithm -> string -> default is HS256
        """

        def decorator(views_func):
            def container(request, *args, **kwargs):
                headers = request.headers
                # if header exists will continue to check token
                # if not exists will return 403 http status code
                if header_name.lower() in headers:

                    # if token valid will continue to the next request
                    # if not valid will send 403 http status code
                    try:
                        jwt.decode(str(headers.get(header_name.lower())), jwt_key, algorithm)
                        return views_func(request, *args, **kwargs)

                    except Exception as err:

                        response = JsonResponse(data={
                            "status": 403,
                            "message": str(err)
                        })
                        response.status_code = 403
                        return response
                else:

                    response = JsonResponse(data={
                        "status": 403,
                        "message": "token headers must be sent in request header as {}".format(header_name.lower())
                    })
                    response.status_code = 403
                    return response
            return container
        return decorator

if __name__ != "__main__":

    middleware = JwtMiddleWare()