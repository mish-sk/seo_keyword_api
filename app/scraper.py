import requests


def scrape_google_autocomplete(query: str):
    url = f"https://www.google.com/complete/search?q={query}&client=firefox"
    response = requests.get(url)
    if response.status_code == 200:
        suggestions = response.json()[1]
        return suggestions
    return []


def scrape_youtube_autocomplete(query: str):
    url = f"https://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        suggestions = response.json()[1]
        return suggestions
    return []


def scrape_reddit_keywords(subreddit="SEO"):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        keywords = [post["data"]["title"] for post in posts]
        return keywords[:10]  # Return top 10 trending topics
    return []
