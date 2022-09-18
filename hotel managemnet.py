
from secrets import choice
from tkinter import Y
import mysql.connector
mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="kavya@2003",
    database = "hotel_db"
)
print("************welcome to hotel************")
choice = ["1-Breakfast","2-Lunch"]
for i in choice:
    print(i)
def data(choice):
    if choice==1:
        print("**********READY TO BREAKASY************")
        print("idly")
        print("dosa")
        print("poori")
        print("chapatti")
        print("parotta")
        your_order = input("enter your order :")
        if your_order == "idly"or "dosa" or "chapatti" or "poori"or "parota":
            print(f"yes your order {your_order} are available")
            how_many=int(input(f"how many{your_order}you want:"))
            print("idly_amount=5")
            print("dosa_amount=10")
            print("poori_amount=15")
            print("chapatti_amount=12")
            print("parotta_amount=20")
            cost=int(input("please enter your amount in above list:rs"))
            amnt=how_many*cost
            print(f"your bill is {amnt} with gst 4%")
            Amount=int(input("please enter the amount:"))
            print("please take the receipt")
            print("your order :{your_order}")
            print("your order amount is :{cost}")
            print("your total amount is:{amnt}")
            import datetime
            now =datetime.datetime.now()
            print("date and time:")
            print(now.strftime("%d-%m-%Y/t %H:%M:%S" ))
            print("thank you ")
            order_name=your_order
            how_many=how_many
            order_cost=cost
            total_amount=Amount
            val=(your_order,how_many,cost,Amount)
            sql="insert into order_details(order_name,how_many,order_cost,total_amount)values(%s,%s,%s,%s)"
            mycursor=mydb.cursor()
            mycursor.execute(sql,val)
            mydb.commit()
            def insert(order_name,how_many,order_cost,total_amount):
               mycursor=mydb.cursor()
               sql = "insert into order_details (order_name,how_many,order_cost,total_amount)values (%s,%s,%s,%s)"
               order_details = (order_name,how_many,order_cost,total_amount)
               mycursor.execute(sql,order_details)
               mydb.commit()
               print("insert data successfully")

            def update(order_name,how_many,order_cost,total_amount):
              mycursor=mydb.cursor()
              sql = "update order_details set order_name=%s,how_many=%s,order_cost=%s,total_amount=%s"
              order_details = (order_name,how_many,order_cost,total_amount)
              mycursor.execute(sql,order_details)
              mydb.commit()
              print("update data successfully")

            def select():
              mycursor=mydb.cursor()   
              sql = "select order_name,how_many,order_cost,total_amount from order_details"
              mycursor.execute(sql)
              result = mycursor.fetchall()
              print(result)
            def delete(order_name):
              mycursor = mydb.cursor()
              sql = "delete from order_details where order_name=%s "
              order_details =(order_name,)
              mycursor.execute(sql,order_details)
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
                 order_name = input("enter your order:")
                 how_many = input("how many you want :")
                 order_cost = input("enter your cost :")
                 total_order = input("enter your total amount :")
                 insert(order_name,how_many,order_cost,total_order)

              elif choice == 2:
                 order_name = input("enter your order:")
                 how_many = input("how many you want :")
                 order_cost = input("enter your cost :")
                 total_order = input("enter your total amount :")
                 update(order_name,how_many,order_cost,total_order)

              elif choice == 3:
                select()
     
              elif choice == 4:
                order_name = input("enter the order to delete:") 
                delete(order_name)
              elif choice == 5:
                print("exit") 
              else:
                print(f"sorry{your_order} is not available")

        elif choice==2:
            print("************lunch menu**********")
            print("biriyani")
            print("whiterice")
            print("varietyrice")
            Your_order=input("enter your order:").lower().strip()
            if Your_order=="biriyani" or "whiterice" or "varietyrice":
               print(f"yes your order{Your_order}is available")
               How_many=int(input(f"how mant{Your_order} you want :"))
               print("biriyani_amount=50")
               print("whiterice_amount=30")
               print("varietyrice_amount=40")
               Cost=int(input("please enter your dishes amount in above list:"))
               amount = How_many*Cost
               print(f"your bill is{amount} with gst 6%")
               amount=int(input("please enter the Amount:"))
               print("*********please take the receipt***********")
               print(f"Your order:{Your_order}")
               print(f"Your order Amount is {cost}")
               print(f"Your total Amount is:{amount}")
               import datetime
               now=datetime.datetime.now()
               print("date and time:")
               print(now.strftime("%d-%m-%Y/t%H:%M:%S"))
               print("*********thank you***********")
               order_name=your_order
               how_many=How_many
               order_cost=Cost
               total_amount=amount
               val=(Your_order,How_many,Cost,amount)
               sql = "insert into order_details(order_name,how_many,order_cost,total_amount )values(%s,%s,%s,%s)"
               mycursor=mydb.cursor()
               mycursor.execute(sql,val)
               mydb.commit()

            def insert(order_name,how_many,order_cost,total_amount):
                mycursor=mydb.cursor()
                sql = "insert into order_details (order_name,how_many,order_cost,total_amount)values (%s,%s,%s,%s)"
                order_details = (order_name,how_many,order_cost,total_amount)
                mycursor.execute(sql,order_details)
                mydb.commit()
                print("insert data successfully")

            def update(order_name,how_many,order_cost,total_amount):
                mycursor=mydb.cursor()
                sql = "update order_details set order_name=%s,how_many=%s,order_cost=%s,total_amount=%s"
                order_details = (order_name,how_many,order_cost,total_amount)
                mycursor.execute(sql,order_details)
                mydb.commit()
                print("update data successfully")

            def select():
                mycursor=mydb.cursor()   
                sql = "select order_name,how_many,order_cost,total_amount from order_details"
                mycursor.execute(sql)
                result = mycursor.fetchall()
                print(result)
            def delete(order_name):
                mycursor = mydb.cursor()
                sql = "delete from order_details where order_name=%s "
                order_details =(order_name,)
                mycursor.execute(sql,order_details)
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
                order_name = input("enter your order:")
                how_many = input("how many you want :")
                order_cost = input("enter your cost :")
                total_order = input("enter your total amount :")
                insert(order_name,how_many,order_cost,total_order)

             elif choice == 2:
               order_name = input("enter your order:")
               how_many = input("how many you want :")
               order_cost = input("enter your cost :")
               total_order = input("enter your total amount :")
               update(order_name,how_many,order_cost,total_order)

             elif choice == 3:
              select()
     
             elif choice == 4:
              order_name = input("enter the order to delete:") 
              delete(order_name)
             elif choice == 5:
              print("exit")
        else:
              print(f"sorry{your_order}is not available")
n = int(input("enter your choice:"))        
data(n)