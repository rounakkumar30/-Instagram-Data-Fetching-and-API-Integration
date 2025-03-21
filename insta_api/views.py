import requests
from django.http import JsonResponse
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
from django.http import JsonResponse
import time
        
import requests
from django.shortcuts import render
from .forms import InstagramForm

ACCESS_TOKEN = "IGAAJh38TkRuJBZAE85anN4QmNGSW9nX0VJa1F4R3R6Smo1aWhBUmhjckJwMWJTMVI3bnNXVFhEQjRQMXBJblEyclV2UGVCeXpIZAUtKVGdGdk16T0JaOTRxUmdObkRuMDdOWWV4bUFxVXQ4OTZAlQ1djTFduRTNQSjJjajBNTVdZAbwZDZD"  # Replace with your actual token
USER_ID = "17841417510644967"  

def fetch_instagram_post(request):
    """Fetch the latest post from BBC News Instagram using the Instagram Graph API and render it as an HTML page."""
    url = f"https://graph.instagram.com/{USER_ID}/media?fields=id,caption,media_type,media_url&access_token={ACCESS_TOKEN}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "data" in data and data["data"]:
            latest_post = data["data"][0]
            context = {
                "caption": latest_post.get("caption", "No caption available"),
                "image_url": latest_post.get("media_url", "No image available"),
            }
            return render(request, "insta_api/instagram_post.html", context)

        else:
            logger.warning("No posts found for BBC News.")
            return render(request, "insta_api/instagram_post.html", {"error": "No posts found"})

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        return render(request, "insta_api/instagram_post.html", {"error": f"API request failed: {e}"})

# Configure logging
logger = logging.getLogger(__name__)

def fetch_instagram_post_scrape(request, username="bbcnews"):
    """Scrape Instagram to fetch the latest post caption and image."""
    url = f"https://www.instagram.com/{username}/"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run browser in the background
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        time.sleep(5)  # Allow time for the page to load

        # Find post elements (adjust selectors based on Instagram changes)
        posts = driver.find_elements(By.CLASS_NAME, "x1i10hfl")  # Class name might change
        if posts:
            post = posts[0]
            caption = post.text
            image = post.find_element(By.TAG_NAME, "img").get_attribute("src")

            return JsonResponse({"caption": caption, "image_url": image})

        return JsonResponse({"error": "No posts found"}, status=404)

    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        return JsonResponse({"error": f"Scraping failed: {e}"}, status=500)

    finally:
        driver.quit()
        
