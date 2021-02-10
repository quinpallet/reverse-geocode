# reverse-geocode

Address acquisition class by reverse geocoding using the [OpenStreetMap Nominatim API](https://wiki.openstreetmap.org/wiki/Nominatim)

## Requirements

- None

## Prerequisites

- Python >= 3.7

## Usage

sample code ([main.py](main.py))

``` python
from q_geocode import ReverseGeocode


def main():
    TYO_COORDINATES = (35.68944, 139.69167)  # Location of 東京都庁
    YOK_COORDINATES = (35.4503658, 139.6336805)  # Location of 横浜市市庁舎
    YLM_COORDINATES = (35.4548814, 139.6311911)  # Location of 横浜ランドマークタワー

    print(ReverseGeocode(TYO_COORDINATES).get_address())
    print(ReverseGeocode(YOK_COORDINATES).get_address())
    print(ReverseGeocode(YLM_COORDINATES).get_address())

if __name__ == '__main__':
    main()

```

```sh
$ python main.py 
東京都庁
横浜市市庁舎
神奈川県横浜市西区みなとみらい二丁目
$ 
```

## License

&copy; 2021 [Ken Kurosaki](https://github.com/quinpallet).<br>
This project is [MIT](https://github.com/quinpallet/reverse-geocode/blob/master/LICENSE) licensed.
