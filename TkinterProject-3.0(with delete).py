import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def sec():
    # Create a secondary window
    sec_window = tk.Toplevel(background="lightblue4")
    sec_window.title("Sec Window")

    # Create two Frames: top for inputs, bottom for buttons
    top_frame = tk.Frame(sec_window, background="lightblue4")
    bottom_frame = tk.Frame(sec_window, background="lightblue4")

    # Labels and Entry fields for top Frame
    name_label = tk.Label(top_frame, text="Name", background="lightblue4")
    name_entry = tk.Entry(top_frame, width=40)
    tel_label = tk.Label(top_frame, text="Tel", background="lightblue4")
    tel_entry = tk.Entry(top_frame, width=40)
    mobile_label = tk.Label(top_frame, text="Mobile", background="lightblue4")
    mobile_entry = tk.Entry(top_frame, width=40)
    email_label = tk.Label(top_frame, text="Email", background="lightblue4")
    email_entry = tk.Entry(top_frame, width=40)

    # Grid layout for top Frame Labels and Entry fields
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    tel_label.grid(row=1, column=0, padx=5, pady=5)
    tel_entry.grid(row=1, column=1, padx=5, pady=5)
    mobile_label.grid(row=2, column=0, padx=5, pady=5)
    mobile_entry.grid(row=2, column=1, padx=5, pady=5)
    email_label.grid(row=3, column=0, padx=5, pady=5)
    email_entry.grid(row=3, column=1, padx=5, pady=5)

    # Frame Pack
    top_frame.pack(padx=40, pady=20)
    bottom_frame.pack(padx=40, pady=20)

    # Function to insert data into the listbox
    def insert():
        data = f"Name: {name_entry.get()}, Tel: {tel_entry.get()}, Mobile: {mobile_entry.get()}, Email: {email_entry.get()}"
        listbox.insert(tk.END, data)

    # Buttons for the bottom frame
    exit_bt = tk.Button(bottom_frame, text="Exit", command=sec_window.destroy)
    add_bt = tk.Button(bottom_frame, text="Add", command=insert)

    # Grid layout for Buttons
    exit_bt.grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=4)
    add_bt.grid(row=0, column=1, padx=5, pady=5, ipadx=10, ipady=4)


temp_data = None
temp_pos = None


def delete():
    global temp_data
    global temp_pos
    temp_data = listbox.get(tk.ACTIVE)
    temp_pos = listbox.curselection()
    listbox.delete(tk.ACTIVE)


def undo_delete():
    global temp_data
    global temp_pos
    listbox.insert(temp_pos, temp_data)


def search():
    # Create a search window
    search_window = tk.Toplevel(background="lightblue4")
    search_window.title("Search Window")

    # Frame for input and button
    search_frame = tk.Frame(search_window,background="lightblue4")
    search_frame.pack(padx=10, pady=10)

    # Label and Entry field for search
    search_label = tk.Label(search_frame, text="Name", background="lightblue4")
    search_entry = tk.Entry(search_frame, width=20)
    search_label.grid(row=0, column=0, padx=5, pady=5)
    search_entry.grid(row=0, column=1, padx=5, pady=5)

    def perform_search():
        search_name = search_entry.get()
        found = False
        for idx in range(listbox.size()):
            item = listbox.get(idx)
            if search_name.lower() in item.lower():
                listbox.selection_clear(0, tk.END)
                listbox.selection_set(idx)
                listbox.activate(idx)
                found = True
                break
        if not found:
            messagebox.showinfo("Search Result", f"No match found for '{search_name}'")

    # Search and Exit buttons
    search_bt = tk.Button(search_frame, text="Search", command=perform_search)
    exit_bt = tk.Button(search_frame, text="Exit", command=search_window.destroy)
    search_bt.grid(row=1, column=0, pady=5, ipadx=8)
    exit_bt.grid(row=1, column=1, pady=5, ipadx=10)


# Function to sort the listbox
def sort_listbox():
    # Get all items from the listbox
    items = listbox.get(0, tk.END)
    # Sort the items
    sorted_items = sorted(items)
    # Delete all items in the listbox
    listbox.delete(0, tk.END)
    # Insert sorted items back into the listbox
    for item in sorted_items:
        listbox.insert(tk.END, item)


# Function to save the listbox contents to a file
def save_list():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            for item in listbox.get(0, tk.END):
                file.write(f"{item}\n")
        messagebox.showinfo("Save List", "List saved successfully!")


# Function to load the listbox contents from a file
def load_list():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            listbox.delete(0, tk.END)
            for line in lines:
                listbox.insert(tk.END, line.strip())
        messagebox.showinfo("Load List", "List loaded successfully!",)

# Main window setup
Main_window = tk.Tk()
Main_window.configure(background="lightblue3")
Main_window.title("Phone Notebook")

# Frames
top_frame = tk.Frame(Main_window, background="lightblue3")
right_frame = tk.Frame(Main_window, background="lightblue3")
left_frame = tk.Frame(Main_window, background="lightblue3")
buttom_frame = tk.Frame(Main_window, background="lightblue3")

# Grid for Frames
top_frame.grid(row=0, column=0)
left_frame.grid(row=1, column=0)
right_frame.grid(row=1, column=1)
buttom_frame.grid(row=2, column=0)


# Listbox in the Main window
listbox = tk.Listbox(left_frame, width=120, background="lightblue1")
listbox.pack(padx=20)

# Buttons in the right frame
insert_bt = tk.Button(right_frame, text="Insert", command=sec)
delete_bt = tk.Button(right_frame,text="Delete", command=delete)
undo_bt = tk.Button(right_frame,text="Undo", command=undo_delete)
sort_bt = tk.Button(right_frame, text="Sort", command=sort_listbox)
search_bt = tk.Button(right_frame, text="Search", command=search)
save_bt = tk.Button(buttom_frame, text="Save", command=save_list)
load_bt = tk.Button(buttom_frame, text="Load", command=load_list)
exit_bt = tk.Button(right_frame, text="Exit", command=Main_window.destroy)

# Pack buttons in the right frame vertically
insert_bt.pack(pady=5, ipadx=22)
delete_bt.pack(pady=5, ipadx=22)
undo_bt.pack(pady=5, ipadx=22)
sort_bt.pack(pady=5, ipadx=27)
search_bt.pack(pady=5, ipadx=22)
exit_bt.pack(pady=5, ipadx=28)

# Grid for S/L button
save_bt.grid(row=0, column=0, ipadx=30, pady=10, padx=5)
load_bt.grid(row=0, column=1, ipadx=30, pady=10, padx=5)

# Start the main loop
Main_window.mainloop()
