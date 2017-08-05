# acidrain-api

## API Docs

### 회원

#### 회원 가입

- URL: POST /users/
- 파라메터: name, password
- 성공:

```
{
    "success": true,
    "user": {
        "name": "qodot",
        "joined_at": "2017-08-05T09:09:37.084Z",
    }
}
```

- 요청의 바디가 없을 경우:

```
{
    "success": false,
    "message": "no request body"
}
```

- `name`, `password`가 없을 경우:

```
{
    "success": false,
    "message": "no name or password"
}
```
