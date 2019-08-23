import peewee
from peewee import *

db = MySQLDatabase('geek_time', user='root')


class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db
        db_table = 'price'


def test_peewee():
    Price.create_table()
    price = Price.create(timestamp='2019-06-07 13:17:18', BTCUSD='12345.67')
    price.save()
    print('price saved!')


if __name__ == "__main__":
    test_peewee()
