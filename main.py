from flask import Flask, request
import sqlite3
import re

app = Flask(__name__)

##---Database--##
def create_table():
    connect = sqlite3.connect("hospital.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE if not exists patients(id int,"
                   "name text not null,"
                   "dob text not  null,"
                   "gender text not null,"
                   "email text unique not null,"
                   "phone text unique not null,"
                   "address text)")
    connect.commit()
    connect.close()
    def get_connection():
        return sqlite3.connect("hospital.db")

    ##validator class##
    class PatientValidator:
        def validate_name(name):  ##_name__#
            if not re.fullmatch(r"[A-Za-z]+",name):
                raise ValueError(
                    "name should contain only letter and space"
                )
        def validate_email(email): #___email___#
            if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",email):


                raise ValueError(
                    "invalid email format"
                )
        def validate_phone(phone):#____phone___#
            if not re.fullmatch(r"[6-9][0-9]{9}",phone):
                raise ValueError(
                    "phone should be 10 digit "
                )


##____patient class___##
class Patient:
    def __init__(self,name,dob,gender,email,phone,address):
        self.name=name
        self.dob = dob
        self.gender= gender
        self.email= email
        self.phone = phone
        self.address= address





