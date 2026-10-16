# database/__init__.py
import importlib
from config.settings import settings

_backends = {"postgres", "sqlite", "mysql", "mongodb", "firebase"}
db_type = settings.DB_TYPE.strip().lower()
if db_type not in _backends:
    raise RuntimeError(f"Unsupported DB_TYPE={settings.DB_TYPE!r}, must be one of {_backends}")

_mod = importlib.import_module(f"database.{db_type}")
get_connection = _mod.get_connection
user_queries = _mod