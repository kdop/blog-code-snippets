#!/usr/bin/python

import datetime


def get_season_today(today: datetime) -> str:
    """
    Finds what the current season is based on today's date.
    :param today: Today's date.
    :return: The name of the season.
    """

    month = today.month

    if 3 <= month <= 5:
        return "spring"
    if 6 <= month <= 8:
        return "summer"
    if 9 <= month <= 11:
        return "autumn"

    return "winter"


def main():
    print(get_season_today(today=datetime.date.today()))


if __name__ == "__main__":
    main()
