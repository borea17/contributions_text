from email.utils import formatdate
from datetime import timedelta as td


def convert_words_to_dates(word, start_datetime):
    all_dates = []
    for letter in word:
        if letter == " ":
            start_datetime = start_datetime + td(4 * 7)
        else:
            all_dates.extend(convert_letter_to_dates(letter, start_datetime))
            if letter in ["W"]:
                start_datetime = start_datetime + td(6 * 7)
            else:
                start_datetime = start_datetime + td(4 * 7)
    return all_dates


def convert_letter_to_dates(letter, start_datetime):
    all_dates = [start_datetime]
    if letter == "H":
        # vertical line left
        all_dates.extend([start_datetime + td(days) for days in range(1, 5)])
        # vertical line right
        all_dates.extend([start_datetime + td(14 + days) for days in range(0, 5)])
        # horizontal point
        all_dates.extend([start_datetime + td(9)])
    elif letter == "E":
        # vertical line
        all_dates.extend([start_datetime + td(days) for days in range(1, 5)])
        # horizontal lines
        all_dates.extend([start_datetime + td(7 * days) for days in range(1, 3)])
        all_dates.extend([start_datetime + td(2 + 7 * days) for days in range(1, 3)])
        all_dates.extend([start_datetime + td(4 + 7 * days) for days in range(1, 3)])
    elif letter == "L":
        # vertical line
        all_dates.extend([start_datetime + td(days) for days in range(1, 5)])
        # horizontal line
        all_dates.extend([start_datetime + td(4 + 7 * days) for days in range(1, 3)])
    elif letter == "O":
        # vertical lines
        all_dates.extend([start_datetime + td(days) for days in range(1, 5)])
        all_dates.extend([start_datetime + td(14 + days) for days in range(0, 5)])
        # horizontal
        all_dates.extend([start_datetime + td(7)])
        all_dates.extend([start_datetime + td(4 + 7)])
    elif letter == "W":
        # vertical lines
        all_dates.extend([start_datetime + td(days) for days in range(1, 5)])
        all_dates.extend([start_datetime + td(14 + days) for days in range(0, 5)])
        all_dates.extend([start_datetime + td(28 + days) for days in range(0, 5)])
        # horizontal points
        all_dates.extend([start_datetime + td(4 + 7)])
        all_dates.extend([start_datetime + td(4 + 21)])
    elif letter == "R":
        # vertical lines
        all_dates.extend([start_datetime + td(days) for days in range(1, 5)])
        all_dates.extend([start_datetime + td(14 + days) for days in [1, 3, 4]])
        # horizontal points
        all_dates.extend([start_datetime + td(7)])
        all_dates.extend([start_datetime + td(2 + 7)])
    elif letter == "D":
        # vertical lines
        all_dates.extend([start_datetime + td(days) for days in range(1, 5)])
        all_dates.extend([start_datetime + td(14 + days) for days in [1, 2, 3, 4]])
        # horizontal points
        all_dates.extend([start_datetime + td(7)])
        all_dates.extend([start_datetime + td(4 + 7)])
    # sort dates
    all_dates.sort()
    # convert into rfc 2822
    out_dates_rfc = [formatdate(float(date.strftime("%s"))) for date in all_dates]
    return out_dates_rfc
