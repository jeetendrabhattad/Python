#!/usr/bin/python

import MySQLdb as mdb
import sys
con = None
try:
    con = mdb.connect('localhost', 'testuser', 'test123', 'testdb');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Database values : ", ver
   
    cur.execute("create table if not exists employee (eid int primary key , ename varchar(25), age int)");
    cur.execute("insert into employee values(1, \"Chetan\", 25)")

    cur.execute("SELECT * from employee")
    ver = cur.fetchall()
    print "Database values : ", ver

    cur.execute("update employee set ename=\"Vinod\" where eid=1")
    cur.execute("SELECT * from employee")
    ver = cur.fetchall()
    print "After Update Database values : ", ver

    cur.execute("insert into employee values(6,\"Chetan\", 25)")
    cur.execute("SELECT * from employee")
    ver = cur.fetchall()
    print "After Insert Database values : ", ver
    con.commit()
    
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
finally:           
    if con:    
        con.close()
