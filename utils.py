from anime_downloader.sites import get_anime_class
from anime_downloader.sites.anime import AnimeEpisode


class DummyParent:
    def __init__(self):
        self.quality = '1080p'
        self.QUALITIES = ['1080p']
        self._fallback_qualities = []
        self.title = 'dummy title'


def SearchResult_to_json(SearchResult):
    data = {
        "link": SearchResult.url,
        "title": SearchResult.title,
        "poster": SearchResult.poster
    }
    if type(SearchResult.meta) != str:
        for meta in SearchResult.meta:
            if meta not in data:
                data[meta] = SearchResult.meta[meta]
    return data


def AnimeEpisode_to_json(AnimeEpisode):
    data = {
        "link": AnimeEpisode.url,
        "ep_no": AnimeEpisode.ep_no
    }
    return data


def get_episodes_using_provider(link, provider):
    provider = get_anime_class(provider)
    search = provider(link)
    return [AnimeEpisode_to_json(x) for x in search]


def get_episode(link, provider, parent):
    try:
        episode_class = AnimeEpisode.subclasses[provider]
        episode = episode_class(link, parent=DummyParent())
        return episode.source().stream_url
    except KeyError:
        provider_ = get_anime_class(provider)
        search = provider_(parent)
        print(search)
        episode_class = AnimeEpisode.subclasses[provider]
        episode = episode_class(link, parent=DummyParent())
        source = episode.source()
        return {
            "link": source.stream_url,
            "headers": {
                "referer": source.referer
            }
        }
