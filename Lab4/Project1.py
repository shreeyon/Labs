import os 
CONTACTS_FILE = "contacts.txt" 
def display_menu(): 
   print("\nContact Book Menu:") 
   print("1. Add a new contact") 
   print("2. View all contacts") 
   print("3. Search for a contact") 
   print("4. Exit") 
def add_contact(): 
   name = input("Enter contact name: ").strip() 
   phone = input("Enter contact phone number: ").strip() 
   if not name or not phone: 
       print("Error: Name and phone number cannot be empty!") 
       return 
   try: 
       with open(CONTACTS_FILE, "a") as file: 
           file.write(f"{name},{phone}\n") 
       print(f"Contact '{name}' added successfully!") 
   except IOError as e: 
       print(f"Error writing to file: {e}") 
def view_contacts(): 
   try: 
       if not os.path.exists(CONTACTS_FILE): 
           print("No contacts found. The contact book is empty.") 
           return 
       with open(CONTACTS_FILE, "r") as file: 
           contacts = file.readlines() 
       if not contacts: 
           print("No contacts found. The contact book is empty.") 
           return 
       print("\nAll Contacts:") 
       print("-------------") 
       for i, contact in enumerate(contacts, 1): 
           name, phone = contact.strip().split(",") 
           print(f"{i}. {name}: {phone}") 
   except IOError as e: 
       print(f"Error reading file: {e}") 
def search_contact(): 
   search_term = input("Enter name or phone number to search: ").strip().lower() 
   if not search_term: 
       print("Error: Search term cannot be empty!") 
       return 
   try: 
       if not os.path.exists(CONTACTS_FILE): 
           print("No contacts found. The contact book is empty.") 
           return 
       with open(CONTACTS_FILE, "r") as file: 
           contacts = file.readlines() 
       found_contacts = [] 
       for contact in contacts: 
           name, phone = contact.strip().split(",") 
           if search_term in name.lower() or search_term in phone: 
               found_contacts.append((name, phone)) 
       if not found_contacts: 
           print("No matching contacts found.") 
       else: 
           print("\nSearch Results:") 
           print("--------------") 
           for i, (name, phone) in enumerate(found_contacts, 1): 
               print(f"{i}. {name}: {phone}") 
   except IOError as e: 
       print(f"Error reading file: {e}") 
def main(): 
   print("Welcome to the Contact Book!") 
   while True: 
       display_menu() 
       choice = input("Enter your choice (1-4): ").strip() 
       if choice == "1": 
           add_contact() 
       elif choice == "2": 
           view_contacts() 
       elif choice == "3": 
           search_contact() 
       elif choice == "4": 
           print("Goodbye!") 
           break 
       else: 
           print("Invalid choice. Please enter a number between 1 and 4.") 
if __name__ == "__main__": 
   main()


  