from app.cache import get_cached_data, set_cached_data
import requests
from fastapi import HTTPException


def scrape_google_autocomplete(query: str):
    cache_key = f"google:{query}"
    cached_result = get_cached_data(cache_key)
    if cached_result:
        return eval(cached_result)

    url = f"https://www.google.com/complete/search?q={query}&client=firefox"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise exception for 4xx/5xx errors

        suggestions = response.json()[1]
        set_cached_data(cache_key, suggestions)
        return suggestions
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=408, detail="Request to Google timed out.")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Google API error: {str(e)}")


def scrape_youtube_autocomplete(query: str):
    cache_key = f"youtube:{query}"
    cached_result = get_cached_data(cache_key)
    if cached_result:
        return eval(cached_result)

    url = f"https://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q={query}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        suggestions = response.json()[1]
        set_cached_data(cache_key, suggestions)
        return suggestions
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=408, detail="Request to YouTube timed out.")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"YouTube API error: {str(e)}")


def scrape_reddit_keywords(subreddit="SEO"):
    cache_key = f"reddit:{subreddit}"
    cached_result = get_cached_data(cache_key)
    if cached_result:
        return eval(cached_result)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()

        posts = response.json()["data"]["children"]
        keywords = [post["data"]["title"] for post in posts][:10]
        set_cached_data(cache_key, keywords)
        return keywords
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=408, detail="Request to Reddit timed out.")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Reddit API error: {str(e)}")
