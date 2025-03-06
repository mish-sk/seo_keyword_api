from app.cache import get_cached_data, set_cached_data
import requests


def scrape_google_autocomplete(query: str):
    cache_key = f"google:{query}"
    cached_result = get_cached_data(cache_key)
    if cached_result:
        return eval(cached_result)  # Convert string back to list

    url = f"https://www.google.com/complete/search?q={query}&client=firefox"
    response = requests.get(url)
    if response.status_code == 200:
        suggestions = response.json()[1]
        set_cached_data(cache_key, suggestions)  # Store in Redis
        return suggestions
    return []


def scrape_youtube_autocomplete(query: str):
    cache_key = f"youtube:{query}"
    cached_result = get_cached_data(cache_key)
    if cached_result:
        return eval(cached_result)

    url = f"https://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        suggestions = response.json()[1]
        set_cached_data(cache_key, suggestions)
        return suggestions
    return []


def scrape_reddit_keywords(subreddit="SEO"):
    cache_key = f"reddit:{subreddit}"
    cached_result = get_cached_data(cache_key)
    if cached_result:
        return eval(cached_result)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        keywords = [post["data"]["title"] for post in posts][:10]
        set_cached_data(cache_key, keywords)
        return keywords
    return []
