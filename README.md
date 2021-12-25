# django_jwt_middleware

`django_jwt_middleware` is a package used for authorize django request with JSON Web Tokens

## 1. Installation

```bash
pip3 install django-jwt-middleware
```

or clone

```bash
git clone https://github.com/rizki4106/django_jwt_middleware.git
```

<hr/>

## 2. Example

### with http cookie

If you store jwt key on cookie you can use `@middleware.with_cookie` decorator

```python
from django_jwt_middleware import middleware
from rest_framework.decorators import api_view
from rest_framework.response import Response

@middleware.with_cookie(cookie_name="example-token", jwt_key="supersecretkey", algorithm="HS256")
def hello_world(request):
    return Response(data={
        "message": "hello world"
    })
```

`@middleware.with_cookie` takes 3 arguments

| name        | type   | description                                        |
| ----------- | ------ | -------------------------------------------------- |
| cookie_name | string | name of cookie that store your jwt token           |
| jwt_key     | string | jsonwebtoken secret key                            |
| algoritm    | string | algorithm to decoded your jwt key default is HS256 |

<hr/>

### With http headers

If you store jwt key http headers you can use `@middleware.with_header` decorator

```python
from django_jwt_middleware import middleware
from rest_framework.decorators import api_view
from rest_framework.response import Response

@middleware.with_header(header_name="example-token", jwt_key="supersecretkey", algorithm="HS256")
def hello_world(request):
    return Response(data={
        "message": "hello world"
    })
```

`@middleware.with_header` takes 3 arguments

| name        | type   | description                                        |
| ----------- | ------ | -------------------------------------------------- |
| header_name | string | name of header that store your jwt token           |
| jwt_key     | string | jsonwebtoken secret key                            |
| algoritm    | string | algorithm to decoded your jwt key default is HS256 |

## 3. Response

| Type    | Description                                        |
| ------- | -------------------------------------------------- |
| success | Will continue to request destination               |
| failed  | Return http status code 403 with the message in it |

## 4. Discovered Problems

if you get error and it said `jwt has no attribute decode` try this command

```bash
pip3 uninstall pyjwt
pip3 install pyjwt
```
