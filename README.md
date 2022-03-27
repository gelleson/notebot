# Notebot

Simple bot to keep

## Features
- [x] Keeps notes
    - [x] Keeps plain text notes and add hashtags as filter
    - [x] Keeps url notes and add hashtags as filter
- [ ] Can be used in a channel

## Installation
```bash
poetry install
```

## Getting Started

### Docker
```bash
docker build -t notebot .
docker run -d notebot
```

## Configuration

`LOG_LEVEL(default=INFO)` - Log level for the bot.<br>

`DATABASE_URLS(*required)`- list of database urls to connect. 
If you pass more than one url, the bot will connect to all of them. 
The first one will be used as the main database (write only). 
The others will be used as read-only. 
If you pass only one url, the bot will connect to the default database only. 
The urls are splits by ","<br>


`TELEGRAM_BOT_TOKEN(*required)` - token of the bot.<br>
`TELEGRAM_WEBHOOK_ENABLED(default=false)` - enable webhook for the bot.<br>
`TELEGRAM_WEBHOOK_HOST(*required-if=TELEGRAM_WEBHOOK_ENABLED=true)` - host of the webhook.<br>
`TELEGRAM_WEBHOOK_PATH(*required-if=TELEGRAM_WEBHOOK_ENABLED=true)` - url path of the webhook (example: /updates)<br>
`TELEGRAM_INTERNAL_HOST(default=0.0.0.0)` - host of the internal server.<br>
`TELEGRAM_INTERNAL_PORT(default=8443)` - port of the internal server.<br>
`TELEGRAM_STORAGE(default=memory)` - storage to use. Available storage to use are memory and redis(default memory).<br>
`TELEGRAM_STORAGE_REDIS_HOST(*required-if=TELEGRAM_STORAGE=redis)` - host of the redis server.<br>
`TELEGRAM_STORAGE_REDIS_PORT(default=6379)` - port of the redis server.<br>
`TELEGRAM_STORAGE_REDIS_DB(default=0)` - database of the redis server.<br>
`TELEGRAM_STORAGE_REDIS_PASSWORD(default=None)` - password of the redis server.<br>
`TELEGRAM_STORAGE_REDIS_POOL_SIZE(default=10)` - pool size of the redis server.<br>
`TELEGRAM_STORAGE_REDIS_PREFIX(default=fsm)` - prefix of the redis keys.<br>


