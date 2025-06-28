import sqlite3
import os
from language import*
import time
from os_command import*


connect = sqlite3.connect("shop.db")
cursor = connect.cursor()


rows = cursor.fetchall()


language = int(input("оберіть мову : UA -- 1"
"\n               EN -- 2\n"))


cls_nt()

print(f"                    {UA[1]}")


while True:
    if language == 1 or "UA":
        print(f"                    {UA[2]}\n")
        print(f"    {UA[3]}")
        print(f"    {UA[4]}")
        print(f"    {UA[5]}")
        print(f"    {UA[6]}")
        print(f"    {UA[7]}")
        print(f"    {UA[8]}")
        
        choose = int(input())
        cls_nt()

        if choose == 1:
            cursor.execute(
                """SELECT SUM(products.price * orders.quantity) AS Total_Sales
                FROM orders 
                INNER JOIN products ON orders.product_id = products.product_id;"""
                           )
            
            rows = cursor.fetchall()
            sort_price(rows)

        if choose == 2:
            cursor.execute(
                """SELECT customers.first_name , customers.last_name ,COUNT(orders.order_id) AS Order_Count
                FROM customers 
                INNER JOIN orders ON customers.customer_id = orders.customer_id
                GROUP BY customers.customer_id;"""
                           )
            
            rows = cursor.fetchall()

            for first_name , last_name , orders in rows:
                print(first_name , last_name , "--" , orders)

            enter()
            cls_nt()
            
        if choose == 3:
            cursor.execute(
                """SELECT ROUND(AVG(products.price * orders.quantity), 2) AS AVG_Sales
                FROM orders 
                INNER JOIN products ON orders.product_id = products.product_id;"""
                           )
            
            rows = cursor.fetchall()
            sort_price(rows)

        if choose == 4:
            cursor.execute(
                """SELECT products.category , COUNT(orders.order_id) AS Order_Count
                FROM orders
                INNER JOIN products ON orders.product_id = products.product_id
                GROUP BY products.category
                ORDER BY Order_Count DESC 
                LIMIT 1;"""
                           )
            rows = cursor.fetchall()
            sort_data(rows)
            enter()

        if choose == 5:
            cursor.execute(
                """SELECT products.category , COUNT(products.category) AS Category_Count
                FROM products
                GROUP BY products.category;"""
                )
            rows = cursor.fetchall()
            sort_data(rows)
            enter()

        if choose == 6:
            choose = input("виберіть категорію")

        