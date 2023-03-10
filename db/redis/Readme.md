## Redis install

macos
> brew install redis

linux
> sudo apt-get install redis-server

## Run

macos
> brew services start redis


## Connect

> redis-cli

### SET, GET, DELETE

> SET foo 43

> GET foo

> DELETE foo

### создание переменной на 20 сек
> SET foo '42' EX 20

### установка жизни переменной на 20 сек
> EXPIRE foo 20

### show all keys
> KEYS *