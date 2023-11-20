import tkinter as tk

def get_user_details():

    username = user_text.get()
    passwd = pass_text.get()
    print(username, passwd)

root = tk.Tk()
root.title('User management')
root.geometry('600x400')
root.config(background='#3498DB')

user_label = tk.Label(root, text='Username' , font=('Cambria', 18), bg='blue')
user_label.pack(padx=10, pady=10)

user_text=tk.Entry(root, width=20)
user_text.pack(padx=10, pady=10)

pass_label = tk.Label(root, text='Password', font=('Cambria', 18), bg='blue')
pass_label.pack(padx=10, pady=10)

pass_text=tk.Entry(root, width=30, show='*')
pass_text.pack(padx=10, pady=10)

button = tk.Button(root,
                   text='Submit',
                   font=('Cambria', 16),
                   activebackground='blue',
                   activeforeground='yellow',
                   command=get_user_details
                   )
button.pack(pady=10)

root.mainloop()


