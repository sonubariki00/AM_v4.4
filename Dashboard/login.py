import tkinter as tk
from tkinter import messagebox,ttk
import requests
import json
from admin_menu import AdminMenu
from employee_menu import EmployeeMenu

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Asset Management System")
        self.master.geometry("1024x768")
        self.master.configure(bg="#f0f0f0")

        # Main frame
        main_frame = tk.Frame(self.master, bg="#f0f0f0")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        title_label = tk.Label(main_frame, text="Asset Management System", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333333")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))

        # Admin Login Frame
        admin_frame = tk.Frame(main_frame, bg="#ffffff", bd=2, relief="raised", padx=20, pady=20)
        admin_frame.grid(row=1, column=0, padx=20, sticky="nsew")

        tk.Label(admin_frame, text="Admin Login", font=("Arial", 18, "bold"), bg="#ffffff", fg="#333333").pack(pady=(0, 10))
        
        tk.Label(admin_frame, text="Username:", bg="#ffffff", fg="#333333").pack(anchor="w")
        self.admin_username = ttk.Entry(admin_frame, width=30)
        self.admin_username.pack(pady=(0, 10), ipady=5)
        
        tk.Label(admin_frame, text="Password:", bg="#ffffff", fg="#333333").pack(anchor="w")
        self.admin_password = ttk.Entry(admin_frame, show="*", width=30)
        self.admin_password.pack(pady=(0, 20), ipady=5)
        
        admin_login_button = ttk.Button(admin_frame, text="Login", command=self.admin_login, style="AccentButton.TButton")
        admin_login_button.pack(pady=(0, 10), ipadx=10, ipady=5)

        # Employee Login Frame
        employee_frame = tk.Frame(main_frame, bg="#ffffff", bd=2, relief="raised", padx=20, pady=20)
        employee_frame.grid(row=1, column=1, padx=20, sticky="nsew")

        tk.Label(employee_frame, text="Employee Login", font=("Arial", 18, "bold"), bg="#ffffff", fg="#333333").pack(pady=(0, 10))
        
        tk.Label(employee_frame, text="Username:", bg="#ffffff", fg="#333333").pack(anchor="w")
        self.employee_username = ttk.Entry(employee_frame, width=30)
        self.employee_username.pack(pady=(0, 10), ipady=5)
        
        tk.Label(employee_frame, text="Password:", bg="#ffffff", fg="#333333").pack(anchor="w")
        self.employee_password = ttk.Entry(employee_frame, show="*", width=30)
        self.employee_password.pack(pady=(0, 20), ipady=5)
        
        employee_login_button = ttk.Button(employee_frame, text="Login", command=self.employee_login, style="AccentButton.TButton")
        employee_login_button.pack(pady=(0, 10), ipadx=10, ipady=5)

        # Configure styles
        style = ttk.Style()
        style.configure("AccentButton.TButton", background="#4CAF50", foreground="#ffffff")
        style.map("AccentButton.TButton", background=[("active", "#45a049")])
    def admin_login(self):
        username = self.admin_username.get()
        password = self.admin_password.get()

        response = requests.post("http://localhost:5000/api/login", json={"username": username, "password": password})
        if response.status_code == 200:
            response_data = response.json()
            user_id = response_data['user_id']
            self.master.withdraw()
            admin_menu_root = tk.Toplevel(self.master)
            _ =AdminMenu(admin_menu_root,user_id)
        else:
            messagebox.showerror("Invalid Credentials", "Invalid username or password or 401")

    def employee_login(self):
        username = self.employee_username.get()
        password = self.employee_password.get()


        response = requests.post("http://localhost:5000/api/login", json={"username": username, "password": password})
        if response.status_code == 200:
            response_data = response.json()
            user_id = response_data['user_id']
            self.master.withdraw()
            employee_menu_root = tk.Toplevel(self.master)
            _ = EmployeeMenu(employee_menu_root,user_id)
        else:
            messagebox.showerror("Invalid Credentials", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()

