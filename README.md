Init project for local development with provided dump (configured with docker-compose.local.yml)

```bash
docker compose -f docker-compose.yml -f docker-compose.local.yml up
```

Project will start nginx at 80 port forwarding /api/ and /admin/ locations to django backend.

Backend also will be accessable at 8000 port only for ya.practicum postman tests. (movies_admin/tests/movies API.postman_collection.json)