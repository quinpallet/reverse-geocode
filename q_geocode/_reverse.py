import urllib.request
import json
from typing import Union


class ReverseGeocode:
    def __init__(self, location: tuple):
        self.__location: tuple = location
        self.__lat: float = location[0]
        self.__lng: float = location[1]
        self.__payload: dict = {
            'format': 'json',
            'lat': location[0],
            'lon': location[1],
            'zoom': 18,
            'addressdetails': 1
        }
        self.__endpoint: str = 'https://nominatim.openstreetmap.org/reverse'
        self.__resdata: dict = self.__req()
        self.__display_name: str = self.__resdata.get('display_name')
        self.__address: dict = self.__resdata.get('address')

    def __req(self) -> dict:
        params: str = urllib.parse.urlencode(self.__payload)
        with urllib.request.urlopen(f'{self.__endpoint}?{params}') as res:
            return json.loads(res.read().decode('utf-8'))

    def get_url(self) -> str:
        params: str = urllib.parse.urlencode(self.__payload)
        return f'{self.__endpoint}?{params}'

    def get_data(self, key) -> Union[dict, str, float, int]:
        return self.__resdata[key]

    # 日本用データ構成から住所を取得
    def get_jp_address(self) -> str:
        # ランドマーク名が存在すれば名称を返す
        amenity_name: dict = self.__address.get('amenity')
        if amenity_name:
            return amenity_name

        # display_nameから住所を再構成
        display_name_list: list = self.__display_name.split(', ')[::-1]
        return ''.join(display_name_list[2:6])  # province, city, suburb, hamlet/neighbourhood

    def get_address(self) -> str:
        display_name_list: list = self.__display_name.split(', ')[::-1]
        addr: str = ' '.join(display_name_list)
        if self.__address['country_code'] == 'jp':
            return self.get_jp_address()
        return addr

    @property
    def endpoint(self) -> str:
        return self.__endpoint

    @property
    def payload(self) -> dict:
        return self.__payload

    @property
    def lat(self) -> float:
        return self.__lat

    @property
    def lng(self) -> float:
        return self.__lng

    @property
    def resdata(self) -> dict:
        return self.__resdata

    @property
    def display_name(self) -> str:
        return self.__display_name

    @property
    def address(self) -> dict:
        return self.__address
