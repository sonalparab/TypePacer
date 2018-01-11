import sqlite3, hashlib   #enable control of an sqlite database


def encrypt(password):
    encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass

def createTables():
    db=sqlite3.connect("data/accounts.db")
    c=db.cursor()

    c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='accounts';")
    bol = c.fetchone()
    counter = 0
    if bol == 0:
        counter = 1
    if bol == 1:
        c.execute("SELECT COUNT(id) FROM accounts;")
        counter = c.fetchone()
        counter = int(counter[0]) + 1

    createAccount = "CREATE TABLE IF NOT EXISTS accounts (id INTEGER NOT NULL, username TEXT NOT NULL, pass TEXT NOT NULL);"
    createLeaderboad = "CREATE TABLE IF NOT EXISTS leaderboard (id INTEGER NOT NULL, username TEXT NOT NULL, wpm INTEGER NOT NULL);"
    c.execute(createAccount)
    c.execute(createLeaderboad)
    #print "INSERT INTO accounts VALUES (?,?,?)", (counter,'test',encrypted)
    
    #dummy execution 
    #c.execute("INSERT INTO accounts VALUES (?,?,?)", (counter,'test',encrypt('dummyPass')))
    db.commit()
    db.close()

#create dict of usernames and passwords
def user_dict():
    db=sqlite3.connect("data/accounts.db")
    c=db.cursor()
    users = {} #{username: password}
    user_data = c.execute("SELECT * FROM accounts;")
    for data in user_data:
        users[data[1]] = data[2]
    db.commit()
    db.close()
    return users

#create dict of edit history
def leaderboard_dict():
    db=sqlite3.connect("data/accounts.db")
    c=db.cursor()
    leaderboard = {} #{id: {username: contribution}}
    leaderboard_data = c.execute("SELECT * FROM leaderboard;")
    for data in leaderboard_data:
        leaderboard[data[1]] = data[2]
    db.commit()
    db.close()
    return leaderboard

def insertAccount(username, password):
    db=sqlite3.connect("data/accounts.db")
    c=db.cursor()
    c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='accounts';")
    bol = c.fetchone()[0]
    counter = 0
    if bol == 0:
        counter = 1
    if bol == 1:
        c.execute("SELECT COUNT(id) FROM accounts;")
        counter = c.fetchone()
        counter = int(counter[0]) + 1
    c.execute("INSERT INTO accounts VALUES (?,?, ?)", (counter,username, encrypt(password)))
    db.commit()
    db.close()

def updateLeaderboard(username,wpm):
    db=sqlite3.connect("data/accounts.db")
    c=db.cursor()
    c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='leaderboard';")
    bol = c.fetchone()
    counter = 0
    if bol == 0:
        counter = 1
    if bol == 1:
        c.execute("SELECT COUNT(id) FROM leaderboard;")
        counter = c.fetchone()
        counter = int(counter[0]) + 1
    c.execute("INSERT INTO leaderboard VALUES (?,?, ?)", (counter,username, wpm))
    db.commit()
    db.close()