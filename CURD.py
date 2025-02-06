from altair import to_values
import streamlit as st
import urllib.parse
import mysql.connector
import pandas as pd
from  sqlalchemy import create_engine 

class curd_3():
 
 def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = urllib.parse.quote(password)
        self.database = database
        self. mydb =mysql.connector.connect(host=self.host,user=self.user,password=password ,database=self.database)
        self.engine = create_engine(f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}/{self.database}")
        self.mycursor = self.mydb.cursor()
        
 
 def insert_values(self,table_name,columns,row_1,rows):
   for i, value in enumerate(rows):
        
        if columns[i] == 'total_orders' and value == '':
            rows[i] = 0  
        elif value == '': 
            rows[i] = None
   query = (f"INSERT INTO {table_name} ({",".join(columns)}) VALUES ({row_1}) ")
   y = self.mycursor.execute(query,tuple(rows))
   self.mydb.commit()
   return y

 def delete_table(self,w):
   try: 
    query = (f"DROP TABLE {w} ;")
    self.mycursor.execute(query)
    self.mydb.commit()
    
   except:
      print("Table not exsists") 

 def create_table(self,x,columns_1):
    
    query = (f"CREATE TABLE  {x} ({columns_1})")

    a =  self.mycursor.execute(query)
    self.mydb.commit()
    return a 
 
 def update_table(self,y,column_name,new_column_name,new_row_value,row_value):
    
    

    query_1= (f"UPDATE {y} SET {column_name} =%s WHERE {new_column_name} = %s") 
    set_value = (new_row_value.strip(),row_value.strip())
    b =  self.mycursor.execute(query_1,set_value)
    self.mydb.commit()
    return b
    

 def select_table(self,z):
    
    
  
    self.mycursor = self.mydb.cursor()
    query = (f"SELECT * from  {z} ")
    self.mycursor.execute(query)
    rows = self.mycursor.fetchall()
    df = pd.read_sql(f"{query}", con=self.engine)
    return rows
    
 def show_table(self,t):
     
    self.mycursor = self.mydb.cursor()
    query = (f"SHOW COLUMNS FROM  {t} ")
    self.mycursor.execute(query)
    rows = self.mycursor.fetchall()
    return rows



