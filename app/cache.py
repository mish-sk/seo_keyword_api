import os

import redis


REDIS_URL = os.getenv("REDIS_URL")

if REDIS_URL:
    try:
        redis_client = redis.from_url(REDIS_URL, decode_responses=True)
        redis_client.ping()  # Check if Redis is available
        print(f"✅ Connected to Redis: {REDIS_URL}")
    except redis.exceptions.ConnectionError:
        redis_client = None  # Disable Redis if not available
        print("⚠️ Redis connection failed. Caching is disabled.")
else:
    redis_client = None  # Disable Redis if REDIS_URL is not set
    print("⚠️ No REDIS_URL provided. Caching is disabled.")


def get_cached_data(key: str):
    """Retrieve cached data from Redis, or return None if Redis is unavailable."""
    if redis_client:
        return redis_client.get(key)
    return None  # No caching if Redis is disabled


def set_cached_data(key: str, value: list, expire_time: int = 3600):
    """Store data in Redis if available."""
    if redis_client:
        redis_client.setex(key, expire_time, str(value))


def get_last_search(query: str):
    """Retrieve the last stored search result from Redis."""
    if redis_client:
        return redis_client.get(f"result:{query}")
    return None  # No result storage if Redis is disabled


def store_search_result(query: str, result: list):
    """Store the last search result in Redis."""
    if redis_client:
        redis_client.setex(f"result:{query}", 3600, str(result))
