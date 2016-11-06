#!/usr/bin/env python2.7

from MySQLdb.connections import Connection
from MySQLdb import cursors
import MySQLdb

host = "localhost"
user = "root"
passwd = "django@123"
database = "universal" 
con = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database)

cur = con.cursor()
print (cur)
