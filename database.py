import mysql.connector
import pandas as pd
import streamlit as st
import urllib.parse
from  sqlalchemy import create_engine
from Datasetcreation import Customers_Table
from Datasetcreation import Restaurant_table
from Datasetcreation import Deliveries_Table
from Datasetcreation import Orders_table


mydb =mysql.connector.connect(host="localhost",user="root",password="Varunchand@8",database="zomato")
password = urllib.parse.quote("Varunchand@8")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/zomato")
mycursor = mydb.cursor()






def customers_table_1():


       mycursor.execute("""CREATE TABLE IF NOT EXISTS Customers_Table(
                     customer_id VARCHAR(255) PRIMARY KEY,
                     name VARCHAR(255),
                     email VARCHAR(255),
                     phone VARCHAR(255),
                     location VARCHAR(255),
                     signup_details VARCHAR(255),
                     preferred_cuisine VARCHAR(50),
                     total_orders INT,
                     average_rating INT,
                     is_premium varchar(255),
                     order_value INT   
                      )
  
       
                     
          """)
 
  
   
      
       CUSTO_2 = Customers_Table()
       cust_value = """INSERT INTO Customers_Table (customer_id,name ,email ,phone ,location ,signup_details ,preferred_cuisine ,total_orders,average_rating,is_premium,order_value)  
       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
       for index, row in CUSTO_2.iterrows():
          values_customer= ( row['customer_id'],str(row['name']), row['email'], row['phone'],row['location'],row['signup_details'],row['preferred_cuisine'],row['total_orders'],row['average_rating'],row['is_premium'],row['order_value'])
          mycursor.execute(cust_value,values_customer)
          mydb.commit()
      
      

def restaurant_table_1():
        mycursor.execute("""CREATE TABLE IF NOT EXISTS Restaurant_table(
                    restaurant_id VARCHAR(255) PRIMARY KEY ,
                    name VARCHAR(255),
                    cuisine_type VARCHAR(50),
                    location VARCHAR(255),
                    owner_name VARCHAR(255),
                    average_delivery_time INT,
                    contact_number VARCHAR(255),
                    rating INT,
                    total_orders INT,
                    order_value INT,
                    active VARCHAR(15)
                    )
                 """)
 
        RESTO_2 = Restaurant_table()
 

        restaurant_values = """INSERT INTO Restaurant_table(restaurant_id,name,cuisine_type,location,owner_name,average_delivery_time,contact_number,rating,total_orders,order_value,active) 
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        for index ,row in RESTO_2.iterrows():
            values_restaurant = (row['restaurant_id'],str(row['name']),row['cuisine_type'],row['location'],row['owner_name'],row['average_delivery_time'],row['contact_number'],row['rating'],row['total_orders'],row['order_value'],row['active'])
            mycursor.execute(restaurant_values,values_restaurant)
            mydb.commit()
     
   
def oders_table_1():
              mycursor.execute(""" CREATE TABLE IF NOT EXISTS Orders_table(
                     order_id  VARCHAR(255) PRIMARY KEY,
                     customer_id VARCHAR(255),
                     restaurant_id VARCHAR(255),
                     order_date VARCHAR(255),
                     delivery_time VARCHAR(255),
                     status VARCHAR(255),
                     total_amount INT,
                     payment_mode VARCHAR(255) ,
                     discount_applied VARCHAR(255),
                     feedback_rating INT,
                     location VARCHAR(255)          
                     )
                   """)    
    
              ORDO_2 = Orders_table(Customers_Table(),Restaurant_table())

              order_values = """INSERT INTO Orders_table(order_id,customer_id,restaurant_id,order_date,delivery_time,status,total_amount,payment_mode,discount_applied,feedback_rating,location) 
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
              for index,row in ORDO_2.iterrows():
               values_orders = (row['order_id'],row['customer_id'],row['restaurant_id'],row['order_date'],row['delivery_time'],row['status'],row['total_amount'],row['payment_mode'],row['discount_applied'],row['feedback_rating'],row['location'])
               mycursor.execute(order_values,values_orders)
               mydb.commit()
    
   
   
def deliveries_table_1():
         mycursor.execute(""" CREATE TABLE IF NOT EXISTS Deliveries_Table(
                  delivery_id VARCHAR(255) PRIMARY KEY,
                 order_id  VARCHAR(255),
                 delivery_person_id VARCHAR(255),
                 delivery_status VARCHAR(20),
                 distance INT,
                 delivery_time VARCHAR(255),
                 estimated_time INT,
                 Delayed_In_Mins INT,
                 delivery_fee INT,
                 vehicle_type VARCHAR(5)
                 )""")

         DELI_2 = Deliveries_Table(Orders_table(Customers_Table(),Restaurant_table()))
         deliveries_values = """INSERT INTO Deliveries_Table(delivery_id,order_id,delivery_person_id,delivery_status,distance,delivery_time,estimated_time,Delayed_In_Mins,delivery_fee,vehicle_type) 
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
         for index,row in DELI_2.iterrows():
             values_orders = (row['delivery_id'],row['order_id'],row['delivery_person_id'],row['delivery_status'],row['distance'],row['delivery_time'],row['estimated_time'],row['Delayed_In_Mins'],row['delivery_fee'],row['vehicle_type'])
             mycursor.execute(deliveries_values,values_orders)
             mydb.commit()
   















 





