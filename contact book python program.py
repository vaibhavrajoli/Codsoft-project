import tkinter as tk
from tkinter import messagebox
class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("1000x600")
        self.header_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.header_frame.pack(fill="x")
        self.content_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.content_frame.pack(fill="both", expand=True)
        self.header_label = tk.Label(self.header_frame, text="Contact Book", font=("Times new roman", 24), fg="#FF0000")
        self.header_label.pack(pady=10)
        self.contacts_listbox = tk.Listbox(self.content_frame, width=40, height=15)
        self.contacts_listbox.pack(side=tk.LEFT, fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self.content_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.contacts_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contacts_listbox.yview)
        self.entry_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        self.entry_frame.pack(side=tk.LEFT, fill="x")
        self.name_label = tk.Label(self.entry_frame, text="Name:", font=("Times new roman", 14))
        self.name_label.pack()
        self.name_entry = tk.Entry(self.entry_frame, width=30)
        self.name_entry.pack()
        self.phone_label = tk.Label(self.entry_frame, text="Phone:", font=("Times new roman", 14))
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.entry_frame, width=30)
        self.phone_entry.pack()
        self.email_label = tk.Label(self.entry_frame, text="Email:", font=("Times new roman", 14))
        self.email_label.pack()
        self.email_entry = tk.Entry(self.entry_frame, width=30)
        self.email_entry.pack()
        self.address_label = tk.Label(self.entry_frame, text="Address:", font=("Times new roman", 14))
        self.address_label.pack()
        self.address_entry = tk.Entry(self.entry_frame, width=30)
        self.address_entry.pack()
        self.button_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        self.button_frame.pack(side=tk.LEFT, fill="x")
        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.pack(side=tk.LEFT, padx=5)
        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(side=tk.LEFT, padx=5)
        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(self.button_frame, width=20)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = tk.Button(self.button_frame, text="Search", command=self.search_contact)
        self.search_button.pack(side=tk.LEFT, padx=5)
        self.contacts = []
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.contacts_listbox.insert(tk.END, f"{name} - {phone}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter name and phone number")
    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            if name and phone:
                self.contacts[selected_index[0]] = {"name": name, "phone": phone, "email": email, "address": address}
                self.contacts_listbox.delete(selected_index[0])
                self.contacts_listbox.insert(selected_index[0], f"{name} - {phone}")
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.address_entry.delete(0, tk.END)
            else:
                 messagebox.showerror("Error", "Please enter name and phone number")
        else:
            messagebox.showerror("Error", "Please select a contact to update")
    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            self.contacts_listbox.delete(selected_index[0])
            del self.contacts[selected_index[0]]
        else:
            messagebox.showerror("Error", "Please select a contact to delete")
    def search_contact(self):
        search_term = self.search_entry.get()
        if search_term:
            self.contacts_listbox.delete(0, tk.END)
            for contact in self.contacts:
                if search_term in contact["name"] or search_term in contact["phone"]:
                    self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    app.run()