#!/usr/bin/env python3
""" module diocumntation """
from typing import List
import logging
import mysql.connector
import re
import os


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """documentation"""
    for field in fields:
        regex = f"{field}=[^{separator}]*"
        message = re.sub(regex, f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """documntation style"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """documntation style"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """documntation style"""
        org = super().format(record)
        return filter_datum(self.fields, self.REDACTION, org, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """documentation style"""
    logr = logging.getLogger("user_data")
    logr.setLevel(logging.INFO)
    logr.propagate = False
    shnd = logging.StreamHandler()
    shnd.setFormatter(RedactingFormatter(PII_FIELDS))
    logr.addHandler(sh)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """documntation style"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username, password=password, host=host, database=db_name
    )


def main() -> None:
    """documnetation style"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logr = get_logger()
    for row in cursor:
        data = []
        for desc, value in zip(cursor.description, row):
            pair = f"{desc[0]}={str(value)}"
            data.append(pair)
        row_str = "; ".join(data)
        log.info(row_str)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
