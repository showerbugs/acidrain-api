# acidrain-api

## API Docs

### 회원

#### 회원 가입

- URL: POST /users/
- 파라메터: `name`, `password`
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

- `name`이 중복되는 경우

```
{
    "success": false,
    "message": "this name already exists"
}
```

#### 로그인

- URL: POST /session/
- 파라메터: `name`, `password`
- 성공:

```
{
    "success": true,
    "user": {
        "name": "qodot",
        "joined_at": "2017-08-05T09:09:37.084Z",
        "last_signin_at": "2017-08-05T09:09:37.084Z"
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

- 인증에 실패한 경우

```
{
    "success": false,
    "message": "authentication failed"
}
```

#### 로그아웃

- URL: DELETE /session/
- 파라메터: 없음
- 성공:

```
{
    "success": true,
}
```

- 세션이 없는 경우

```
{
    "success": false,
    "message": "login required"
}
```

### 평가

#### 평가 시작

- URL: GET /sentences/
- 파라메터:
    - `assessment_type`: word(단어), sentence(문장)
    - `difficulty`: 3(상), 2(중), 1(하)
    - `sentence_count`
- 성공:

```
{
    "success": True,
    "sentences": [{
        "body": "apple",
        "difficulty": 1,
        "type": "word"
    }]
}
```

- 요청의 바디가 없을 경우:

```
{
    "success": false,
    "message": "no request body"
}
```

- 세션이 없는 경우

```
{
    "success": false,
    "message": "login required"
}
```

- `assessment_type `, `difficulty `, `sentence_count`가 없을 경우:

```
{
    "success": false,
    "message": "assessment_type, difficulty, sentence_count is required,
}
```

- 요청한 숫자보다 전체 문제 셋이 더 적은 경우

```
{
    "success": false,
    "message": "sentences are not enough"
}
```

#### 평가 끝
