import os
import time
from language import *
import sqlite3
import subprocess

subprocess.run(["h.bat"])


def cls_nt():
    os.system('cls' if os.name == 'nt' else 'clear')


def sort_data(*args):
    for result in args:
        for first_result in result:


            if first_result is str and float or int:


                for item , last_result in enumerate(first_result):

                    end_char = " --- " if item == 0 else "\n"
                    print(last_result , end = end_char )


            else:
                for last_result in first_result:

                    print(last_result)


    def sort_str_data(*args):
        num = 0
        for sort in args:
            for sort_data in sort:
                for result in sort_data:
                    num += 1
                    print(f"\t {num} --- {result}")
    return sort_str_data







def sort_price(*args):
    for first_result in args:
        for last_result in first_result:
            for price in last_result:
                print(price)


def enter():
    time.sleep(1)
    print(f"\n                  {UA[9]}")
    choose = input()
    cls_nt()


"""
     КАТЕГОРІЇ    
"""
connect = sqlite3.connect("shop.db")
cursor_category = connect.cursor()

cursor_category.execute(
    """SELECT category
    FROM products 
    GROUP BY category"""
    )

rows_category = cursor_category.fetchall()
ssd = sort_data()

def category():
    s = ssd(rows_category)






    
    