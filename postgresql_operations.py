#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import psycopg2

"""
TABLE public.student
(
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    subjects character(4) NOT NULL,
    PRIMARY KEY (id)
)
"""

class PostgreSQLAdapter(object):
    def __init__(self):
        self.database = 'test'
        self.user = 'postgres'
        self.password = 'your password'
        self.host = '127.0.0.1'
        self.port = '5432'

    def __create_connection(self):
        return psycopg2.connect(database = self.database, user = self.user, password = self.password)

    def execute_non_query(self, sql):
        with self.__create_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()

    def query(self, sql):
        with self.__create_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

if __name__ == '__main__':
    
    database = PostgreSQLAdapter()
    rows = database.query("SELECT id, name, subjects FROM public.student")
    for row in rows:
        print('ID = {0}, Name = {1}, Subjects = {2}'.format(row[0], row[1], row[2]))