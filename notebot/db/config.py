from notebot import settings

TORTOISE_ORM = {
    "connections": settings.DATABASE_CONNECTIONS,
    "apps": {
        "models": {
            "models": ["notebot.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
    "routers": ["notebot.db.router.Router"],
}

TORTOISE_ORM2 = {
    "connections": {
        "default": "postgres://postgres:password@localhost:3434/notedb"
    },
    "apps": {
        "models": {
            "models": ["notebot.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
    "routers": ["notebot.db.router.Router"],
}
