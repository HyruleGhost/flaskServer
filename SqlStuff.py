import sqlite3
import json

class Users:
    # creating the table if it doesnt exists
    def __init__(self,tablename="Users",Num="Num",AccountName="AccountName",Password="Password",Email="Email",PhoneNumber="PhoneNumber",Id="Id",FreindList="FreindList"):
        self.__tablename=tablename
        self.__Num=Num
        self.__AccountName=AccountName
        self.__Password=Password
        self.__Email=Email
        self.__PhoneNumber=PhoneNumber
        self.__Id=Id
        self.__FreindList=FreindList
        conn = sqlite3.connect('UserT.db')
        print("Opened database successfully")
        commend = "CREATE TABLE IF NOT EXISTS " +self.__tablename + "(" + self.__Num + " " + " INTEGER PRIMARY KEY AUTOINCREMENT ,"
        commend += " " + self.__AccountName +  " TEXT    NOT NULL ,"
        commend += " " + self.__Password +  " TEXT    NOT NULL ,"
        commend += " " + self.__Email + " TEXT    NOT NULL ,"
        commend += " " + self.__PhoneNumber + " TEXT    NOT NULL ,"
        commend += " " + self.__Id + " TEXT    NOT NULL ,"
        commend += " " + self.__FreindList + " JSON    NOT NULL )"
        conn.execute(commend)
        print ("Table created successfully")
        conn.commit()
        conn.close()
    
    # inserting a user to the table
    def Insert_User(self,AccountName,Password,Email,PhoneNumber,Id):
        conn = sqlite3.connect('UserT.db')
        str_insert = "INSERT INTO " + self.__tablename + " (" + self.__AccountName +"," + self.__Password +","+self.__Email +","+self.__PhoneNumber +","+self.__Id+","+self.__FreindList+") VALUES (" +  "'" +AccountName + "'" + "," + "'" +Password +"'" +","+ "'" +Email +"'" +","+"'"+PhoneNumber+"'"+","+"'"+str(Id)+"'"+","+"'[]'"+");"
        print (str_insert)
        conn.execute(str_insert)
        conn.commit()
        conn.close()
        print ("User inserted successfully")

    # getting spesific user staff by his name
    def Select_by_AccountName(self,AccountName):
        conn = sqlite3.connect('UserT.db')
        strsql = "SELECT Num, AccountName, Password, Email, PhoneNumber, Id, FreindList    from " +self.__tablename + " where " + self.__AccountName + "='" + AccountName+"'"
        print(strsql)
        cursor = conn.execute(strsql)
        for row in cursor:
            conn.close()
            return row

    # getting spesific user staff by his ID
    def Select_by_Id(self,Id):
        conn = sqlite3.connect('UserT.db')
        strsql = "SELECT Num, AccountName, Password, Email, PhoneNumber, Id, FreindList   from " +self.__tablename + " where " + self.__Id + "='" + str(Id)+"'"
        print(strsql)
        cursor = conn.execute(strsql)
        for row in cursor:
            # print("Operation done successfully")
            conn.close()
            return row

    # updating user staff by his ID
    def Update_by_Id(self,Id,AccountName,Password,Email,PhoneNumber):
        conn=sqlite3.connect('UserT.db')
        str_update="UPDATE "+ self.__tablename+" SET "+self.__AccountName+"='"+AccountName+"', "+self.__Password+"='"+Password+"', "+self.__Email+"='"+Email+"', "+self.__PhoneNumber+"='"+PhoneNumber+"' WHERE "+self.__Id+"='"+str(Id)+"'"
        conn.execute(str_update)
        conn.commit()
        conn.close()
        print("Updated Account")

    # adding a FreindList to an account
    def AddFreindListByName(self,AccountName,FreindList):
        conn=sqlite3.connect('UserT.db')
        str_update="UPDATE "+ self.__tablename+" SET "+self.__FreindList+"='"+FreindList+"' WHERE "+self.__AccountName+"='"+AccountName+"'"
        conn.execute(str_update)
        conn.commit()
        conn.close()
        print("Add FreindList")

    def Get_Every_Id(self):
        conn=sqlite3.connect('UserT.db')
        IdArr=[]
        strsql="SELECT Id from "+self.__tablename
        print(strsql)
        cursor = conn.execute(strsql)
        for row in cursor:
            IdArr.append(row[0])
        return IdArr
        conn.close()

    def __str__(self):
        return "table name is "+self.__tablename
    def get_table_name(self):
        return  self.__tablename