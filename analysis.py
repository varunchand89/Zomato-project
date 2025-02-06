import streamlit as st
import pandas as pd
import urllib.parse
import mysql.connector
from  sqlalchemy import create_engine


class Zomato_analysis:
 

 def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = urllib.parse.quote(password)
        self.database = database
        self. mydb =mysql.connector.connect(host=self.host,user=self.user,password=password ,database=self.database)
        self.engine = create_engine(f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}/{self.database}")
        self.mycursor = self.mydb.cursor()

 def customers_analysis(self):


    query_1 =("SELECT name,order_value FROM Customers_Table  order by  order_value DESC  LIMIT 3 ")
    query_2 =("SELECT name , total_orders FROM Customers_Table  order by total_orders DESC  LIMIT 3")
    query_3 =("SELECT preferred_cuisine,COUNT(*) AS preference FROM Customers_Table GROUP BY  preferred_cuisine ") 
    df = pd.read_sql(query_1, con = self.engine)
    dz = pd.read_sql(query_2 , con = self.engine)
    dg = pd.read_sql(query_3 , con = self.engine)
    
    return df,dz,dg

 def restaurant_analysis(self):
    query_1=("SELECT name ,COUNT(*) AS Famous_restaurant FROM Restaurant_table GROUP BY name ORDER BY Famous_restaurant DESC LIMIT 4")  
    query_2 =("SELECT cuisine_type,COUNT(*) AS preffered_cuisine FROM Restaurant_table GROUP BY cuisine_type ORDER BY preffered_cuisine DESC")
    query_3 = ("SELECT order_value FROM Restaurant_table ORDER BY order_value DESC ")
    query_4 = ("SELECT rating,cuisine_type, GROUP_CONCAT(name) AS names ,COUNT(*) AS most_rating, COUNT(*) AS Prefered_cuisine  FROM restaurant_table GROUP BY  rating,cuisine_type ORDER BY rating DESC ;")
    vc = pd.read_sql(query_1, con = self.engine)
    cv = pd.read_sql(query_2, con = self.engine)
    nb = pd.read_sql(query_3, con = self.engine)
    op = pd.read_sql(query_4, con = self.engine)
    return vc,cv,nb,op
    
 def orders_analysis(self):
      
      query_1 =("SELECT HOUR(order_date) AS order_Hour, COUNT(*) AS peak_order FROM orders_table GROUP BY order_Hour ORDER BY peak_order DESC LIMIT 3")
      query_2 = ("SELECT location , COUNT(*) AS peak_location FROM  orders_table GROUP BY location ")
      query_3 =("SELECT status, COUNT(*) AS Status_1 FROM  orders_table WHERE status = 'pending' OR status = 'Cancelled' GROUP BY status ")
      di = pd.read_sql(query_1 , con = self.engine)
      dj = pd.read_sql(query_2 , con = self.engine)
      do = pd.read_sql(query_3 , con = self.engine)
      return di,dj,do
 
 def delivery_analysis(self):
      
     
    query_1 = ("SELECT estimated_time AS Delivery_estimated , COUNT(*) AS delayed_count FROM deliveries_table GROUP BY estimated_time ORDER BY Delivery_estimated")
    query_2 =("SELECT delivery_person_id,estimated_time,Delayed_In_Mins FROM deliveries_table ORDER BY  Delayed_In_Mins ASC ")
    di = pd.read_sql(query_1 , con = self.engine)
    df = pd.read_sql(query_2 , con = self.engine)
    return di,df
  







