Common Company FastAPI Structure

```
my_project/
├── alembic/                    # migration scripts
│   ├── versions/
│   └── env.py
├── alembic.ini
├── src/
│   ├── __init__.py
│   ├── main.py                 # creates FastAPI app, includes routers
│   ├── config.py                # Settings via pydantic-settings, reads .env
│   ├── database.py               # engine, SessionLocal, Base, get_db
│   ├── dependencies.py           # shared Depends() (get_current_user, pagination, etc.)
│   ├── exceptions.py             # custom exception classes + handlers
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── router.py              # @router.post("/token") etc.
│   │   ├── schemas.py              # Pydantic: LoginRequest, Token, TokenData
│   │   ├── service.py               # business logic: authenticate_user, create_token
│   │   └── utils.py                  # password hashing, jwt helpers
│   │
│   ├── users/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py                # SQLAlchemy ORM model: User
│   │   └── service.py
│   │
│   ├── todos/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   └── service.py
│   │
│   └── core/
│       ├── security.py            # shared JWT/password logic
│       └── logging.py
│
├── tests/
│   ├── conftest.py                # fixtures: test db, test client, overrides
│   ├── test_auth.py
│   ├── test_users.py
│   └── test_todos.py
│
├── .env
├── .env.example
├── requirements.txt / pyproject.toml
├── Dockerfile
├── docker-compose.yml
└── README.md
```