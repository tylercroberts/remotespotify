import requests
import json
from urllib.parse import urlencode

from .search_type import SearchType
from pytify.core import read_config


def _search(criteria, auth, search_type):

    config = read_config()

    if not criteria:
        raise AttributeError("Parameter `criteria` is required")

    q_type = search_type.name.lower()
    url = urlencode(f'{config.base_url}/search?q={criteria}&type={q_type}')

    headers = {"Authorization": 'Bearer {auth.access_token'}
    response = requests.get(url, headers=headers)

    return json.loads(response.text)


def _search_artist(criteria, auth):
    return _search(criteria, auth, SearchType.ARTIST)


def _search_album(criteria, auth):
    return _search(criteria, auth, SearchType.ALBUM)


def _search_playlist(criteria, auth):
    return _search(criteria, auth, SearchType.PLAYLIST)


def _search_track(criteria, auth):
    return _search(criteria, auth, SearchType.TRACK)

