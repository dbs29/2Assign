import sqlite3 as lite
import csv
import re
import pandas as pd
import argparse
import collections
import json
import glob
import math
import os
import requests
import string
import sqlite3
import sys
import time
import xml


class Movie_db(object):
    def __init__(self, db_name):
        #db_name: "cs1656-public.db"
        self.con = lite.connect(db_name)
        self.cur = self.con.cursor()
    
    #q0 is an example 
    def q0(self):
        query = '''SELECT COUNT(*) FROM Actors'''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q1(self):
        query = '''
        SELECT fname, lname
        FROM Actors as a, Movies as m80, Movies as m2000, Cast as c80, Cast as c2000
        WHERE a.aid = c80.aid AND m80.mid = c80.mid AND m80.year BETWEEN 1980 AND 1990 AND a.aid = c2000.aid AND m2000.mid = c2000.mid AND m2000.year >= 2000
        ORDER BY lname ASC, fname ASC
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows
        

    def q2(self):
        query = '''
            SELECT m.title, m.year
            FROM Movies as m, (SELECT *
                                FROM Movies as rw WHERE rw.title = 'Rogue One: A Star Wars Story') as mRW
                                WHERE m.year = mRW.year AND m.rank > mRW.rank ORDER BY m.title ASC
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q3(self):
        query = '''
            SELECT fname, lname, mr.cred
            FROM Actors as act, (Select c.aid, count(role) as cred FROM Movies as m, Cast as c WHERE m.mid = c.mid AND m.title LIKE '%Star Wars%' GROUP BY c.aid Having cred >=1) mr
            WHERE act.aid = mr.aid
            ORDER By mr.cred DESC, act.lname ASC, act.fname ASC
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows


    def q4(self):
        query = '''
            SELECT DISTINCT a.fname, a.lname
            FROM Actors as act, Movies as movie, Cast as cast
            WHERE act.aid = cast.aid AND cast.mid = movie.mid AND movie.year < 1980 and act.aid NOT IN (SELECT cast.aid FROM Cast cast
                            WHERE cast.mid in (SELECT movie.mid FROM Movies movie WHERE movie.year >= 1980))
            ORDER BY lname ASC, fname ASC
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q5(self):
        query = '''
            SELECT d.fname, d.lname, count(*) as f
            FROM Movies as m, Movie_Director as md, Directors as d
            WHERE m.mid = md.mid AND md.did = d.did
            GROUP BY d.lname, d.fname
            ORDER BY f DESC, d.lname, d.fname
            LIMIT 10
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q6(self):
        query = '''
            SELECT m.title, count(DISTINCT c.aid) as number
            FROM Movies as m, Cast as c
            WHERE BY c.mid
            ORDER BY number DESC
            LIMIT 11
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q7(self):
        query = '''
            SELECT m.title, fm.gencnt, ma.gencnt
                FROM Movies as m, (SELECT c.mid, count(*) gencnt FROM cast as c, actors a WHERE c.aid = a.aid and a.gender = 'Female' 
                    GROUP BY c.mid) fm,
                    (SELECT c.mid, count(*) gencnt
                    FROM Cast as c, Actors a WHERE a.aid = c.aid AND a.gender = 'Male' Group BY c.mid) ma
                    WHERE m.mid = fm mid AND m.mid = ma.mid AND mf.gencnt > ma.gencnt
                    ORDER BY m.title
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q8(self):
        query = '''
            SELECT a.fname, a.lname, count(DISTINCT md.did) as cnt
            FROM Actors as a, Movie_Director as md, Cast as c
            WHERE a.aid = c.aid AND c.mid = md.mid AND a.aid != md.did
            GROUP BY a.fname, a.lname having count(DISTINCT md.did) >= 7
            ORDER BY cnt DESC
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows


    def q9(self):
        query = '''
            
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q10(self):
        query = '''
            
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q11(self):
        query = '''
            
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q12(self):
        query = '''
            
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

if __name__ == "__main__":
    task = Movie_db("cs1656-public.db")
    rows = task.q0()
    print(rows)
    print()
    rows = task.q1()
    print(rows)
    print()
    rows = task.q2()
    print(rows)
    print()
    rows = task.q3()
    print(rows)
    print()
    rows = task.q4()
    print(rows)
    print()
    rows = task.q5()
    print(rows)
    print()
    rows = task.q6()
    print(rows)
    print()
    rows = task.q7()
    print(rows)
    print()
    rows = task.q8()
    print(rows)
    print()
    rows = task.q9()
    print(rows)
    print()
    rows = task.q10()
    print(rows)
    print()
    rows = task.q11()
    print(rows)
    print()
    rows = task.q12()
    print(rows)
    print()
