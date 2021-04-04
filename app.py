from flask import Flask,request
from SqlStuff import Users
from random import randint
import json

# creating a server to run in main
app=Flask(__name__)

# saving every id so there wouldnt be any duplicates

# generating an id for a new user
def generateRandomId():
    userT=Users()
    IdArr=userT.Get_Every_Id()
    while True:
        value = randint(100000000, 999999999)
        Exist=False
        # checking that the doesnt exist already
        for localId in IdArr:
            if localId==value:
                Exist=True
        # if it passes the check without trigering the flag then its new
        if Exist==False:
            return value

# a fun that creates a table is there isnt one
@app.route('/CreatTable', methods=['GET'])
def CreatTable():
    print("got req!!!!!!!!!!!! am here")
    userT=Users()
    # Num, AccountName, Password, Email, PhoneNumber,Id
    return "Created Table"
    
# conferming that the user has the right name of password
@app.route('/confirm', methods=['POST','GET'])
def write():
    userT=Users()
    username = request.args.get('username')
    password = request.args.get('password')
    userData=userT.Select_by_AccountName(username)
    if (userData==None):
        return "name not found"
    if (userData[2]==password):
        # sending id as an answer
        return str(userData[5])
    return "wrong password"

# registering a new user into the table
@app.route('/register', methods=['POST','GET'])
def addUser():
    userT=Users()
    username = request.args.get('username')
    password = request.args.get('password')
    email = request.args.get('email')
    phoneNumber = request.args.get('phoneNumber')
    try:
        userData=userT.Select_by_AccountName(username)
        # checking if the name exists
        if (userData==None):
            rand=generateRandomId()
            userT.Insert_User(username,password,email,phoneNumber,rand)
            return "user successfully registered"
        return "Name Exists Choose Another"
    except:
        return "error while registering"

# getting a users name through his id
@app.route('/getNameById', methods=['POST','GET'])
def SendNameById():
    userT=Users()
    Id = request.args.get('Id')
    try:
        userData=userT.Select_by_Id(Id)
        if (userData==None):
            return "ID doesnt Exist"
        return str(userData[1])

    except:
        return "error while getting name by ID"

# adding a friend to a users friendList
@app.route('/addFriend', methods=['POST','GET'])
def addFriend():
    userT=Users()
    accountName=request.args.get('accountName')
    friendName=request.args.get('friendName')
    # checking if this account exists
    if (userT.Select_by_AccountName(friendName)!=None):
        check=userT.Select_by_AccountName(accountName)[6]
        # checking if this is first friendList
        if (check=='null'):
            # saving friend as a json
            userT.AddFreindListByName(accountName,json.dumps([friendName]))
        else:
            # getting friendList json and turning it into arr
            friendList=json.loads(check)
            # checking if friend exists in list
            for name in friendList:
                if (name==friendName):
                    return friendName+" is already your friend"
            # adding friend to arr and turning it into json to save
            friendList.append(friendName)
            userT.AddFreindListByName(accountName,json.dumps(friendList))
        return "added "+friendName+" to your friendList"
    else:
        return "friend not found"

# getting the friendList of a user
@app.route('/getFreindListByName', methods=['POST','GET'])
def getFreindListByName():
    userT=Users()
    accountName=request.args.get('accountName')
    friendList=userT.Select_by_AccountName(accountName)[6]
    return friendList
    
    
            
# running the server on port 5000
if __name__ == "__main__":
    print("hello")
    app.run(host="0.0.0.0")
