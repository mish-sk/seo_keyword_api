from fastapi import APIRouter
from app.scraper import scrape_google_autocomplete, scrape_youtube_autocomplete, scrape_reddit_keywords

router = APIRouter()


@router.get("/keywords/google")
async def google_keywords(query: str):
    return {"keywords": scrape_google_autocomplete(query)}


@router.get("/keywords/google")
async def google_keywords(query: str):
    return {"keywords": scrape_google_autocomplete(query)}


@router.get("/keywords/youtube")
async def youtube_keywords(query: str):
    return {"keywords": scrape_youtube_autocomplete(query)}


@router.get("/keywords/reddit")
async def reddit_keywords(subreddit: str = "SEO"):
    return {"keywords": scrape_reddit_keywords(subreddit)}
