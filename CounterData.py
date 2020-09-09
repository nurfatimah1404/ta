import sqlite3
from datetime import datetime
import os
import logging


def counterDir():
    directory = "./db"
    if not os.path.exists(directory):
        os.makedirs(directory)


def upReceived():
    counterDir()
    now = datetime.now()
    nowString = datetime.strftime(now, "%Y-%m-%d")

    conn = sqlite3.connect(
        './db/counter.db')
    cursor = conn.cursor()
    # Create table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS counter (time text NULL, received BIGINT NULL, blocked BIGINT NULL)")
    cursor.execute(
        'SELECT * FROM counter WHERE time="{}"'.format(nowString))
    row = cursor.fetchone()
    if row is None:
        # update
        cursor.execute(
            "INSERT INTO counter values ('{}', 1, 0)".format(nowString))
    else:
        cursor.execute(
            "UPDATE counter SET received = received+1 WHERE time='{}'".format(nowString))
    conn.commit()
    conn.close()


def upBlocked():
    counterDir
    now = datetime.now()
    nowString = datetime.strftime(now, "%Y-%m-%d")

    conn = sqlite3.connect(
        './db/counter.db')
    cursor = conn.cursor()
    # Create table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS counter (time text NULL, received BIGINT NULL, blocked BIGINT NULL, sent BIGINT NULL)")
    cursor.execute(
        'SELECT * FROM counter WHERE time="{}"'.format(nowString))
    row = cursor.fetchone()
    if row is None:
        # update
        cursor.execute(
            "INSERT INTO counter values ('{}', 0, 1, 0)".format(nowString))
    else:
        cursor.execute(
            "UPDATE counter SET blocked = blocked+1 WHERE time='{}'".format(nowString))
    conn.commit()
    conn.close()


def clearCounter(date=None):
    if os.path.exists('./db/counter.db'):
        if date is None:
            now = datetime.now()
            date = datetime.strftime(now, "%Y-%m-%d")
            conn = sqlite3.connect(
                './db/counter.db')
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE counter SET received = 0, blocked = 0, WHERE time='{}'".format(date))
            conn.commit()
            conn.close()
        else:
            conn = sqlite3.connect(
                './db/counter.db')
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE counter SET received = 0, blocked = 0, WHERE time='{}'".format(date))
            conn.commit()
            conn.close()


def getCounter(date=None):
    if date is None:
        now = datetime.now()
        date = datetime.strftime(now, "%Y-%m-%d")
    if os.path.exists('./db/counter.db'):
        conn = sqlite3.connect('./db/counter.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM counter WHERE time='{}'".format(date))
        row = cursor.fetchone()
        if row is None:
            return {
                'time': date,
                'received': 0,
                'blocked': 0
            }
        else:
            return {
                'time': row[0],
                'received': row[1],
                'blocked': row[2]
            }
        conn.close()
    else:
        return {
            'time': date,
            'received': 0,
            'blocked': 0
        }
