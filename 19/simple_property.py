from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, name, time):
        self.time = time
        self.name = name

    @property
    def expired(self):
        return NOW > self.time


if __name__ == '__main__':
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    print(twitter_promo.expired)

    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newsletter', future_date)
    print(newsletter_promo.expired)
