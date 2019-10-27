from flask_mysqldb import MySQL
import json

def connectDB(app, host, port, user, password, dbName):
    app.config['MYSQL_HOST'] = host
    app.config['MYSQL_PORT'] = port
    app.config['MYSQL_USER'] = user
    app.config['MYSQL_PASSWORD'] = password
    app.config['MYSQL_DB'] = dbName
    return MySQL(app)

def executeQuery(mysqlDB, query, args=None):
    cur = mysqlDB.connection.cursor()
    cur.execute(query) if args == None else cur.execute(query, args)
    return cur.fetchall()

def sqlRowToJsonDict(rows, rowHeaders):
    jsonData = []
    for result in rows:
        jsonData.append(dict(zip(rowHeaders, result)))
    return jsonData