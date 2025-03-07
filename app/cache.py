import redis

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def get_cached_data(key: str):
    """Retrieve cached data from Redis."""
    return redis_client.get(key)


def set_cached_data(key: str, value: list, expire_time: int = 3600):
    """Store data in Redis with an expiration time (default: 1 hour)."""
    redis_client.setex(key, expire_time, str(value))


def get_last_search(query: str):
    """Retrieve the last stored search result from Redis."""
    key = f"result:{query}"
    return redis_client.get(key)


def store_search_result(query: str, result: list):
    """Store the last search result in Redis."""
    key = f"result:{query}"
    redis_client.setex(key, 3600, str(result))  # Store for 1 hour
    print(f"✅ Stored in Redis: {key} -> {result}")  # Debugging output
