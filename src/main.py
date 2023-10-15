import pandas as pd
from distributer import distributer
from buyer import buyer
from middleman import middleman

def order():
    # order_file_name = input("Enter the path of the item order report: ")
    order_file_name = ""
    order_data = pd.read_csv(order_file_name)
    order_len = len(pd.read_csv(order_file_name))
    return order_file_name, order_data, order_len

def option():
    # option_file_name = input("Enter the path of the item option report: ")
    option_file_name = ""
    option_data = pd.read_csv(option_file_name)
    option_len = len(pd.read_csv(option_file_name))
    return option_file_name, option_data, option_len

def main():
    order_file_name, order_data, order_len = order()
    option_file_name, option_data, option_len = option()

    buyer(option_data, option_len)
    middleman()
    distributer(order_data, order_len)

main()