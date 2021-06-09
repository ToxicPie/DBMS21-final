import requests


API_BASE_URL = 'https://api.hypixel.net/'


class HypixelAPIError(Exception):
    pass


def fetch_api(path, params={}, tries=1):
    for i in range(tries):
        try:
            request = requests.get(API_BASE_URL + path, params=params)
            request.raise_for_status()
            result = request.json()
            if not result['success']:
                error = result['cause']
                raise HypixelAPIError('API does not return success: ' + error)
        except Exception as ex:
            if i == tries - 1: raise ex
        else:
            return result
