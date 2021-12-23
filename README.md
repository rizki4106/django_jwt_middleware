# django_jwt_middleware

`django_jwt_middleware` is a lightweight package used for create authorized request with jsonwebtoken on your function view

## Installation

```bash
pip3 install django_jwt_middleware
```

or clone

```bash
git clone https://github.com/rizki4106/django_jwt_middleware.git
```

<hr/>

## Example

### with http cookie

If you store jwt key on cookie you can use `@verify_jwt_cookie` decorator

```python
from django_jwt_middleware import verify_jwt_cookie
from rest_framework.decorators import api_view
from rest_framework.response import Response

@verify_jwt_cookie(cookie_name="example-token", jwt_key="supersecretkey", algorithm="HS256")
def hello_world(request):
    return Response(data={
        "message": "hello world"
    })
```

`@verify_jwt_cookie` takes 3 arguments
| name | type | description |
| ---- | ---- | ----------- |
| cookie_name | string | name of cookie that store your jwt token |
| jwt_key | string | jsonwebtoken secret key |
| algoritm | string | algorithm to decoded your jwt key default is HS256 |

<hr/>

### With http headers

If you store jwt key http headers you can use `@verify_jwt_header` decorator

```python
from django_jwt_middleware import verify_jwt_header
from rest_framework.decorators import api_view
from rest_framework.response import Response

@verify_jwt_header(header_name="example-token", jwt_key="supersecretkey", algorithm="HS256")
def hello_world(request):
    return Response(data={
        "message": "hello world"
    })
```

`@verify_jwt_header` takes 3 arguments
| name | type | description |
| ---- | ---- | ----------- |
| header_name | string | name of header that store your jwt token |
| jwt_key | string | jsonwebtoken secret key |
| algoritm | string | algorithm to decoded your jwt key default is HS256 |
