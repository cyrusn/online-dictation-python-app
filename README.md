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
