"""Файл базы данных."""
import psycopg2
from psycopg2 import sql

from src.config import settings


class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=settings.db_host,
                port=settings.db_port,
                dbname=settings.db_name,
                user=settings.db_user,
                password=settings.db_pass,
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database")
        except (Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database:", error)

    def execute_script(self, script_path: str):
        try:
            with open(script_path, "r", encoding="utf-8") as script_file:
                query = sql.SQL(script_file.read())
                self.cursor.execute(query)
            self.conn.commit()
            print("Script executed successfully")

        except (Exception, psycopg2.Error) as error:
            print("Error executing script:", error)

    def execute_query(self, query: str, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            print("Query executed successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error executing query:", error)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def check_data_exists(self, table_name, column_name, column_value):
        try:
            query = sql.SQL(
                "SELECT EXISTS(SELECT 1 FROM {} WHERE {} = %s LIMIT 1)"
            ).format(sql.Identifier(table_name), sql.Identifier(column_name))
            self.cursor.execute(query, (column_value,))
            result = self.cursor.fetchone()
            return result[0]
        except (Exception, psycopg2.Error) as error:
            print("Error checking data existence:", error)

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Disconnected from the database")
