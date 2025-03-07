from fastapi import APIRouter, Depends, Request
from app.scraper import scrape_google_autocomplete, scrape_youtube_autocomplete, scrape_reddit_keywords
from app.rate_limiter import rate_limiter

router = APIRouter()


@router.get("/keywords/google", dependencies=[Depends(rate_limiter)])
async def google_keywords(query: str):
    return {"keywords": scrape_google_autocomplete(query)}


@router.get("/keywords/youtube", dependencies=[Depends(rate_limiter)])
async def youtube_keywords(query: str):
    return {"keywords": scrape_youtube_autocomplete(query)}


@router.get("/keywords/reddit", dependencies=[Depends(rate_limiter)])
async def reddit_keywords(subreddit: str = "SEO"):
    return {"keywords": scrape_reddit_keywords(subreddit)}
