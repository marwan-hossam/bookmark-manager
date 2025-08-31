#-------------------------------
#----Simple Bookmark Manager----
#-------------------------------

# Emty List to store bookmarks
bookmarks = []

# Maximum number of bookmarks
max_bookmarks = 5

while True:       # Loop keep running until user exits

    # Show menu
    print("\n-----Bookmark Manager-----")
    print("1. Add a new bookmark")
    print("2. View Bookmarks")
    print("3. Delete a bookmark")
    print("4. Exit")

    choice = input("Choose an option (1-4)")

    #---------------------ADD BOOKMARK--------------------
    if choice == "1":
        if len(bookmarks) < max_bookmarks:
            site = input("Enter website name (without https:)")
            bookmarks.append(f"https://{site.strip().lower()}")
            print("Bookmark added successfully.")
        else:
            print("Bookmarks list is full.")
    
    #--------------------VIEW BOOKMARK--------------------
    elif choice == "2":
        if len(bookmarks) > 0:
            bookmarks.sort()
            print("\nYour bookmarks:")
            for i, site in enumerate(bookmarks, start=1):
                print(f"{i}. {site}")
        else:
            print("No bookmarks to show.")

    #-------------------DELETE BOOKMARK-------------------
    elif choice == "3":
        if len(bookmarks) > 0:
            for i, site in enumerate(bookmarks, start=1):
                print(f"{i}. {site}")
            delete_index = int(input("Enter the number of bookmark to delete: "))
            if 1 <= delete_index <= len(bookmarks):
                removed = bookmarks.pop(delete_index - 1)
                print(f"{removed} has been removed.")
            else:
                print("⚠️ Invalid number!")
        else:
            print("⚠️ No bookmarks to delete.")

    #-----------------------EXIT--------------------------
    elif choice == "4":
        print("Exiting Bookmark Managaer\nGoodBye!")
        break

    else:
        print("Invalid Choice! Please choose between (1-4). ")

