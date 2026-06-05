from flask import Flask, request
import sqlite3
import re

app = Flask(__name__)

##---Database--##
def create_table():
    connect = sqlite3.connect("hospital.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE if not exists patients(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name text not null,
                   dob text not  null,
                   gender text not null,
                   email text unique not null,
                   phone text unique not null,
                   address text)""")
    connect.commit()
    connect.close()
def get_connection():
        return sqlite3.connect("hospital.db")

    ##validator class##
class PatientValidator:
        def validate_name(self,name):  ##_name__#
            if not re.fullmatch(r"[A-Za-z]+",name):
                raise ValueError(
                    "name should contain only letter and space"
                )
        def validate_email(self,email): #___email___#
            if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",email):


                raise ValueError(
                    "invalid email format"
                )
        def validate_phone(self,phone):#____phone___#
            if not re.fullmatch(r"[6-9][0-9]{9}",phone):
                raise ValueError(
                    "phone should be 10 digit "
                )


##____patient class___##
class Patient:
    def __init__(self,name,dob,gender,email,phone,address):

        validator = PatientValidator()
        validator.validate_name(name)
        validator.validate_email(email)
        validator.validate_phone(phone)

        self.name=name
        self.dob = dob
        self.gender= gender
        self.email= email
        self.phone = phone
        self.address= address

create_table()


##____home route___####

@app.route("/")
def home():
    return "patient management api running"


###__register patient__##



@app.route('/patient',methods=['POST'])
def add_patients():
    try:

        data= request.get_json()

        patient = Patient(
            data["name"],
            data["dob"],
            data["gender"],
            data["email"],
            data["phone"],
            data["address"])
        connect = sqlite3.connect("hospital.db")
        cursor=connect.cursor()
        cursor.execute(
            """insert into patients(name,dob,gender,email,phone,address)
            values(?,?,?,?,?,?)""",

            (
                data["name"],
                data["dob"],
                data["gender"],
                data["email"],
                data["phone"],
                data["address"]



            )
        )
        connect.commit()
        connect.close()
        return "patient register sucessfully "
    except Exception as error:
        print("ERROR:",error)
        return str(error)


@app.route("/patients",methods=['GET'])
def get_patients():
    connect= sqlite3.connect("hospital.db")
    cursor= connect.cursor()
    cursor.execute("select * from patients")

    all_patients= cursor.fetchall()
    connect.close()

    result=[]

    ##-convert each row into dictionary
    for patient in all_patients:
        patient_data={
            "id":patient[0],
            "name":patient[1],
            "dob":patient[2],
            "gender":patient[3],
            "email":patient[4],
            "phone":patient[5],
            "address":patient[6]
        }
        result.append(patient_data)

    return (result)


##--- view single patient__##

@app.route('/details/<int:id>',methods=['GET'])
def get_patient(id):
    connect=sqlite3.connect("hospital.db")
    cursor = connect.cursor()
    cursor.execute(
        "select *from patients where id = ?",
        (id,)
    )

    patients = cursor.fetchone()
    connect.close()

    if patients:
        return({
            "id":patients[0],
            "name":patients[1],
            "dob":patients[2],
            "gender":patients[3],
            "email":patients[4],
            "phone":patients[5],
            "address":patients[6]
        })
    return({"message":"patient not found"})

@app.route('/delete/<int:id>',methods=["DELETE"])
def delete_patient(id):
    connect=sqlite3.connect("hospital.db")
    cursor= connect.cursor()
    cursor.execute("delete from patients where id =?",(id,))
    connect.commit()
    connect.close()

    return {
        "message":"patient delete sucessfully"
    }
if __name__=="__main__":

    app.run(port=5000)