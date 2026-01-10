from faker import Faker
import random, json
from datetime import datetime

PLATFORM_PREFIX_MAP = {
    "Google Ads": "GA-",
    "Facebook Ads": "FB-",
    "TikTok Ads": "TT-",
    "YouTube Ads": "YT-"
}

fake = Faker()

# generate a single row for api (campaign_engagement)
def generate_api_data(platforms, i):
    
    campaign_id = f"{PLATFORM_PREFIX_MAP.get(platforms, 'XX-')}{i:04d}"
    
    return{
        "event_time": fake.iso8601(),
        "platform": platforms,
        "campaign_id": campaign_id,
        "page_views": random.randint(10, 400),
        "unique_vistors": random.randint(50, 300),
        "avg_time_on_site": round(random.uniform(1, 60),2),
        "bounce_rate": round(random.uniform(0, 1),2),
    }

# generate api list
def get_mock_api_data(num_rows_per_platform=100):
    platforms = ["Google Ads", "Facebook Ads", "TikTok Ads", "YouTube Ads"]
    data = []
    for platform in platforms:
        for i in range(1, num_rows_per_platform +1):
            row = generate_api_data(platform, i)
            data.append(row)
    return(data)    