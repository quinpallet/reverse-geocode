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
