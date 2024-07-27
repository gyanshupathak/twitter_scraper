import asyncio
import json
from twikit import Client

USERNAME = 'gyanshu_pathak'
EMAIL = 'pathakgyanshu@gmail.com'
PASSWORD = 'Password@54321'

client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

    # Search tweets with keyword 'web3'
    tweets = await client.search_tweet('web3', 'Latest')

    # Create a list to store tweet data
    tweet_data = []

    # Collect data from tweets
    for tweet in tweets:
        tweet_data.append({
            'user': tweet.user.name,
            'text': tweet.text,
            'created_at': tweet.created_at
        })

    # Save tweet data to a JSON file
    with open('scraped_tweets.json', 'w') as f:
        json.dump(tweet_data, f, indent=4)

asyncio.run(main())
