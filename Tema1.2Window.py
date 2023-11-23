import tkinter as tk

def get_user_details():

    username = user_text.get()
    passwd = pass_text.get()
    name = name_text.get()
    adress = adress_text.get()
    town = town_text.get()
    state = state_text.get()

    print(username, passwd, name, adress, town, state )

root = tk.Tk()
root.title('User management')
root.geometry('600x1000')
root.config(background='#3498DB')

user_label = tk.Label(root, text='Username' , font=('Cambria', 18), bg='blue')
user_label.pack(padx=10, pady=10)

user_text=tk.Entry(root, width=20)
user_text.pack(padx=10, pady=10)

pass_label = tk.Label(root, text='Password', font=('Cambria', 18), bg='blue')
pass_label.pack(padx=10, pady=10)

pass_text=tk.Entry(root, width=30, show='*')
pass_text.pack(padx=10, pady=10)

name_label = tk.Label(root, text='Name', font=('Cambria', 18), bg='blue')
name_label.pack(padx=10, pady=10)

name_text=tk.Entry(root, width=30, )
name_text.pack(padx=10, pady=10)

adress_label = tk.Label(root, text='Adresa', font=('Cambria', 18), bg='blue')
adress_label.pack(padx=10, pady=10)

adress_text=tk.Entry(root, width=30,)
adress_text.pack(padx=10, pady=10)

town_label = tk.Label(root, text='Oras', font=('Cambria', 18), bg='blue')
town_label.pack(padx=10, pady=10)

town_text=tk.Entry(root, width=30, )
town_text.pack(padx=10, pady=10)

state_label = tk.Label(root, text='Judet', font=('Cambria', 18), bg='blue')
state_label.pack(padx=10, pady=10)

state_text=tk.Entry(root, width=30, )
state_text.pack(padx=10, pady=10)

pin_label = tk.Label(root, text='cod PIN', font=('Cambria', 18), bg='blue')
pin_label.pack(padx=10, pady=10)

pin_text=tk.Entry(root, width=30, show='*')
pin_text.pack(padx=10, pady=10)


button = tk.Button(root,
                   text='Submit',
                   font=('Cambria', 16),
                   activebackground='blue',
                   activeforeground='yellow',
                   command=get_user_details
                   )
button.pack(pady=10)

root.mainloop()