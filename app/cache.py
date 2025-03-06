import redis

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def get_cached_data(key: str):
    """Retrieve cached data from Redis."""
    cached_value = redis_client.get(key)
    if cached_value:
        print(f"🔹 Cache HIT: {key}")  # Debugging output
    else:
        print(f"🔸 Cache MISS: {key}")  # Debugging output
    return cached_value


def set_cached_data(key: str, value: list, expire_time: int = 3600):
    """Store data in Redis with an expiration time (default: 1 hour)."""
    redis_client.setex(key, expire_time, str(value))
    print(f"✅ Cached data in Redis: {key}")  # Debugging output
