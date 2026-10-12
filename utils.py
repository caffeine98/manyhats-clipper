import re

def parse_time(elapsed_time: str) -> int:
    # Convert _h_m_s into seconds. For example, converts 13m51s to 831 seconds or 2h11m4s to 7,864 seconds
    hours, minutes, seconds = 0, 0, 0

    m = re.fullmatch(r"(?:(?P<hours>\d+)h)?(?:(?P<minutes>\d+)m)?(?:(?P<seconds>\d+)s?)?", elapsed_time.lower())
    if not elapsed_time or m is None:
        raise ValueError("Pattern matching failed")

    hours   = int(m.group("hours")) if m.group("hours") is not None else 0
    minutes = int(m.group("minutes")) if m.group("minutes") is not None else 0
    seconds = int(m.group("seconds")) if m.group("seconds") is not None else 0

    return (hours * 3600) + (minutes * 60) + seconds


def _test_parse_time():
    valid = [
    ("13m51s",  831),
    ("2h11m4s", 7864),
    ("2h1m3s",  7263),
    ("51s",     51),
    ("51",      51),     # no unit means seconds
    ("2m13",    133),    # trailing s is optional
    ("2m13s",   133),
    ("2h4s",    7204),   # no minutes
    ("2h",      7200),   # hours only
    ("13m",     780),    # minutes only
    ("2h11m",   7860),   # no seconds
    ("90m",     5400),   # minutes over 59 are allowed
    ("0s",      0),
    ("2H1M3S",  7263),
    ]

    invalid = [
        "",         # nothing at all
        "abc",
        "13x",      # unknown unit
        "4s2h",     # wrong order
        "5m2h",     # wrong order
        "s",        # unit with no number
        "h",
        "13m51ss",  # doubled s
        "1.5s",     # decimals aren't supported by this pattern
        "-5s",
        " 5s",      # stray whitespace
    ]

    for text, expected in valid:
        result = parse_time(text)
        print("PASS" if result == expected else "FAIL", repr(text), result, expected)

    for text in invalid:
        try:
            result = parse_time(text)
            print("FAIL", repr(text), "returned", result)
        except ValueError:
            print("PASS", repr(text))

#print(parse_time("2h3m1s"))

#_test_parse_time()