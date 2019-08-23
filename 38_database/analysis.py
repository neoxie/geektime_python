import MySQLdb
import numpy as np


def test_pymysql():
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user='root',
                           db='geek_time')

    cur = conn.cursor()
    cur.execute('''
            SELECT
              BTCUSD
            FROM
              price
            WHERE
              timestamp > now() - interval 60 minute
    ''')

    BTCUSD = np.array(cur.fetchall())
    print(BTCUSD.max(), BTCUSD.min())

    conn.close()
