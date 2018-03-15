import mysql.connector
import configparser
import pprint
import json
import pprint
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


config = configparser.ConfigParser()
config.read('../config/config.ini')


def connectMysql(user,password,host,database):
    config = {
      'user': user,
      'password': password,
      'database': database,
      'host': host,
      'raise_on_warnings': True,
    }
    # print(config)
    cnx = mysql.connector.connect(**config)
    return cnx

def getMysqlData(cnx,query,data=''):
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query, data)
    row = cursor.fetchall()
    return row
    # return cursor

def insertMysql(cnx,query,data=''):
    cursor = cnx.cursor()
    try:
        cursor.execute(query, data)
    except mysql.connector.IntegrityError as err:
        # print("Error: {}".format(err))
        errorMsg = "insertMysql Error: {}".format(err)
        return errorMsg
        # pass
    cnx.commit()
    return data


lab_server_section = config['LAB_DB']
lab_server = lab_server_section['LAB_SERVER']
lab_user = lab_server_section['LAB_USER']
lab_password = lab_server_section['LAB_PASSWORD']
lab_database = lab_server_section['LAB_DATABASE_NAME']
lab_cur_mysql = connectMSsql(lab_server,lab_user,lab_password,lab_database)

