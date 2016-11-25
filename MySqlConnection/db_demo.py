#!/usr/bin/python

import MySQLdb as mdb
import sys
con = None
try:
    con = mdb.connect('localhost', 'jeetu', '12345', 'testdb');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Database values : ", ver
   
    cur.execute("create table if not exists employee_stellus (eid int primary key , ename varchar(25), age int)");
    cur.execute("insert into employee_stellus values(1, \"Chetan\", 25)")

    cur.execute("SELECT * from employee_stellus")
    ver = cur.fetchall()
    print "Database values : ", ver

    cur.execute("update employee_stellus set ename=\"Vinod\" where eid=1")
    cur.execute("SELECT * from employee_stellus")
    ver = cur.fetchall()
    print "After Update Database values : ", ver

    cur.execute("insert into employee_stellus values(6,\"Chetan\", 25)")
    cur.execute("insert into employee_stellus values(2,\"Vishwa\", 32)")
    cur.execute("SELECT * from employee_stellus")
    ver = cur.fetchall()
    print "After Insert Database values : ", ver
    con.commit()
    
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
finally:           
    if con:    
        con.close()
