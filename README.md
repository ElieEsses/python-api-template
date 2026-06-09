# FastAPI Template

Minimal FastAPI starter with SQLite, CORS, JWT auth, and environment-based config.

## Setup

```bash
cp .env.example .env
chmod +x run.sh
./run.sh
```

API runs at `http://localhost:8000`. Docs at `/docs`.

## Env Variables

| Variable                          | Default                   |
|-----------------------------------|---------------------------|
| `DEBUG_MODE`                      | `false`                   |
| `PORT`                            | `8000`                    |
| `FRONTEND_ORIGINS`                | `http://localhost:3000`   |
| `DB_PATH`                         | `./data.db`               |
| `DB_SCHEMA_PATH`                  | `./Project/db/schema.sql` |
| `JWT_SECRET_KEY`                  | *(required)*              |
| `JWT_ALGORITHM`                   | *(required, e.g. `HS256`)*|
| `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` | `60`                      |

## Database

Use `get_db()` from `Project/db/DBUtils.py` to query SQLite. It auto-commits on success and rolls back on exception.

```python
with get_db() as db:
    row = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
```

`init_db(db_schema_path)` runs the schema SQL file to create tables. It's called automatically on startup from `main.py`.

Schema is in `Project/db/schema.sql`. Default tables: `users` and `data`.

## Auth

Cookie-based JWT. Endpoints: `POST /auth/signup`, `POST /auth/login`, `POST /auth/logout`, `GET /auth/me`.

Protect a route with the `get_current_user` dependency:

```python
from fastapi import Depends
from Project.models.auth import UserResponse
from Project.services.auth import get_current_user

@router.get("/protected")
def protected(user: UserResponse = Depends(get_current_user)):
    ...
```

## Adding a Route

Create `Project/routes/yourroute.py` with a `router = APIRouter()`, then add it to `all_routes` in `Project/routes/__init__.py`.

## Linting & Formatting

Use `ruff check . --fix && ruff format .` for auto-fix, linting, and formatting
Config in pyproject.toml: line length 88, double quotes, checks pycodestyle, pyflakes, imports, bugbear, and pyupgrade.