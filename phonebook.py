'''
Create an app that acts like a phonebook:

A user can:
Add a name and phone number 
List all of the names and phone numbers in the phonebook
Look up a phone number by the person's name
Remove a person from the phonebook

tips:
Plan out how to write/structure this code in english
Think of what data structure to use for storing the name and phone number of the phonebook
use functions to break up the tasks, does the function take a parameter? Does the function return something? 
If so,What does the function return?
'''


def phonebook_loop():
	contact_entries = []
	while True:
		command = raw_input("Please choose one of the following commands:\na Add an entry\nl List entries\nf Find an entry\nr Remove an entry.\n")
		# print command
		if command == "a":
			contact_entries.append(add_contact())
		elif command == "l":
			list_contacts(contact_entries)
		elif command == "r":
			remove_contact(contact_entries)
		elif command =="f":
			find_contact(contact_entries)

def add_contact():
	name = raw_input("Enter contact name")
	phone = raw_input("Enter contact number")
	return {"Name" : name, "Phone": phone}

def list_contacts(contacts):
	for entry in contacts:
		print entry
		 
def remove_contact(contacts):
	for entry in contacts:
		print entry['Name']
	remove_contact = raw_input("Choose a contact to remove.")
	for key, value in enumerate(contacts):
		if value['Name'] == remove_contact:
			contacts.pop(key)

def find_contact(contacts):
	contact_entry = raw_input("Choose a contact to find")
	for key, value in enumerate(contacts):
			if value['Name'] == contact_entry:
				print value



phonebook_loop()



