import redis
r = redis.StrictRedis(host='127.0.0.1', port=6379)
pipe = r.pipeline()
pipe.set('point')
pipe.execute