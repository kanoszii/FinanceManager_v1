# Finance Manager [early phase]

Finance Manager is a self-developed application written in procedural Python. It allows users to record their expenses in specific categories, including the date. The project encompasses essential components such as a user-friendly GUI, complete button functionality, windows management, and comprehensive exception handling for possible user errors (e.g., omitting a date or not specifying an expense category). User input is stored in a database file (.db). Additionally, an attached "emailsenderv2.py" file contains a basic script for sending email messages with attachments at predefined intervals.

The program currently leverages modules such as sqlite, datetime, and tkinter to create a graphical user interface.

## In Progress

- Adding sorting functionality based on product category, product name, price, and date.
- The ultimate goal is to have the program running continuously in the cloud, automatically sending users a weekly email report detailing total weekly expenses and categorized expenses.

## Current Features

### Data Entry Fields

- "Category" Listbox: Allows users to select a category from a dropdown list.
- "Product" Field: Used to enter the name of the expense, e.g., fuel.
- "Price" Field: Used to enter the expense amount (only numeric input allowed).
- "Date" Field: Used to select the purchase date.

### Buttons

- "Add" Button: Adds the entered product to the table (requires filling all fields mentioned above).
- "Update" Button: Allows users to update a selected entry in the table (select the entry, make changes, then press the button).
- "Delete" Button: Removes the selected entry from the list.

## Setup and Usage

1. Create a new database (e.g., using the DB Browser for SQLite application).
2. In lines 56, 79, 103, and 128, set the path to the .db file that will store user data.
3. Make sure that required modules, such as tkinter and sqlite3, are installed in your environment.
4. To run the program, execute the main.py file.

## Note

I am currently focused on expanding my knowledge of Linux, which might lead to slower updates.

---

Your contribution is welcome! If you have any questions or suggestions, feel free to open an issue or submit a pull request.
