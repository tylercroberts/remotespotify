import requests
import json
from urllib.parse import quote

from .search_type import SearchType
from pytify.core import read_config, logging_wrapper


def _search(criteria, auth, search_type):
    logger = logging_wrapper(2, "logs/test.log")
    logger.info("Criteria is: {}".format(criteria))

    config = read_config()

    if not criteria:
        raise AttributeError("Parameter `criteria` is required")

    q_type = search_type.name.lower()
    url = quote(f'{config.base_url}/search?q={criteria}&type={q_type}', safe="/:?&=")
    logger.info("URL to request: {}".format(url))

    headers = {"Authorization": f'Bearer {auth.access_token}'}
    response = requests.get(url, headers=headers)

    # if response['error']:
    #     #     logger.warning("{}".format(response['Error']))

    return json.loads(response.text)


def search_artist(criteria, auth):
    return _search(criteria, auth, SearchType.ARTIST)


def search_album(criteria, auth):
    return _search(criteria, auth, SearchType.ALBUM)


def search_playlist(criteria, auth):
    return _search(criteria, auth, SearchType.PLAYLIST)


def search_track(criteria, auth):
    return _search(criteria, auth, SearchType.TRACK)

