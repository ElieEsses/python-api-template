import sqlite3
from contextlib import contextmanager
from pathlib import Path

from src.app.config import settings

DB_PATH = settings.db_path
DB_SCHEMA_PATH = settings.db_schema_path


@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db() -> None:
    schema = Path(DB_SCHEMA_PATH)
    with get_db() as conn:
        conn.executescript(schema.read_text(encoding="utf-8"))
