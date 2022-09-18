import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "kavya@2003",
    database = "atm"
)

print("***************WELCOME TO ATM **************")
print("you can withdraw and balance only check this atm")
print("if you withdraw your amount goto insert option ")
print("if you check your balance then goto select balance option")

def insert(LANGUAGE,PIN_NO,ACCOUNT_TYPE,WITHDRAWAL_AMOUNT):
    mycursor = mydb.cursor()
    sql ="insert into withdraw(language,pin_no,account_type,withdrawal_amount) values(%s,%s,%s,%s)"
    withdraw = (LANGUAGE,PIN_NO,ACCOUNT_TYPE,WITHDRAWAL_AMOUNT)
    mycursor.execute(sql,withdraw)
    mydb.commit()
    print("data inserted successfully")
def update (LANGUAGE,PIN_NO,ACCOUNT_TYPE,WITHDRAWAL_AMOUNT):
    mycursor = mydb.cursor()
    sql ="update withdraw set language=%s,account_type=%s,withdrawal_amount=%s where pin_no=%s"
    withdraw = (LANGUAGE,PIN_NO,ACCOUNT_TYPE,WITHDRAWAL_AMOUNT)
    mycursor.execute(sql,withdraw)
    mydb.commit()
    print("data updated successfully")
def select():
    mycursor = mydb.cursor()
    sql = "select balance from balance "
    mycursor.execute(sql)
    result = mycursor.fetchone()
    print(result)
def delete(PIN_NO):
    mycursor = mydb.cursor()
    sql = "delete from withdraw where pin_no=%s"
    withdraw = (PIN_NO,)
    mycursor.execute(sql,withdraw)
    mydb.commit()
    print("data delete successfully")
while True:
    print("1.insert data")
    print("2.update data")
    print("3.delete data")
    print("4.select balance")
    choice = int(input("enter your option :"))
    if choice == 1:
        print("swap your atm card")
        language = input("select your language :")
        pin_no = input("enter your pin no :")
        account_type = input("select your account type :")
        withdrawal_amount = input("how much amount you want :")
        print ("take your amount")
        insert(language, pin_no,account_type,withdrawal_amount)
    elif  choice == 2:
        print("swap your atm card")
        pin_no = input("enter your pin no to update  :")
        language = input("select your language :")
        account_type = input("select your account type :")
        withdrawal_amount = input("how much amount you want :")
        update(language, pin_no,account_type,withdrawal_amount)
    elif choice == 3:
        select()
    elif choice == 4:
        pin_no = input("enter your pin no to delete :")
        delete (pin_no)
    elif choice == 5:
        pin_no =  input("enter your pin :")
        language = input("select your language :")
        account_type = input("select your account type :")
        print("your balance :")
        select()
    else:
        print("sorry invalid section")
        