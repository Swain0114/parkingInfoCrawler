import mysql.connector
import configparser
import pprint
import json
import pprint
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


config = configparser.ConfigParser()
config.read('/Users/swain/Desktop/software_engineering/database/config.ini')

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


gcp_server = "35.188.183.43"
gcp_user = root
gcp_password = ""
gcp_database = ParkingInfo
#local_user,local_password,local_server,local_database
gcp_cur_mysql = connectMysql(gcp_user,gcp_password,gcp_server,gcp_database) 
