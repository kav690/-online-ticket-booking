from ssl import SSL_ERROR_WANT_CONNECT
import mysql.connector
mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "kavya@2003",
    database = "busticket_db"
)
print("*************WELCOME TO ONLINE BUS TICKET BOOKING***************")
print("```````AVAILABLE BUS```````` :")
print("1.without ac")
print("2.with ac")
print("3.sleeper bus")
print("4.luxury bus")
print("5.delux bus")
def without_ac():
    print("BENEfITS : ")
    print("your body cool while travelling")
    print("and you comortable with ac bus")
    print("thank you for your booking")
def with_ac():
    print("BENEFITS :")
    print("you enjoy the nature air")
    print("and you comortable with this bus")
    print("thank you for your booking")
def sleeper_bus():
    print("BENEFITS :")
    print("when you feel tired and you take rest this bus ")
    print("you take sleep")
    print("you comortable this bus")
    print("thank you for your bokking")
def luxury_bus():
    print("BENEFITS :")
    print("you feel comortable with this bus")
    print("thank you for your booking")
def delux_bus():
    print("BEBEFITS :")
    print("you feel comortable with this bus")
    print("thank you for your booking")
user = int(input("enter your bus no :"))
if user == 1:
    print("yes your bus is available")
    print("plz enter the details")
    bus_type = input("enter your bus type you already choose :")
    name = input("enter your name :")
    seat_no = input("enter your seat no :")
    travel_from = input("enter your travel from city :")
    travel_to = input("enter your travel to city :")
    amount = input("pay your amount :")
    without_ac()
if user == 2:
    print("yes your bus is available")
    print("plz enter the details")
    bus_type = input("enter your bus type you already choose :")
    name = input("enter your name :")
    seat_no = input("enter your seat no :")
    travel_from = input("enter your travel from city :")
    travel_to = input("enter your travel to city :")
    amount = input("pay your amount :")
    with_ac()
if user == 3:
    print("yes your bus is available")
    print("plz enter the details")
    bus_type = input("enter your bus type you already choose :")
    name = input("enter your name :")
    seat_no = input("enter your seat no :")
    travel_from = input("enter your travel from city :")
    travel_to = input("enter your travel to city :")
    amount = input("pay your amount :")
    sleeper_bus()
if user == 4:
    print("yes your bus is available")
    print("plz enter the details")
    bus_type = input("enter your bus type you already choose :")
    name = input("enter your name :")
    seat_no = input("enter your seat no :")
    travel_from = input("enter your travel from city :")
    travel_to = input("enter your travel to city :")
    amount = input("pay your amount :")
    luxury_bus()
if user == 5:
    print("yes your bus is available")
    print("plz enter the details")
    bus_type = input("enter your bus type you already choose :")
    name = input("enter your name :")
    seat_no = input("enter your seat no :")
    travel_from = input("enter your travel from city :")
    travel_to = input("enter your travel to city :")
    amount = input("pay your amount :")
    delux_bus()
    bus_type = bus_type
    name = name
    seat_no = seat_no
    travel_from=travel_from
    travel_to=travel_to
    amount=amount
    val=(bus_type,name,seat_no,travel_from,travel_to,amount)
    sql="insert into details( bus_type,name,seat_no,travel_from,travel_to,amount)values(%s,%s,%s,%s,%s,%s)"
    mycursor=mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()
def insert(bus_type,name,seat_no,travel_from,travel_to,amount):
    mycursor=mydb.cursor()
    sql = "insert into details (bus_type,name,seat_no,travel_from,travel_to,amount)values (%s,%s,%s,%s,%s,%s)"
    details = (bus_type,name,seat_no,travel_from,travel_to,amount)
    mycursor.execute(sql,details)
    mydb.commit()
    print("insert data successfully")
def update(bus_type,name,seat_no,travel_from,travel_to,amount):
    mycursor=mydb.cursor()
    sql = "update details set  bus_type=%s,seat_no=%s,travel_from=%s,travel_to=%s, amount=%s where name=%s"
    details = (bus_type,name,seat_no,travel_from,travel_to,amount)
    mycursor.execute(sql,details)
    mydb.commit()
    print("update data successfully")
def select():
    mycursor=mydb.cursor()   
    sql = "select bus_type,name,seat_no,travel_from,travel_to,amount from details"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
def delete(name):
    mycursor = mydb.cursor()
    sql = "delete from details where name=%s "
    details =(name,)
    mycursor.execute(sql,details)
    mydb.commit()
    print("data delete successfully")

while True:
        print("1.insert data")
        print("2.update data")
        print("3.select data")
        print("4.delete data")
        print("5.exit")
        choice=int(input("enter your option:"))
        if choice == 1:
            bus_type= input("enter your bus already you choose :")
            name = input("enter your name:")
            seat_no= input("enter your seat no :")
            travel_from = input("enter your travel from city:")
            travel_to = input("enter your travel to city:")
            amount = input("ply your amount :")
            insert(bus_type,name,seat_no,travel_from,travel_to,amount)
        elif choice == 2:
            name = input("enter your name to update :")
            bus_type= input("enter your bus already you choose :")
            seat_no= input("enter your seat no :")
            travel_from = input("enter your travel from city:")
            travel_to = input("enter your travel to city:")
            amount = input("ply your amount :")
            update(bus_type,name,seat_no,travel_from,travel_to,amount)
        elif choice == 3:
            select()
        elif choice == 4:
           name = input("enter the name to delete:") 
           delete(name)
        elif choice == 5:
            print("exit")
        else:
            print("sorry")

