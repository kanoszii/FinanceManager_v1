"""IMPORT SECTION"""
import tkinter
from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button
from tkinter import messagebox, OptionMenu, StringVar, ttk
import sqlite3
from datetime import date, datetime
from tkcalendar import DateEntry


"""WINDOW + CANVAS"""
window = Tk()
window.title('Finance Manager by Jareczek')
window.config(width=770, height=600)
window.update_idletasks()
image = PhotoImage(file='logo.png')
canvas = Canvas(width=770, height=600)
canvas.create_image(120, 120, image=image)
canvas.place(x=0, y=0)

"""LABELS"""
title_label = tkinter.Label(text='Finance Manager', font=('Courier', 40, 'bold'), highlightthickness=0, fg='black')
title_label.place(x=250, y=40)
#
category_label = tkinter.Label(text='CATEGORY', font=('Arial', 15, 'bold'), highlightthickness=0, fg='black')
category_label.place(x=270, y=120)
#
product_label = tkinter.Label(text='PRODUCT', font=('Arial', 15, 'bold'), highlightthickness=0, fg='black')
product_label.place(x=415, y=120)
#
price_label = tkinter.Label(text='PRICE', font=('Arial', 15, 'bold'), highlightthickness=0, fg='black')
price_label.place(x=545, y=120)
#
date_label = tkinter.Label(text='DATE', font=('Arial', 15, 'bold'), highlightthickness=0, fg='black')
date_label.place(x=645, y=120)


"""TEXTBOXES"""
product_input = tkinter.Entry(width=18)                                                             #product
product_input.place(x=410, y=150)

price_input = tkinter.Entry(width=11)                                                               #price
price_input.place(x=540, y=150)

date_input = DateEntry(date_pattern='dd-mm-yyyy', width=11)                                         #time
date_input.place(x=630, y=150)                                


"""FUNCTIONS"""
def clear():
    value_inside.set("Select an Option")
    product_input.delete(0, tkinter.END)
    price_input.delete(0, tkinter.END)
    date_input.delete(0, tkinter.END)

def load_data():
    conn = sqlite3.connect('finance_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 'Finance Manager by Jareczek'")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fill_table():
    data = load_data()

    for row in data:
        tree.insert('', 'end', values=row)

def add_data():
    category = value_inside.get()
    product =product_input.get()
    price = price_input.get()
    date = date_input.get()

    if len(category) > 13 or len(product) <= 0 or len(price) <= 0 or len(date) != 10:
        messagebox.showinfo(title='', message='Data to save provided incorrectly')
    else:
        try:
            conn = sqlite3.connect('finance_database.db')
            cursor = conn.cursor()
            tree.insert("", "end", values=(category, product, price, date))

            cursor.execute("INSERT INTO 'Finance Manager by Jareczek' (Category, Product, Price, Date) VALUES (?, ?, ?, ?)",
                    (category, product, price, date))
            conn.commit()

            clear()

        except ValueError:
            messagebox.showeinfo(title='Oops', message='Price section supports only numbers')

def on_selection_change(*args):                                                                     #category menu (optionmenu)
    selected_value = value_inside.get()

def delete_data():
    selected_item = tree.selection()                                                                #download row info from table

    if not selected_item:
        messagebox.showinfo(title='Oops', message='Select a row to delete')
    item_id = selected_item[0]
    item_data = tree.item(item_id, 'values')                                                        #download data from selected row

    conn = sqlite3.connect('finance_database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM 'Finance Manager by Jareczek' WHERE Category=? AND Product=? AND Price=? AND Date=?",
                   (item_data[0], item_data[1], item_data[2], item_data[3]))
    
    conn.commit()
    conn.close()

    clear()

    tree.delete(item_id)                                                                            #delete row from gui

def modify_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showinfo(title='', message='Select a row to modify')
    item_id = selected_item[0]
    item_data = tree.item(item_id, 'values')

    new_category = value_inside.get()
    new_product =product_input.get()
    new_price = price_input.get()
    new_date = date_input.get()

    conn = sqlite3.connect('finance_database.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE 'Finance Manager by Jareczek' SET Category=?, Product=?, Price=?, Date=? WHERE Category=? AND Product=? AND Price=? AND Date=?",
                   (new_category, new_product, new_price, new_date, item_data[0], item_data[1], item_data[2], item_data[3]))
    conn.commit()
    conn.close()

    tree.delete(item_id)
    tree.insert("", "end", values=(new_category, new_product, new_price, new_date))
    messagebox.showinfo(title='', message='Data updated succesfully')

    clear()
options_list = ['Food', 'Transport', 'Subscriptions', 'Health', 'Relax', 'Bills', 'Others']
value_inside = tkinter.StringVar()
value_inside.set("Select an Option")
value_inside.trace("w", on_selection_change)

category_menu = tkinter.OptionMenu(window, value_inside, *options_list)
category_menu.config(width=14)
category_menu.place(x=270, y=145)


"""BUTTONS"""
add_button = tkinter.Button(text='Add', width=64, command=add_data)
add_button.place(x=270, y=175)

delete_button = tkinter.Button(text="Delete", command=delete_data)
delete_button.place(x=550, y=230)

modify_button = tkinter.Button(text='Update', width=64, command=modify_data)
modify_button.place(x=270, y=200)


"""TABLE SECTION"""
tree = ttk.Treeview(window, columns=("category", "product", "price", "date"), show="headings")
tree.heading("category", text="Category")                                                           #Headings settings
tree.heading("product", text="Product")
tree.heading("price", text="Price")
tree.heading("date", text="Date")
tree.column("category", width=120)                                                                  #Size of columns
tree.column("product", width=200)
tree.column("price", width=80)
tree.column("date", width=100)
tree.place(x=20, y=230)
scrollbar = tkinter.Scrollbar(window, command=tree.yview)                                           #scrollbar
scrollbar.place(x=522, y=230, height=230)
tree.configure(yscrollcommand=scrollbar.set)

def on_tree_select(event):
    selected_item = tree.selection()

    if not selected_item:
        return

    item_id = selected_item[0]
    item_data = tree.item(item_id, 'values')

    value_inside.set(item_data[0])
    product_input.delete(0, tkinter.END)
    product_input.insert(0, item_data[1])
    price_input.delete(0, tkinter.END)
    price_input.insert(0, item_data[2])
    date_input.delete(0, tkinter.END)
    date_input.insert(0, item_data[3])
tree.bind("<<TreeviewSelect>>", on_tree_select)


fill_table()                                                                                        #load db
window.mainloop()