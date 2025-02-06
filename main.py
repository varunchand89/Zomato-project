import streamlit as st
import urllib.parse
import mysql.connector
import pandas as pd
from analysis import Zomato_analysis
from CURD import curd_3
from  sqlalchemy import create_engine
from database import restaurant_table_1
from database import customers_table_1
from database import deliveries_table_1
from database import oders_table_1

import sys
sys.path.append("C:/Users/Hp/OneDrive/Desktop/zomato_project/CURD.py")
mydb =mysql.connector.connect(host="localhost",user="root",password="Varunchand@8",database="zomato")
password = urllib.parse.quote("Varunchand@8")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/zomato")
mycursor = mydb.cursor()

st.markdown(
    """<style> 
        .stApp {
            background-color: #00FFFF;
        }
    </style>
    """,
     unsafe_allow_html=True
    )

st.title('Zomata - Food Delivery Data Insights Using Python and SQL')
 



zomato_conection = Zomato_analysis(host="localhost",user="root",password="Varunchand@8",database="zomato")
curd_1 = curd_3(host="localhost",user="root",password="Varunchand@8",database="zomato")







#For analysis

zomato_tables = st.selectbox("Table for analysis Tables",["SELECT ONE","Customers_Table","Restaurant_table","Deliveries_Table","Orders_table"])

if zomato_tables == "Customers_Table":
   if  st.button("Submit Customers"):
      dh = customers_table_1()
      df = pd.read_sql("SELECT * FROM Customers_Table", con=engine)
      st.write(df)
   if st.button("Show me the analysis"):
    st.write("Analyzing customer preferences and order patterns")
    customers_df, customers_dz, customers_dg = zomato_conection.customers_analysis()
    st.dataframe(customers_dg)
    st.write("Identifying top customers based on order frequency and value")
    st.dataframe(customers_df)
    st.dataframe(customers_dz)
     

if zomato_tables == "Restaurant_table":
   if st.button("Submit Restaurant"):
    dg = restaurant_table_1()
    df = pd.read_sql("SELECT * FROM Restaurant_table", con=engine)
    st.write(df) 
   if st.button("Show me the analysis"): 
    Restaurant_vc,Restaurant_cv,Restaurant_nb,Restaurant_op = zomato_conection.restaurant_analysis()
    st.write("Evaluating the most popular restaurants and cuisines.")
    st.dataframe(Restaurant_vc);st.dataframe(Restaurant_cv)
    st.write("Monitoring order values and frequency by restaurant.")
    st.dataframe(Restaurant_nb);st.dataframe(Restaurant_op)


if zomato_tables == "Orders_table":
   if st.button("Submit orders"):
      dj = oders_table_1()
      df = pd.read_sql("SELECT * FROM orders_table", con=engine)
      st.write(df)
   if st.button("Show me the analysis"):  
      st.write("Identifying peak ordering times and locations.") 
      orders_di, orders_dj, orders_do = zomato_conection.orders_analysis()
      st.dataframe(orders_di)
      st.dataframe(orders_dj)
      st.write("Tracking delayed and canceled deliveries.") 
      st.dataframe(orders_do) 

if zomato_tables == "Deliveries_Table":
   if st.button("Submit Deliveries"):
    dk = deliveries_table_1()
    df = pd.read_sql("SELECT * FROM Deliveries_Table", con=engine)
    st.write(df) 
   if st.button("Show me the analysis"):
    st.write("Analyzing delivery times and delays to improve logistics")  
    deliveries_di, deliveries_df = zomato_conection.delivery_analysis()
    st.write(deliveries_di) 
    st.write("Tracking delivery personnel performance.")
    st.write(deliveries_df)  

 #curd operation 


C_table = st.selectbox('Which operation need to be performed', ['SELECT ANY ONE', 'CREATE', 'UPDATE', 'SELECT', 'DELETE', 'INSERT','SHOW'])






if C_table == "CREATE":
    st.warning('Blocked names "Customers_Table","Restaurant_table","Deliveries_Table","Orders_table"' )

    x = st.text_input("Enter a table name : ")
    
    num_colu = st.number_input("Enter number of rows: ",value=0,step=1)
    
    columns=[]
    for i in range(num_colu):
           
            column_name = st.text_input(f"Enter col name : {i +1 } ")
            column_datatype = st.text_input(f"Enter data type {i+1}{column_name} :")
            columns.append((column_name, column_datatype)) 
    columns_1 = ",".join(f"{col[0]} {col[1]}" for col in columns) 
    create_table_a = curd_1.create_table(x,columns_1)
    st.write(create_table_a)         


    
            
    

elif C_table == "UPDATE":
    y = st.text_input("Enter a table name :")
    new_column_name = st.text_input("Enter a column name :")
    new_row_value = st.text_input(f"Enter new a row value for {new_column_name}:")
    column_name = st.text_input("Enter column name :")
    row_value = st.text_input(f"Enter row value {column_name}")
    update_table_b = curd_1.update_table(y,column_name,new_column_name,new_row_value,row_value)

    if st.button("Submit update"):
       st.write(update_table_b)  


elif C_table == "SELECT":
  
    z = st.text_input("Enter a table name :")
    select_table_df = curd_1.select_table(z)
    if st.button("submit Select"):
       st.dataframe(select_table_df) 
  


elif C_table == "DELETE":
  
    w = st.text_input("Enter a table name  to delete : ")
    delete_table_c = curd_1.delete_table(w)
    if st.button("Submit Delete"):
       st.write("Deleted")
         
         

elif C_table == "INSERT":
    table_name = st.text_input("Enter a table name : ")
    
    query_1 = (f"SELECT *  FROM {table_name}")
    df= mycursor.execute(query_1)
    columns = [col[0] for col in mycursor.description] 
    st.dataframe(columns)
    rows = []
    num_colu = len(columns) 
    with st.form(key="data_form"):  
      for i in range (num_colu):
       row_values =st.text_input(f"Enter row name :{i} ")
       rows.append(row_values)
      submit_button = st.form_submit_button("Submit") 
      row_1 = ",".join(["%s"]*num_colu )
    if st.button("Submit Insert"):
      insert_values_y = curd_1.insert_values(table_name,columns,row_1,rows)
      st.write(insert_values_y)

elif C_table == "SHOW":
   table_name = st.text_input("Enter a table name : ")
   show_values_t =curd_1.show_table(table_name)
   if st.button("Submit Show"):
      st.dataframe(show_values_t)
    
 



    
    
    


              








 