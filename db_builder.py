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
    createLeaderboad = "CREATE TABLE IF NOT EXISTS leaderboard (id INTEGER NOT NULL, username TEXT NOT NULL, totalWPM INTEGER NOT NULL, games INTEGER NOT NULL);"
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
    c.execute("INSERT INTO leaderboard VALUES (?,?, ?, ?)", (counter,username, 0, 0))
    db.commit()
    db.close()

def takeID(username):
    db=sqlite3.connect("data/accounts.db")
    c=db.cursor()
    c.execute("SELECT id, username FROM leaderboard;")
    tupleList =  c.fetchall()
    print tupleList
    for each in tupleList:
        if each[1] == username:
            return each[0]
    return -1;
    db.commit()
    db.close()

def takeWPM(tupleTemp):
    if tupleTemp[3] == 0:
        return 0
    else:
        return (tupleTemp[2]/tupleTemp[3])

def updateLeaderboard(username, wpm):
    db=sqlite3.connect("data/accounts.db")
    c=db.cursor()
    c.execute("SELECT totalWPM, games FROM leaderboard WHERE username = {}".format("'"+str(username)+"'"))
    tupleElement =  c.fetchone()
    print tupleElement[0] + wpm
    c.execute("UPDATE leaderboard set totalWPM = {0}, games = {1} WHERE username = {2}".format(tupleElement[0] + wpm, tupleElement[1] + 1, "'"+str(username)+"'"))
    
    
    c.execute("SELECT * FROM leaderboard;")
    newList = c.fetchall()

    #take another copu of old leaderboard
    c.execute("SELECT * FROM leaderboard;")
    boardList = c.fetchall()
    newList.sort(reverse = True, key=takeWPM)
    for oldEach in newList:
        each = newList[oldEach[0]-1]
        print "old", oldEach
        print "compare: ", each, " ", oldEach
        if each[1] != oldEach[1]:
            print "UPDATE leaderboard set username = {1}, totalWPM = {2}, games = {3} WHERE id = {0};".format(oldEach[0],"'"+str(each[1])+"'", each[2], each[3])
            c.execute("UPDATE leaderboard set username = {1}, totalWPM = {2}, games = {3} WHERE id = {0};".format(oldEach[0],"'"+str(each[1])+"'", each[2], each[3]))
    #c.execute("INSERT INTO leaderboard VALUES (?,?, ?)", (counter,username, wpm))
    db.commit()
    db.close()

def refreshLeaderboard():
    db=sqlite3.connect("data/accounts.db")
    c=db.cursor()
    c.execute("SELECT * FROM leaderboard;")
    newList = c.fetchall()

    #take another copu of old leaderboard
    c.execute("SELECT * FROM leaderboard;")
    boardList = c.fetchall()
    newList.sort(reverse = True, key=takeWPM)
    for oldEach in newList:
        each = newList[oldEach[0]-1]
        print "old", oldEach
        print "compare: ", each, " ", oldEach
        if each[1] != oldEach[1]:
            print "UPDATE leaderboard set username = {1}, totalWPM = {2}, games = {3} WHERE id = {0};".format(oldEach[0],"'"+str(each[1])+"'", each[2], each[3])
            c.execute("UPDATE leaderboard set username = {1}, totalWPM = {2}, games = {3} WHERE id = {0};".format(oldEach[0],"'"+str(each[1])+"'", each[2], each[3]))
    #print "LISTS:", tupleList, boardList
    #for each in tupleList:
    #    oldTuple = tupleList[each[0] - 1]
    #    print "newTuple: ", each
    #    print "compare new to old: ", each,oldTuple, (each[1] != oldTuple[1])
    #    if each[1] != oldTuple[1]:
    #        print "diffence: ", each[0], oldTuple[0]
    #        c.execute("UPDATE leaderboard SET id = {0}, username = {1}, wpm = {2} WHERE id = {3}, username = {1};".format(each[0],"'"+str(each[1])+"'", each[2], oldTuple[0]))
    #        test = c.fetchall()
    #        c.execute("SELECT * FROM leaderboard")
    #        test = c.fetchall()
    #        print test
    #        #c.execute("REPLACE INTO leaderboard (id, username, wpm) VALUES (?,?,?);", (oldTuple[0],each[1], each[2]))
    
    #print tupleList
    #c.execute("SELECT * FROM leaderboard;")
    #test = c.fetchall()
    #print test
    db.commit()
    db.close()