import os
import psycopg2
from postgres_db import postgres_init
from dotenv import load_dotenv

def insert_atemp(atemp):
    """
    Create a new entry into the ATemp table:
    :param atemp(ambient temperature, and datetime):
    :return: id
    """
    try:
        conn = postgres_init.connect()
        sql = ('insert into ATemp(id,atemp,location,date) values(DEFAULT, %s,%s,%s)')
        cur = conn.cursor()
        cur.execute(sql, atemp)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_humidity(hum):
    """
    Create a new entry into the Humidity table:
    :param hum(ambient humidity, and datetime):
    :return: id
    """
    try:
        conn = postgres_init.connect()
        sql = ('insert into Humidity(id,hum,location,date) values(DEFAULT, %s,%s,%s)')
        cur = conn.cursor()
        cur.execute(sql, hum)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_ltemp(ltemp):
    """
    Create a new entry into the LTemp table:
    :param ltemp(liquid temperature, and datetime):
    :return: id
    """
    try:
        conn = postgres_init.connect()
        sql = ('insert into LTemp(id,ltemp,location,date) values(DEFAULT, %s,%s,%s)')
        cur = conn.cursor()
        cur.execute(sql, ltemp)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_ec(ec):
    """
    Create a new entry into the EC table:
    :param ec(ec, and datetime):
    :return: id
    """
    try:
        conn = postgres_init.connect()
        sql = ('insert into EC(id,ec,location,date) values(DEFAULT, %s,%s,%s)')
        cur = conn.cursor()
        cur.execute(sql, ec)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_sunhours(sunhours):
    """
        (   date             TEXT PRIMARY KEY NOT NULL,
            sunrise           REAL NOT NULL,
            sunset            REAL NOT NULL,
            solarnoon         REAL NOT NULL,
            daylength         TEXT NOT NULL);'''
        )
    """
    try:
        conn = postgres_init.connect()
        sql = ('insert into sunhours(date,sunrise,sunset,solarnoon,daylength) values(%s,%s,%s,%s,%s)')
        cur = conn.cursor()
        cur.execute(sql, sunhours)
        conn.commit()
        count = cur.rowcount
        print (count, "Record inserted successfully into SunHours table")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

def insert_ph(ph):
    """
    Create a new entry into the PH table:
    :param ph(ph, and datetime):
    :return: id
    """
    try:
        conn = postgres_init.connect()
        sql = ('insert into PH(id,ph,location,date) values(DEFAULT, %s,%s,%s)')
        cur = conn.cursor()
        cur.execute(sql, ph)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_openweather(weather):
    """
         id SERIAL PRIMARY KEY,
        descrip TEXT,
        mdescrip TEXT,
        feels_like REAL,
        humidity REAL,
        pressure REAL,
        temperature REAL,
        temp_max REAL,
        temp_min REAL,
        winddeg REAL,
        windspeed REAL,
        clouds REAL,
        dt BIGINT
    """
    try:
        conn = postgres_init.connect()
        sql = ('insert into openweather(id,descrip,mdescrip,feels_like,humidity,pressure,temperature,temp_max,temp_min,winddeg,windspeed,clouds,dt) values(DEFAULT, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
        cur = conn.cursor()
        cur.execute(sql, weather)
        conn.commit()
        count = cur.rowcount
        print (count, "Record inserted successfully into OpenWeather table")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

def select_all_hum():
    try:
        conn = postgres_init.connect()
        sql = ("""select * from Humidity""")
        cur = conn.cursor()
        cur.execute(sql)
        humidity = cur.fetchall() 
        cur.close()
        conn.commit()
        return humidity
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def select_all_ec():
    try:
        conn = postgres_init.connect()
        sql = ("""select * from EC""")
        cur = conn.cursor()
        cur.execute(sql)
        ec = cur.fetchall() 
        cur.close()
        conn.commit()
        return ec
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def select_all_atemp():
    try:
        conn = postgres_init.connect()
        sql = ("""select * from ATemp""")
        cur = conn.cursor()
        cur.execute(sql)
        atemp = cur.fetchall() 
        cur.close()
        conn.commit()
        return atemp
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def select_all_ltemp():
    try:
        conn = postgres_init.connect()
        sql = ("""select * from LTemp""")
        cur = conn.cursor()
        cur.execute(sql)
        ltemp = cur.fetchall() 
        cur.close()
        conn.commit()
        return ltemp
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def select_all_ph():
    try:
        conn = postgres_init.connect()
        sql = ("""select * from PH""")
        cur = conn.cursor()
        cur.execute(sql)
        ph = cur.fetchall() 
        cur.close()
        conn.commit()
        return ph
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def clear_humidity_table():
    try:
        conn = postgres_init.connect()
        sql = ('TRUNCATE Humidity; DELETE FROM Humidity;')
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()