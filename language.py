from colorama import init, Fore, Style



init()


UA = {
    1 : "Вітаю",
    2 : "Оберіть дію",
    3 : "1 --- Переглянути суму всіх замовлень",
    4 : "2 --- Вивести всі замовлення кожного клієнта",
    5 : "3 --- Знайти середнє значення всіх замовлень",
    6 : "4 --- Вивести одну найпопулярнішу покупку",
    7 : "5 --- Вивести кількість товарів у кожній категорії",
    8 : "6 --- Змінити ціни в категорії (виберіть категою та на скільки %)",
    9 : f"{Fore.WHITE}{Style.DIM}Нажміть ентер{Style.RESET_ALL}",
    10 : " --- Категорія",
    11 : "Виберіть категорію\n",
    12 : f"{Fore.LIGHTCYAN_EX}Пітвердити дію? \n        {Fore.GREEN}так -- 1 \n         {Fore.RED}ні -- 2 \n{Style.RESET_ALL}",
    13 : f"{Fore.RED}Відмінено{Style.RESET_ALL}\n",
    14 : "Введіть на скільки процентів хочете збільшити ціну\n",
    15 : "7 --- Вихід"
  } 





EN = {
    1 : "Hello",
    2 : "Choose an action",
    3 : "1 --- View the total of all orders",
    4 : "2 --- Display all orders for each customer",
    5 : "3 --- Find the average of all orders",
    6 : "4 --- Show one most popular purchase",
    7 : "5 --- Display the number of products in each category",
    8 : "6 --- Change prices in a category (select category and by how much %)",
    9 : f"{Fore.WHITE}{Style.DIM}Press enter{Style.RESET_ALL}",
    10 : " --- Category",
    11 : "Select a category\n",
    12 : f"{Fore.LIGHTCYAN_EX}Confirm action? \n        {Fore.GREEN}yes -- 1 \n         {Fore.RED}no -- 2 \n{Style.RESET_ALL}",
    13 : f"{Fore.RED}Canceled{Style.RESET_ALL}\n",
    14 : "Enter the percentage you want to increase the price by.\n",
    15 : "7 --- Exit"
  } 
