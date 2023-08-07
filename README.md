

# A Twitter scraper with python by using Nitter.

It is also possible to download the images showed in tweets by passing the argument `save_images = True`. If you only want to scrape images, it is recommended to set the argument `display_type = image` to show only tweets that contain images. 

## Requirements : 

`pip install -r requirements.txt`

Note : You must have Chrome installed on your system. 

## Results :

### Tweets :

The CSV file contains the following features (for each tweet) :

- 'UserName' : 
- 'UserHandle' : UserName 
- 'Timestamp' : timestamp of the tweet
- 'Text' : tweet text
- 'Embedded_text' : embedded text written above the tweet. This can be an image, a video or even another tweet if the tweet in question is a reply
- 'Emojis' : emojis in the tweet
- 'Comments' : number of comments
- 'Likes' : number of likes
- 'Retweets' : number of retweets
- 'Image link' : link of the image in the tweet
- 'Tweet URL' : tweet URL

### Library :

The library is now available. To install the library, run :

`pip install Scrapper_Boot_Twitter==1.8`

After the installation, you can import and use the functions as follows:

```
from Scrapper_Boot_Twitter.Scrapper_Boot_Twitter import scrape
from Scrapper_Boot_Twitter.user import get_user_information, get_users_following, get_users_followers
```

**Scrape top tweets of with the hashtag #udom, in proximity and without replies:**  
**The process is slower as the interval is smaller (choose an interval that can divide the period of time between, start and max date)**

```
data = scrape(hashtag="UDOM", since="2021-08-05", until=None, account = None, interval=1, 
              headless=True, display_type="Top", save_images=False, 
              resume=False, filter_replies=True)
```

**This function will return a list that contains : **  
**["no. of following","no. of followers", "join date", "date of birth", "location", "website", "description"]**


### Terminal :

```
Scrape tweets.

optional arguments:
  -h, --help            ``IN CLI ONLY`` show this help message and exit
  --words WORDS         Words to search for. they should be separated by "//" : Cat//Dog.
  --account USERNAME
                        Tweets posted by account.
  --mention_account MENTION_ACCOUNT
                        Tweets that mention "mention_account" account.         
  --hashtag HASHTAG
                        Tweets containing #hashtag
  --until UNTIL         End date for search query. example : %Y-%m-%d.
  --since SINCE
                        Start date for search query. example : %Y-%m-%d.
  --interval INTERVAL   Interval days between each start date and end date for
                        search queries. example : 5.
  --lang LANG           Tweets language. Example : "en" for english and "sw"
                        for Swahili.
  --headless HEADLESS   Headless webdrives or not. True or False
  --limit LIMIT         Limit tweets to be scraped.
  --display_type DISPLAY_TYPE
                        Display type of Twitter page : Latest or Top tweets
  --resume RESUME       Resume the last scraping. specify the csv file path.
  --location COUNTRY/REGION     Geographical location Example Tanzania, or Dodoma
  --filter_Media FILTER MEDIA
                        Filter based on MEDIA
  --filter_News FILTER NEWS   Fileter based on NEWS
  --filter_Retweets FILTER RETWEETS
                        Filter based on RETWEETS
```

### To run the script :
`python scrapper_boot.py --words "Challenge//CTF" --to_account "MasterCode112"  --until 2020-01-05 --since 2020-01-01 --limit 10 --interval 1 --display_type Latest --lang="en" --headless True`
