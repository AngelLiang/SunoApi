from typing import List
from urllib3.util import Retry
from requests import Request, Session, Response
import requests

if __name__ == '__main__':
    import schemas
else:
    from suno_client import schemas

class SunoClientError(Exception):
    pass


class SunoClient:

    def __init__(self, timeout=10) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            'Connection': 'close',
            # 'Authorization': f'{self.token}'
        }
        self.base_url: str = 'https://studio-api.suno.ai'
        self.timeout: int = timeout
        self.proxies = {}

    def do_request(self, method, url, params=None, json=None, headers=None, files=None):
        if headers:
            self.headers.update(headers)
        req = Request(method=method, url=url, params=params,
                      json=json, headers=self.headers, files=files)
        prepared = req.prepare()
        # pretty_print_POST(prepared)
        try:
            s = Session()
            if self.proxies:
                s.proxies.update(self.proxies)
            # s.mount('http://', HTTPAdapter(max_retries=self.retries))
            return s.send(prepared, timeout=self.timeout)
        except requests.exceptions.ReadTimeout as err:
            raise SunoClientError(err)
        except requests.exceptions.ConnectionError as err:
            raise SunoClientError(err)

    def do_get(self, url, params=None, headers=None) -> Response:
        return self.do_request('get', url, params=params, headers=headers)

    def do_post(self, url, params=None, json=None, headers=None) -> Response:
        return self.do_request('post', url, params=params, json=json, headers=headers)

    def join_url(self, path) -> str:
        return self.base_url + path

    def handle_response(self, resp: Response) -> dict:
        resp_json = resp.json()
        if 'detail' in resp_json:
            raise SunoClientError(resp_json['detail'])
        return resp_json

    def get_feed(self, token:str) -> schemas.Feed:
        """获取创建歌曲列表"""
        url = 'https://studio-api.suno.ai/api/feed/v2?add_preset_clips=true'
        resp = self.do_get(url,headers={'Authorization': f'Bearer {token}'})
        resp_json = self.handle_response(resp)
        return schemas.Feed.parse_obj(resp_json)


client = SunoClient()

if __name__ == '__main__':
    data = client.get_feed('')
    print(data)
