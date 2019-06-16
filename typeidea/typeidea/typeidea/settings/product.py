
REDIS_URL = '127.0.0.1:6379:1'

CACHES = {
    'default' : {
        'BACKEND' : 'django_redis.cache.RedisCache',
        'LOCATION' : REDIS_URL,
        'TIMEOUT' : 300,
        'OPTIONS' : {
            # 'PASSWORD' : '<对应密码>',
            'CLIENT_CLASS' : 'django_redis.client.DefaultClient',
            'PARSER_CLASS' : 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis_connection.BlockingConnectionPool',
    }
}