# Anime Scraper
An api for scraping anime websites.

# Installation Instructions:
1) git clone https://github.com/ArjixGamer/AnimeScraper-1
2) cd AnimeScraper-1
3) python -m pip install -r requirements.txt  
* If python 3 is set as python3 instead of python in your system then use that instead
4) python app.py

# Usage:

## Warning!
Make sure to urlencode any kind of data you pass to the api.

### 1) Get Available Providers
* Endpoint: ``apiUrl/get_providers``
* Method: GET
<details>
<summary>Response</summary>


```json
{
   "message":"ok",
   "data":[
      "4anime",
      "animefreak"
   ]
}
```
</details>


### 2) Search
* Endpoint: ``apiUrl/search/<string:searchQuery>?provider=<providerName>``
* Method: GET
<details>
<summary>Response</summary>


```json
{
   "message":"ok",
   "data":[
      {
         "link":"https://www.animefreak.tv/watch/overlord-ple-ple-pleiades-ova",
         "title":"Overlord: Ple Ple Pleiades (OVA)",
         "poster":""
      },
      {
         "link":"https://www.animefreak.tv/watch/overlord-iii",
         "title":"Overlord III",
         "poster":""
      },
      {
         "link":"https://www.animefreak.tv/watch/overlord",
         "title":"Overlord",
         "poster":""
      }
   ]
}
```
</details>

### 3) List-Episodes
* Endpoint: ``apiUrl/load_episodes?link=<animeLink>&provider=<providerName>``
* Method: GET
<details>
<summary>Response</summary>


```json
{
   "message":"ok",
   "data":[
      {
         "link":"https://www.animefreak.tv/watch/world-witches-hasshin-shimasu/episode/episode-1",
         "ep_no":1
      },
      {
         "link":"https://www.animefreak.tv/watch/world-witches-hasshin-shimasu/episode/episode-2",
         "ep_no":2
      },
      {
         "link":"https://www.animefreak.tv/watch/world-witches-hasshin-shimasu/episode/episode-3",
         "ep_no":3
      }
   ]
}
```
</details>

### 4) Extract Episode
* Endpoint: ``apiUrl/load_episode?provider=<providerName>&link=<episodeLink>&parent=<animeLink>``
* Method: GET
<details>
<summary>Response</summary>


```json
{
   "message":"ok",
   "data":{
      "link":"https://mountainoservo0002.animecdn.com/Shingeki-no-Kyojin-The-Final-Season/Shingeki-no-Kyojin-The-Final-Season-Episode-01-1080p.mp4",
      "headers":{
         "referer":"https://mountainoservo0002.animecdn.com/Shingeki-no-Kyojin-The-Final-Season/Shingeki-no-Kyojin-The-Final-Season-Episode-01-1080p.mp4"
      }
   }
}
```
</details>


## Note:
Before installing make sure git is installed on your machine.
