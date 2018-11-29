# !!!! Incomplete

import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd=" <insert your pw> ",  # your password
                     db="CommunicationSeminarDjango")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

tagset = open("Claws5_tagset.txt","r")
while True:
    line = tagset.readline()
    if not line:
        break

    if line:
        tag = str(line[:3])
        description = str(line[4:])
        print(tag, description)
        statement = "INSERT INTO ComSemApp_tag (tag, type, description) VALUES (%s, %s, %s)"
        # statement += line[0] + "\", \"" + line[0] + "\", \"" + " ".join(line[1:]) + "\")"
        cur.execute(statement,[tag, tag, description])
        # print(statement)
db.commit()
db.close()
