# Online Dictation Backend

- create database
- import
  - vocabulary
  - user
- serve
  - routes
    - /auth/login/
    - /auth/logout/
    - /auth/refresh/
    - /assessment/:level/
    - /assessment/:record/
    - /tts/:vocab/
    - /list/:level/

## User Schema

```json
[
  {
    "userAlias": "string",
    "password": "string",
    "role": "string"
  }
]
```

## Vocabulary Schemas

```json
[
  {
    "id": "string",
    "title": "string",
    "partOfSpeech": "string",
    "definition": "string"
  }
]
```

## Build for linux (Digital Ocean)

GOOS=linux GOARCH=amd64 go build -o ./dictation_server main.go

## Use JWT for authentication
