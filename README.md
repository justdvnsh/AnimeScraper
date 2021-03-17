## Anime Scraper
An api for scraping anime websites.

## Installation Instructions:
1) git clone https://github.com/ArjixGamer/AnimeScraper-1
2) cd AnimeScraper-1
3) python -m pip install -r requirements.txt  
* If python 3 is set as python3 instead of python in your system then use that instead
4) python app.py

## Usage:

1) Search
```
endpoint: apiUrl/search/<string:searchQuery>?provider=<providerName>
method:   GET
return:
```
```json
{
  "data": [
          {
            "link": "https://www.animefreak.tv/watch/overlord-ple-ple-pleiades-ova",
            "title": "Overlord: Ple Ple Pleiades (OVA)",
            "poster": "",
          },
          {
            "link": "https://www.animefreak.tv/watch/overlord-iii",
            "title": "Overlord III",
            "poster": "",
          },
          {
            "link": "https://www.animefreak.tv/watch/overlord",
            "title": "Overlord",
            "poster": "",
          }
      ],
  "message": "ok",
}
```

## Note:
Before installing make sure git is installed on your machine.
