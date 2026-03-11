import redis
from functools import wraps
import pickle

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


def cache_with_redis(key_prefix: str, ttl: int):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = f"{key_prefix}:{args[0]}"
            cached_result = redis_client.get(key)
            if cached_result:
                return pickle.loads(cached_result)

            result = await func(*args, **kwargs)
            redis_client.setex(key, ttl, pickle.dumps(result))
            return result
        return wrapper
    return decorator


def invalidate_cache(key_prefix: str, identifier):
    key = f"{key_prefix}:{identifier}"
    redis_client.delete(key)