import base64


def encode(s: str):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')


def decode(s: str):
    return base64.b64decode(s.encode('utf-8')).decode('utf-8')


if __name__ == "__main__":
    s = "PYIIIIIIIIIIIIIIII7QZjAXP0A0AkAAQ2AB2BB0BBABXP8ABuJIYIhkmKzyCDq4l4FQyBlrRWEahI1tLKT16Pnk1ftLnkPvwlnkW6fhNkan5pNkgF6XPOR8T5HsCivaN19okQSPlKRLvD6DNk3uelNkpTthRXuQ9znk2jEHLK1Ja0FaXkhcTtBink4tlKUQhnvQYotqo0ylnLMTO0SDEWZahOtMwqhG8kXteksLwTdh1e8aLKsja4uQ8kavLKdLrklK0ZeL7qjKLKUTLKuQM8k9bdvDeL1qiSnR5XVIXTOyjENikrphNnrnVnhlBrzHooKOYoyok93u7tOKCNyHzBBSnguLgTcbyxlNKOYoYoMYaUTHphRL2LupQQ0htsFRTn541x3E2Se5T26PyKK8QLTddJlIZFBvyoSeUTLIkrv0oKy8ORpMmlk7Gl6DBrm8SoyoioyoaxrOqh0XwP1xu1Qw1upBbHrmrED3T34qiKOxQLTdEZOyZCaxQmRxgPUp0hpnPn4srRe8BDSo2PT7axqOCWROpophSYpnSo04u83K72Peu70hBpCsqDpF4qHIMXpLQ429k98aEaJr1BF3Ca3bIozp01IPf0Yof5GxAA"
    print(decode(a))
