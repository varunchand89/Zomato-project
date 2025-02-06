import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker() 

np.random.seed(23)

def Customers_Table(num_customers =10):
    customer=[]
    for _ in range (num_customers):
        customer.append({
            "customer_id":fake.uuid4(),
            "name":fake.name(),
            "email":fake.email(),
            "phone":fake.phone_number(),
            "location":fake.address(),
            "signup_details":fake.date_time_between(start_date = '-1y', end_date ='now'),
            "preferred_cuisine":fake.random_element(elements=["chinese","indian","arab","italian"]),
            "total_orders":np.random.randint(0,100),
            "average_rating":fake.random_element(elements=[1,2,3,4,5]),
            "is_premium":fake.random_element(elements=["YES","NO"]),
            "order_value":np.random.randint(50,100)
        })
    custo_1 = pd.DataFrame(customer)
    return custo_1

def Restaurant_table(num_restaurant = 10):
    restaurant=[]
    for _ in range(num_restaurant):
        restaurant.append({
            "restaurant_id":fake.uuid4(),
            "name":fake.random_element(elements=["Taj","ITC","The Park","Courtyard"]),
            "cuisine_type":fake.random_element(elements=["chinese","indian","arab","italian"]),
            "location":fake.address(),
            "owner_name":fake.name(),
            "average_delivery_time":np.random.randint(1,20),
            "contact_number":fake.phone_number(),
            "rating":fake.random_element(elements=[1,2,3,4,5]),
            "total_orders":np.random.randint(0,100),
            "order_value":np.random.randint(50,100),
            "active":fake.random_element(elements=["OPEN","CLOSE","TEMPCLOSED"])
        })
    
    rest0_1 = pd.DataFrame(restaurant)
    return rest0_1

def Orders_table(Customers_Table,Restaurant_table,num_orders = 10):
    order=[]
    for _ in range(num_orders):
        order.append({
            "order_id" :fake.uuid4(),
            "customer_id": np.random.choice(Customers_Table["customer_id"]),
            "restaurant_id":np.random.choice(Restaurant_table["restaurant_id"]),
            "order_date":fake.date_time_between(start_date = '-1y', end_date ='now'),
            "delivery_time" : fake.date_time_between(start_date = '-1y', end_date ='now'),
            "status":fake.random_element(elements=["Pending", "Delivered", "Cancelled"]),
            "total_amount":np.random.randint(0,4000),
            "payment_mode":fake.random_element(elements=["Credit Card", "Cash", "UPI"]),
            "discount_applied":fake.random_element(elements=["10%","20%","15%"]),
            "feedback_rating":np.random.randint(1,5),
            "location":fake.random_element(elements=["Mumbai", "DELHI", "chennai","kochi"])

        })
    
    ordo_1 = pd.DataFrame(order)
    return ordo_1

def Deliveries_Table(Orders_table,num_delivers = 10):
    deliver=[]
    for _ in range(num_delivers):
        deliver.append({
            "delivery_id": fake.uuid4(),
            "order_id":np.random.choice(Orders_table["order_id"]),
            "delivery_person_id":fake.uuid4(),
            "delivery_status":fake.random_element(elements=["On the way","Delivered"]),
            "distance":np.random.randint(3,40),
            "delivery_time" :fake.date_time_between(start_date = '-1y', end_date ='now'),
            "estimated_time":np.random.randint(3,40),
            "Delayed_In_Mins":np.random.randint(1,60),
            "delivery_fee":np.random.randint(3,40),
            "vehicle_type":fake.random_element(elements=["Bike","Car"])
        })

    delivo_1 = pd.DataFrame(deliver)
    return delivo_1










