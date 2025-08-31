# Simple Bookmark Manager

A beginner-friendly Python project where you can **add, view, and delete bookmarks**.  
This project helped me practice Python basics like **loops, lists, conditions, and user input**.

## Features
- ➕ Add new bookmarks (up to 5).
- 📋 View all bookmarks in a sorted list.
- ❌ Delete bookmarks by choosing their number.
- 🔁 Menu keeps running until you choose "Exit".

## How It Works
1. Run the script.
2. Choose an option from the menu:
   - **1** → Add a bookmark  
   - **2** → View bookmarks  
   - **3** → Delete a bookmark  
   - **4** → Exit program
3. Follow the instructions on screen.

## Example Output

-----Bookmark Manager-----

1. Add a new bookmark
2. View Bookmarks
3. Delete a bookmark
4. Exit
Choose an option (1-4) 1
Enter website name (without https:) google.com
Bookmark added successfully.


---

## Code
```python
# Simple Bookmark Manager
bookmarks = []
max_bookmarks = 5

while True:
    print("\n-----Bookmark Manager-----")
    print("1. Add a new bookmark")
    print("2. View Bookmarks")
    print("3. Delete a bookmark")
    print("4. Exit")

    choice = input("Choose an option (1-4)")

    if choice == "1":
        if len(bookmarks) < max_bookmarks:
            site = input("Enter website name (without https:)")
            bookmarks.append(f"https://{site.strip().lower()}")
            print("Bookmark added successfully.")
        else:
            print("Bookmarks list is full.")

    elif choice == "2":
        if len(bookmarks) > 0:
            bookmarks.sort()
            print("\nYour bookmarks:")
            for i, site in enumerate(bookmarks, start=1):
                print(f"{i}. {site}")
        else:
            print("No bookmarks to show.")

    elif choice == "3":
        if len(bookmarks) > 0:
            for i, site in enumerate(bookmarks, start=1):
                print(f"{i}. {site}")
            delete_index = int(input("Enter the number of bookmark to delete: "))
            if 1 <= delete_index <= len(bookmarks):
                removed = bookmarks.pop(delete_index - 1)
                print(f"{removed} has been removed.")
            else:
                print("Invalid number!")
        else:
            print("No bookmarks to delete.")

    elif choice == "4":
        print("Exiting Bookmark Manager\nGoodBye!")
        break

    else:
        print("Invalid Choice! Please choose between (1-4).")

Learning Goals:
==> Practice using while loops and for loops.
==> Learn how to work with lists in Python.
==> Understand how to handle user input and simple validation.
==> Organize code with conditions (if/else).

How to Run:
1. Clone the repository:
git clone https://github.com/YourUsername/Bookmark-Manager.git

2. Open the folder:
cd Bookmark-Manager

3. Run the script:
python bookmark_manager.py
