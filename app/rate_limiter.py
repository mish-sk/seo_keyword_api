import redis
from fastapi import HTTPException, Request

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def rate_limiter(request: Request, limit: int = 10, period: int = 60):
    """Limits requests to 'limit' per 'period' seconds (default: 10 requests per 60 sec)."""
    client_ip = request.client.host  # Get user IP
    key = f"rate_limit:{client_ip}"

    request_count = redis_client.get(key)

    if request_count and int(request_count) >= limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")

    # Increment request count and set expiration if it's a new key
    redis_client.incr(key)
    redis_client.expire(key, period)
