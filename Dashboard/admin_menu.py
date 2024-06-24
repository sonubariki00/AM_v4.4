# # # # import tkinter as tk
# # # # from tkinter import messagebox, ttk
# # # # from log_view_dashboard import LogViewDashboard
# # # # import requests

# # # # class AdminMenu:
# # # #     def __init__(self, master, username):
# # # #         self.master = master
# # # #         self.username = username
# # # #         self.master.title("Admin Dashboard")
# # # #         self.master.geometry("1200x800")
# # # #         self.master.configure(bg="#f0f0f0")
# # # #         self.master.state('zoomed')

# # # #         # Main frame
# # # #         main_frame = tk.Frame(self.master, bg="#f0f0f0")
# # # #         main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# # # #         # Header
# # # #         header_frame = tk.Frame(main_frame, bg="#4a4a4a")
# # # #         header_frame.pack(fill=tk.X, pady=(0, 20))

# # # #         tk.Label(header_frame, text="Admin Dashboard", font=("Arial", 24, "bold"), bg="#4a4a4a", fg="white").pack(side=tk.LEFT, padx=20, pady=10)
# # # #         tk.Label(header_frame, text=f"Welcome, {username}", font=("Arial", 14), bg="#4a4a4a", fg="white").pack(side=tk.RIGHT, padx=20, pady=10)

# # # #         # Content frame
# # # #         content_frame = tk.Frame(main_frame, bg="#f0f0f0")
# # # #         content_frame.pack(fill=tk.BOTH, expand=True)

# # # #         # Grid configuration
# # # #         content_frame.grid_rowconfigure(0, weight=1)
# # # #         content_frame.grid_columnconfigure(0, weight=1)
# # # #         content_frame.grid_columnconfigure(1, weight=1)

# # # #         # Asset Management Frame
# # # #         asset_frame = ttk.LabelFrame(content_frame, text="Asset Management", padding=15)
# # # #         asset_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# # # #         ttk.Label(asset_frame, text="Asset Name:").grid(row=0, column=0, sticky="w", pady=5)
# # # #         self.asset_name = ttk.Entry(asset_frame, width=30)
# # # #         self.asset_name.grid(row=0, column=1, pady=5)

# # # #         ttk.Button(asset_frame, text="Add Asset", command=self.add_asset).grid(row=2, column=0, columnspan=2, pady=10)
# # # #         ttk.Button(asset_frame, text="Remove Asset", command=self.remove_asset).grid(row=3, column=0, columnspan=2, pady=10)

# # # #         # Employee Management Frame
# # # #         employee_frame = ttk.LabelFrame(content_frame, text="Employee Management", padding=15)
# # # #         employee_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# # # #         ttk.Label(employee_frame, text="Employee Name:").grid(row=0, column=0, sticky="w", pady=5)
# # # #         self.employee_name = ttk.Entry(employee_frame, width=30)
# # # #         self.employee_name.grid(row=0, column=1, pady=5)

# # # #         ttk.Label(employee_frame, text="Employee ID:").grid(row=1, column=0, sticky="w", pady=5)
# # # #         self.employee_id = ttk.Entry(employee_frame, width=30)
# # # #         self.employee_id.grid(row=1, column=1, pady=5)

# # # #         ttk.Button(employee_frame, text="Add Employee", command=self.add_employee).grid(row=2, column=0, columnspan=2, pady=10)
# # # #         ttk.Button(employee_frame, text="Remove Employee", command=self.remove_employee).grid(row=3, column=0, columnspan=2, pady=10)

# # # #         # Requests Frame
# # # #         requests_frame = ttk.LabelFrame(content_frame, text="Requests", padding=15)
# # # #         requests_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# # # #         self.requests_tree = ttk.Treeview(requests_frame, columns=("Request ID", "Employee ID", "Asset ID", "Status", "Type", "Request Date"), show="headings")
# # # #         self.requests_tree.heading("Request ID", text="Request ID")
# # # #         self.requests_tree.heading("Employee ID", text="Employee ID")
# # # #         self.requests_tree.heading("Asset ID", text="Asset ID")
# # # #         self.requests_tree.heading("Status", text="Status")
# # # #         self.requests_tree.heading("Type", text="Type")
# # # #         self.requests_tree.heading("Request Date", text="Request Date")
# # # #         self.requests_tree.pack(fill=tk.BOTH, expand=True)

# # # #         ttk.Button(requests_frame, text="View Requests", command=self.view_requests).pack(pady=10)

# # # #         # Log View Button
# # # #         ttk.Button(main_frame, text="View Logs", command=self.view_logs).pack(pady=10)

# # # #         # Logout Button
# # # #         ttk.Button(main_frame, text="Logout", command=self.logout).pack(pady=10)

# # # #     def add_asset(self):
# # # #         asset_name = self.asset_name.get()
# # # #         if not asset_name:
# # # #             messagebox.showerror("Error", "Asset name cannot be empty")
# # # #             return
# # # #         try:
# # # #             response = requests.post("http://localhost:5000/api/admin/add_asset", json={"asset_name": asset_name})
# # # #             if response.status_code == 200:
# # # #                 messagebox.showinfo("Add Asset", f"Asset '{asset_name}' added successfully!")
# # # #             else:
# # # #                 messagebox.showerror("Error", "Failed to add asset")
# # # #         except requests.RequestException:
# # # #             messagebox.showerror("Error", "Failed to connect to server")

# # # #     def remove_asset(self):
# # # #         asset_name = self.asset_name.get()
# # # #         if not asset_name:
# # # #             messagebox.showerror("Error", "Asset name cannot be empty")
# # # #             return
# # # #         try:
# # # #             response = requests.post("http://localhost:5000/api/admin/remove_asset", json={"asset_name": asset_name})
# # # #             if response.status_code == 200:
# # # #                 messagebox.showinfo("Remove Asset", f"Asset '{asset_name}' removed successfully!")
# # # #             else:
# # # #                 messagebox.showerror("Error", "Failed to remove asset")
# # # #         except requests.RequestException:
# # # #             messagebox.showerror("Error", "Failed to connect to server")

# # # #     def add_employee(self):
# # # #         employee_name = self.employee_name.get()
# # # #         employee_id = self.employee_id.get()
# # # #         if not employee_name or not employee_id:
# # # #             messagebox.showerror("Error", "Employee name and ID cannot be empty")
# # # #             return
# # # #         try:
# # # #             response = requests.post("http://localhost:5000/api/admin/add_employee", json={"employee_name": employee_name, "employee_id": employee_id})
# # # #             if response.status_code == 200:
# # # #                 messagebox.showinfo("Add Employee", f"Employee '{employee_name}' added successfully!")
# # # #             else:
# # # #                 messagebox.showerror("Error", "Failed to add employee")
# # # #         except requests.RequestException:
# # # #             messagebox.showerror("Error", "Failed to connect to server")

# # # #     def remove_employee(self):
# # # #         employee_name = self.employee_name.get()
# # # #         employee_id = self.employee_id.get()
# # # #         if not employee_name or not employee_id:
# # # #             messagebox.showerror("Error", "Employee name and ID cannot be empty")
# # # #             return
# # # #         try:
# # # #             response = requests.post("http://localhost:5000/api/admin/remove_employee", json={"employee_name": employee_name, "employee_id": employee_id})
# # # #             if response.status_code == 200:
# # # #                 messagebox.showinfo("Remove Employee", f"Employee '{employee_name}' removed successfully!")
# # # #             else:
# # # #                 messagebox.showerror("Error", "Failed to remove employee")
# # # #         except requests.RequestException:
# # # #             messagebox.showerror("Error", "Failed to connect to server")

# # # #     def view_requests(self):
# # # #         try:
# # # #             response = requests.get("http://localhost:5000/api/admin/view_requests")
# # # #             if response.status_code == 200:
# # # #                 requests_data = response.json().get('requests', [])
# # # #                 for item in self.requests_tree.get_children():
# # # #                     self.requests_tree.delete(item)
# # # #                 for req in requests_data:
# # # #                     self.requests_tree.insert("", "end", values=(
# # # #                         req["Request ID"],
# # # #                         req["Employee ID"],
# # # #                         req["Asset ID"],
# # # #                         req["Status"],
# # # #                         req["Type"],
# # # #                         req["Request Date"]
# # # #                     ))
# # # #             else:
# # # #                 messagebox.showerror("Error", "Failed to retrieve requests")
# # # #         except requests.RequestException:
# # # #             messagebox.showerror("Error", "Failed to connect to server")

# # # #     def view_logs(self):
# # # #         self.master.withdraw()
# # # #         log_view_root = tk.Toplevel(self.master)
# # # #         LogViewDashboard(log_view_root)

# # # #     def logout(self):
# # # #         self.master.destroy()

# # # # if __name__ == "__main__":
# # # #     root = tk.Tk()
# # # #     app = AdminMenu(root, "Admin")
# # # #     root.mainloop()

# # # import tkinter as tk
# # # from tkinter import messagebox, ttk
# # # from log_view_dashboard import LogViewDashboard
# # # import requests

# # # class AdminMenu:
# # #     def __init__(self, master, username):
# # #         self.master = master
# # #         self.username = username
# # #         self.master.title("Admin Dashboard")
# # #         self.master.geometry("1200x800")
# # #         self.master.configure(bg="#f0f0f0")
# # #         self.master.state('zoomed')

# # #         # Main frame
# # #         main_frame = tk.Frame(self.master, bg="#f0f0f0")
# # #         main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# # #         # Header
# # #         header_frame = tk.Frame(main_frame, bg="#4a4a4a")
# # #         header_frame.pack(fill=tk.X, pady=(0, 20))

# # #         tk.Label(header_frame, text="Admin Dashboard", font=("Arial", 24, "bold"), bg="#4a4a4a", fg="white").pack(side=tk.LEFT, padx=20, pady=10)
# # #         tk.Label(header_frame, text=f"Welcome, {username}", font=("Arial", 14), bg="#4a4a4a", fg="white").pack(side=tk.RIGHT, padx=20, pady=10)

# # #         # Content frame
# # #         content_frame = tk.Frame(main_frame, bg="#f0f0f0")
# # #         content_frame.pack(fill=tk.BOTH, expand=True)

# # #         # Grid configuration
# # #         content_frame.grid_rowconfigure(0, weight=1)
# # #         content_frame.grid_columnconfigure(0, weight=1)
# # #         content_frame.grid_columnconfigure(1, weight=1)

# # #         # Asset Management Frame
# # #         asset_frame = ttk.LabelFrame(content_frame, text="Asset Management", padding=15)
# # #         asset_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# # #         ttk.Label(asset_frame, text="Asset Name:").grid(row=0, column=0, sticky="w", pady=5)
# # #         self.asset_name = ttk.Entry(asset_frame, width=30)
# # #         self.asset_name.grid(row=0, column=1, pady=5)

# # #         ttk.Button(asset_frame, text="Add Asset", command=self.add_asset).grid(row=2, column=0, columnspan=2, pady=10)
# # #         ttk.Button(asset_frame, text="Remove Asset", command=self.remove_asset).grid(row=3, column=0, columnspan=2, pady=10)

# # #         # Employee Management Frame
# # #         employee_frame = ttk.LabelFrame(content_frame, text="Employee Management", padding=15)
# # #         employee_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# # #         ttk.Label(employee_frame, text="Employee Name:").grid(row=0, column=0, sticky="w", pady=5)
# # #         self.employee_name = ttk.Entry(employee_frame, width=30)
# # #         self.employee_name.grid(row=0, column=1, pady=5)

# # #         ttk.Label(employee_frame, text="Employee ID:").grid(row=1, column=0, sticky="w", pady=5)
# # #         self.employee_id = ttk.Entry(employee_frame, width=30)
# # #         self.employee_id.grid(row=1, column=1, pady=5)

# # #         ttk.Button(employee_frame, text="Add Employee", command=self.add_employee).grid(row=2, column=0, columnspan=2, pady=10)
# # #         ttk.Button(employee_frame, text="Remove Employee", command=self.remove_employee).grid(row=3, column=0, columnspan=2, pady=10)

# # #         # Requests Frame
# # #         requests_frame = ttk.LabelFrame(content_frame, text="Requests", padding=15)
# # #         requests_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# # #         self.requests_tree = ttk.Treeview(requests_frame, columns=("Request ID", "Employee ID", "Asset ID", "Status", "Type", "Request Date"), show="headings")
# # #         self.requests_tree.heading("Request ID", text="Request ID")
# # #         self.requests_tree.heading("Employee ID", text="Employee ID")
# # #         self.requests_tree.heading("Asset ID", text="Asset ID")
# # #         self.requests_tree.heading("Status", text="Status")
# # #         self.requests_tree.heading("Type", text="Type")
# # #         self.requests_tree.heading("Request Date", text="Request Date")
# # #         self.requests_tree.pack(fill=tk.BOTH, expand=True)

# # #         ttk.Button(requests_frame, text="View Requests", command=self.view_requests).pack(pady=10)

# # #         # Button Frame for additional buttons
# # #         button_frame = tk.Frame(main_frame, bg="#f0f0f0")
# # #         button_frame.pack(fill=tk.X, pady=10)

# # #         # Log View Button
# # #         ttk.Button(button_frame, text="View Logs", command=self.view_logs).pack(side=tk.LEFT, padx=10)

# # #         # Logout Button
# # #         ttk.Button(button_frame, text="Logout", command=self.logout).pack(side=tk.RIGHT, padx=10)

# # #     def add_asset(self):
# # #         asset_name = self.asset_name.get()
# # #         if not asset_name:
# # #             messagebox.showerror("Error", "Asset name cannot be empty")
# # #             return
# # #         try:
# # #             response = requests.post("http://localhost:5000/api/admin/add_asset", json={"asset_name": asset_name})
# # #             if response.status_code == 200:
# # #                 messagebox.showinfo("Add Asset", f"Asset '{asset_name}' added successfully!")
# # #             else:
# # #                 messagebox.showerror("Error", "Failed to add asset")
# # #         except requests.RequestException:
# # #             messagebox.showerror("Error", "Failed to connect to server")

# # #     def remove_asset(self):
# # #         asset_name = self.asset_name.get()
# # #         if not asset_name:
# # #             messagebox.showerror("Error", "Asset name cannot be empty")
# # #             return
# # #         try:
# # #             response = requests.post("http://localhost:5000/api/admin/remove_asset", json={"asset_name": asset_name})
# # #             if response.status_code == 200:
# # #                 messagebox.showinfo("Remove Asset", f"Asset '{asset_name}' removed successfully!")
# # #             else:
# # #                 messagebox.showerror("Error", "Failed to remove asset")
# # #         except requests.RequestException:
# # #             messagebox.showerror("Error", "Failed to connect to server")

# # #     def add_employee(self):
# # #         employee_name = self.employee_name.get()
# # #         employee_id = self.employee_id.get()
# # #         if not employee_name or not employee_id:
# # #             messagebox.showerror("Error", "Employee name and ID cannot be empty")
# # #             return
# # #         try:
# # #             response = requests.post("http://localhost:5000/api/admin/add_employee", json={"employee_name": employee_name, "employee_id": employee_id})
# # #             if response.status_code == 200:
# # #                 messagebox.showinfo("Add Employee", f"Employee '{employee_name}' added successfully!")
# # #             else:
# # #                 messagebox.showerror("Error", "Failed to add employee")
# # #         except requests.RequestException:
# # #             messagebox.showerror("Error", "Failed to connect to server")

# # #     def remove_employee(self):
# # #         employee_name = self.employee_name.get()
# # #         employee_id = self.employee_id.get()
# # #         if not employee_name or not employee_id:
# # #             messagebox.showerror("Error", "Employee name and ID cannot be empty")
# # #             return
# # #         try:
# # #             response = requests.post("http://localhost:5000/api/admin/remove_employee", json={"employee_name": employee_name, "employee_id": employee_id})
# # #             if response.status_code == 200:
# # #                 messagebox.showinfo("Remove Employee", f"Employee '{employee_name}' removed successfully!")
# # #             else:
# # #                 messagebox.showerror("Error", "Failed to remove employee")
# # #         except requests.RequestException:
# # #             messagebox.showerror("Error", "Failed to connect to server")

# # #     def view_requests(self):
# # #         try:
# # #             response = requests.get("http://localhost:5000/api/admin/view_requests")
# # #             if response.status_code == 200:
# # #                 requests_data = response.json().get('requests', [])
# # #                 for item in self.requests_tree.get_children():
# # #                     self.requests_tree.delete(item)
# # #                 for req in requests_data:
# # #                     self.requests_tree.insert("", "end", values=(
# # #                         req["Request ID"],
# # #                         req["Employee ID"],
# # #                         req["Asset ID"],
# # #                         req["Status"],
# # #                         req["Type"],
# # #                         req["Request Date"]
# # #                     ))
# # #             else:
# # #                 messagebox.showerror("Error", "Failed to retrieve requests")
# # #         except requests.RequestException:
# # #             messagebox.showerror("Error", "Failed to connect to server")

# # #     def view_logs(self):
# # #         self.master.withdraw()
# # #         log_view_root = tk.Toplevel(self.master)
# # #         LogViewDashboard(log_view_root)

# # #     def logout(self):
# # #         self.master.destroy()

# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = AdminMenu(root, "Admin")
# # #     root.mainloop()
# # import tkinter as tk
# # from tkinter import messagebox, ttk
# # from log_view_dashboard import LogViewDashboard
# # import requests

# # class AdminMenu:
# #     def __init__(self, master, username):
# #         self.master = master
# #         self.username = username
# #         self.master.title("Admin Dashboard")
# #         self.master.geometry("1200x800")
# #         self.master.configure(bg="#f0f0f0")
# #         self.master.state('zoomed')

# #         # Main frame
# #         main_frame = tk.Frame(self.master, bg="#f0f0f0")
# #         main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# #         # Header
# #         header_frame = tk.Frame(main_frame, bg="#4a4a4a")
# #         header_frame.pack(fill=tk.X, pady=(0, 20))

# #         tk.Label(header_frame, text="Admin Dashboard", font=("Arial", 24, "bold"), bg="#4a4a4a", fg="white").pack(side=tk.LEFT, padx=20, pady=10)
# #         tk.Label(header_frame, text=f"Welcome, {username}", font=("Arial", 14), bg="#4a4a4a", fg="white").pack(side=tk.RIGHT, padx=20, pady=10)

# #         # Content frame
# #         content_frame = tk.Frame(main_frame, bg="#f0f0f0", height=600)
# #         content_frame.pack(fill=tk.X, expand=False)

# #         # Grid configuration
# #         content_frame.grid_rowconfigure(0, weight=1)
# #         content_frame.grid_columnconfigure(0, weight=1)
# #         content_frame.grid_columnconfigure(1, weight=1)

# #         # Asset Management Frame
# #         asset_frame = ttk.LabelFrame(content_frame, text="Asset Management", padding=15)
# #         asset_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# #         ttk.Label(asset_frame, text="Asset Name:").grid(row=0, column=0, sticky="w", pady=5)
# #         self.asset_name = ttk.Entry(asset_frame, width=30)
# #         self.asset_name.grid(row=0, column=1, pady=5)

# #         ttk.Button(asset_frame, text="Add Asset", command=self.add_asset).grid(row=2, column=0, columnspan=2, pady=10)
# #         ttk.Button(asset_frame, text="Remove Asset", command=self.remove_asset).grid(row=3, column=0, columnspan=2, pady=10)

# #         # Employee Management Frame
# #         employee_frame = ttk.LabelFrame(content_frame, text="Employee Management", padding=15)
# #         employee_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# #         ttk.Label(employee_frame, text="Employee Name:").grid(row=0, column=0, sticky="w", pady=5)
# #         self.employee_name = ttk.Entry(employee_frame, width=30)
# #         self.employee_name.grid(row=0, column=1, pady=5)

# #         ttk.Label(employee_frame, text="Employee ID:").grid(row=1, column=0, sticky="w", pady=5)
# #         self.employee_id = ttk.Entry(employee_frame, width=30)
# #         self.employee_id.grid(row=1, column=1, pady=5)

# #         ttk.Button(employee_frame, text="Add Employee", command=self.add_employee).grid(row=2, column=0, columnspan=2, pady=10)
# #         ttk.Button(employee_frame, text="Remove Employee", command=self.remove_employee).grid(row=3, column=0, columnspan=2, pady=10)

# #         # Requests Frame
# #         requests_frame = ttk.LabelFrame(content_frame, text="Requests", padding=15)
# #         requests_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# #         self.requests_tree = ttk.Treeview(requests_frame, columns=("Request ID", "Employee ID", "Asset ID", "Status", "Type", "Request Date"), show="headings")
# #         self.requests_tree.heading("Request ID", text="Request ID")
# #         self.requests_tree.heading("Employee ID", text="Employee ID")
# #         self.requests_tree.heading("Asset ID", text="Asset ID")
# #         self.requests_tree.heading("Status", text="Status")
# #         self.requests_tree.heading("Type", text="Type")
# #         self.requests_tree.heading("Request Date", text="Request Date")
# #         self.requests_tree.pack(fill=tk.BOTH, expand=True)

# #         ttk.Button(requests_frame, text="View Requests", command=self.view_requests).pack(pady=10)

# #         # Button Frame for additional buttons
# #         button_frame = tk.Frame(main_frame, bg="#f0f0f0")
# #         button_frame.pack(fill=tk.X, pady=10)

# #         # Log View Button
# #         ttk.Button(button_frame, text="View Logs", command=self.view_logs).pack(side=tk.LEFT, padx=10)

# #         # Logout Button
# #         ttk.Button(button_frame, text="Logout", command=self.logout).pack(side=tk.RIGHT, padx=10)

# #     def add_asset(self):
# #         asset_name = self.asset_name.get()
# #         if not asset_name:
# #             messagebox.showerror("Error", "Asset name cannot be empty")
# #             return
# #         try:
# #             response = requests.post("http://localhost:5000/api/admin/add_asset", json={"asset_name": asset_name})
# #             if response.status_code == 200:
# #                 messagebox.showinfo("Add Asset", f"Asset '{asset_name}' added successfully!")
# #             else:
# #                 messagebox.showerror("Error", "Failed to add asset")
# #         except requests.RequestException:
# #             messagebox.showerror("Error", "Failed to connect to server")

# #     def remove_asset(self):
# #         asset_name = self.asset_name.get()
# #         if not asset_name:
# #             messagebox.showerror("Error", "Asset name cannot be empty")
# #             return
# #         try:
# #             response = requests.post("http://localhost:5000/api/admin/remove_asset", json={"asset_name": asset_name})
# #             if response.status_code == 200:
# #                 messagebox.showinfo("Remove Asset", f"Asset '{asset_name}' removed successfully!")
# #             else:
# #                 messagebox.showerror("Error", "Failed to remove asset")
# #         except requests.RequestException:
# #             messagebox.showerror("Error", "Failed to connect to server")

# #     def add_employee(self):
# #         employee_name = self.employee_name.get()
# #         employee_id = self.employee_id.get()
# #         if not employee_name or not employee_id:
# #             messagebox.showerror("Error", "Employee name and ID cannot be empty")
# #             return
# #         try:
# #             response = requests.post("http://localhost:5000/api/admin/add_employee", json={"employee_name": employee_name, "employee_id": employee_id})
# #             if response.status_code == 200:
# #                 messagebox.showinfo("Add Employee", f"Employee '{employee_name}' added successfully!")
# #             else:
# #                 messagebox.showerror("Error", "Failed to add employee")
# #         except requests.RequestException:
# #             messagebox.showerror("Error", "Failed to connect to server")

# #     def remove_employee(self):
# #         employee_name = self.employee_name.get()
# #         employee_id = self.employee_id.get()
# #         if not employee_name or not employee_id:
# #             messagebox.showerror("Error", "Employee name and ID cannot be empty")
# #             return
# #         try:
# #             response = requests.post("http://localhost:5000/api/admin/remove_employee", json={"employee_name": employee_name, "employee_id": employee_id})
# #             if response.status_code == 200:
# #                 messagebox.showinfo("Remove Employee", f"Employee '{employee_name}' removed successfully!")
# #             else:
# #                 messagebox.showerror("Error", "Failed to remove employee")
# #         except requests.RequestException:
# #             messagebox.showerror("Error", "Failed to connect to server")

# #     def view_requests(self):
# #         try:
# #             response = requests.get("http://localhost:5000/api/admin/view_requests")
# #             if response.status_code == 200:
# #                 requests_data = response.json().get('requests', [])
# #                 for item in self.requests_tree.get_children():
# #                     self.requests_tree.delete(item)
# #                 for req in requests_data:
# #                     self.requests_tree.insert("", "end", values=(
# #                         req["Request ID"],
# #                         req["Employee ID"],
# #                         req["Asset ID"],
# #                         req["Status"],
# #                         req["Type"],
# #                         req["Request Date"]
# #                     ))
# #             else:
# #                 messagebox.showerror("Error", "Failed to retrieve requests")
# #         except requests.RequestException:
# #             messagebox.showerror("Error", "Failed to connect to server")

# #     def view_logs(self):
# #         self.master.withdraw()
# #         log_view_root = tk.Toplevel(self.master)
# #         LogViewDashboard(log_view_root)

# #     def logout(self):
# #         self.master.destroy()

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = AdminMenu(root, "Admin")
# #     root.mainloop()
# import tkinter as tk
# from tkinter import messagebox, ttk
# from log_view_dashboard import LogViewDashboard
# import requests

# class AdminMenu:
#     def __init__(self, master, username):
#         self.master = master
#         self.username = username
#         self.master.title("Admin Dashboard")
#         self.master.geometry("1200x800")
#         self.master.configure(bg="#f0f0f0")
#         self.master.state('zoomed')

#         # Main frame
#         main_frame = tk.Frame(self.master, bg="#f0f0f0")
#         main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

#         # Header
#         header_frame = tk.Frame(main_frame, bg="#4a4a4a")
#         header_frame.pack(fill=tk.X, pady=(0, 20))

#         tk.Label(header_frame, text="Admin Dashboard", font=("Arial", 24, "bold"), bg="#4a4a4a", fg="white").pack(side=tk.LEFT, padx=20, pady=10)
#         tk.Label(header_frame, text=f"Welcome, {username}", font=("Arial", 14), bg="#4a4a4a", fg="white").pack(side=tk.LEFT, padx=20, pady=10)

#         # View Logs Button
#         ttk.Button(header_frame, text="View Logs", command=self.view_logs).pack(side=tk.RIGHT, padx=10)

#         # Logout Button
#         ttk.Button(header_frame, text="Logout", command=self.logout).pack(side=tk.RIGHT, padx=10)

#         # Content frame
#         content_frame = tk.Frame(main_frame, bg="#f0f0f0", height=600)
#         content_frame.pack(fill=tk.BOTH, expand=True)

#         # Grid configuration
#         content_frame.grid_rowconfigure(0, weight=1)
#         content_frame.grid_columnconfigure(0, weight=1)
#         content_frame.grid_columnconfigure(1, weight=1)

#         # Asset Management Frame
#         asset_frame = ttk.LabelFrame(content_frame, text="Asset Management", padding=15)
#         asset_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

#         ttk.Label(asset_frame, text="Asset Name:").grid(row=0, column=0, sticky="w", pady=5)
#         self.asset_name = ttk.Entry(asset_frame, width=30)
#         self.asset_name.grid(row=0, column=1, pady=5)

#         ttk.Button(asset_frame, text="Add Asset", command=self.add_asset).grid(row=2, column=0, columnspan=2, pady=10)
#         ttk.Button(asset_frame, text="Remove Asset", command=self.remove_asset).grid(row=3, column=0, columnspan=2, pady=10)

#         # Employee Management Frame
#         employee_frame = ttk.LabelFrame(content_frame, text="Employee Management", padding=15)
#         employee_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

#         ttk.Label(employee_frame, text="Employee Name:").grid(row=0, column=0, sticky="w", pady=5)
#         self.employee_name = ttk.Entry(employee_frame, width=30)
#         self.employee_name.grid(row=0, column=1, pady=5)

#         ttk.Label(employee_frame, text="Employee ID:").grid(row=1, column=0, sticky="w", pady=5)
#         self.employee_id = ttk.Entry(employee_frame, width=30)
#         self.employee_id.grid(row=1, column=1, pady=5)

#         ttk.Button(employee_frame, text="Add Employee", command=self.add_employee).grid(row=2, column=0, columnspan=2, pady=10)
#         ttk.Button(employee_frame, text="Remove Employee", command=self.remove_employee).grid(row=3, column=0, columnspan=2, pady=10)

#         # Requests Frame
#         requests_frame = ttk.LabelFrame(content_frame, text="Requests", padding=15)
#         requests_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

#         self.requests_tree = ttk.Treeview(requests_frame, columns=("Request ID", "Employee ID", "Asset ID", "Status", "Type", "Request Date"), show="headings")
#         self.requests_tree.heading("Request ID", text="Request ID")
#         self.requests_tree.heading("Employee ID", text="Employee ID")
#         self.requests_tree.heading("Asset ID", text="Asset ID")
#         self.requests_tree.heading("Status", text="Status")
#         self.requests_tree.heading("Type", text="Type")
#         self.requests_tree.heading("Request Date", text="Request Date")
#         self.requests_tree.pack(fill=tk.BOTH, expand=True)

#         ttk.Button(requests_frame, text="View Requests", command=self.view_requests).pack(pady=10)

#     def add_asset(self):
#         asset_name = self.asset_name.get()
#         if not asset_name:
#             messagebox.showerror("Error", "Asset name cannot be empty")
#             return
#         try:
#             response = requests.post("http://localhost:5000/api/admin/add_asset", json={"asset_name": asset_name})
#             if response.status_code == 200:
#                 messagebox.showinfo("Add Asset", f"Asset '{asset_name}' added successfully!")
#             else:
#                 messagebox.showerror("Error", "Failed to add asset")
#         except requests.RequestException:
#             messagebox.showerror("Error", "Failed to connect to server")

#     def remove_asset(self):
#         asset_name = self.asset_name.get()
#         if not asset_name:
#             messagebox.showerror("Error", "Asset name cannot be empty")
#             return
#         try:
#             response = requests.post("http://localhost:5000/api/admin/remove_asset", json={"asset_name": asset_name})
#             if response.status_code == 200:
#                 messagebox.showinfo("Remove Asset", f"Asset '{asset_name}' removed successfully!")
#             else:
#                 messagebox.showerror("Error", "Failed to remove asset")
#         except requests.RequestException:
#             messagebox.showerror("Error", "Failed to connect to server")

#     def add_employee(self):
#         employee_name = self.employee_name.get()
#         employee_id = self.employee_id.get()
#         if not employee_name or not employee_id:
#             messagebox.showerror("Error", "Employee name and ID cannot be empty")
#             return
#         try:
#             response = requests.post("http://localhost:5000/api/admin/add_employee", json={"employee_name": employee_name, "employee_id": employee_id})
#             if response.status_code == 200:
#                 messagebox.showinfo("Add Employee", f"Employee '{employee_name}' added successfully!")
#             else:
#                 messagebox.showerror("Error", "Failed to add employee")
#         except requests.RequestException:
#             messagebox.showerror("Error", "Failed to connect to server")

#     def remove_employee(self):
#         employee_name = self.employee_name.get()
#         employee_id = self.employee_id.get()
#         if not employee_name or not employee_id:
#             messagebox.showerror("Error", "Employee name and ID cannot be empty")
#             return
#         try:
#             response = requests.post("http://localhost:5000/api/admin/remove_employee", json={"employee_name": employee_name, "employee_id": employee_id})
#             if response.status_code == 200:
#                 messagebox.showinfo("Remove Employee", f"Employee '{employee_name}' removed successfully!")
#             else:
#                 messagebox.showerror("Error", "Failed to remove employee")
#         except requests.RequestException:
#             messagebox.showerror("Error", "Failed to connect to server")

#     def view_requests(self):
#         try:
#             response = requests.get("http://localhost:5000/api/admin/view_requests")
#             if response.status_code == 200:
#                 requests_data = response.json().get('requests', [])
#                 for item in self.requests_tree.get_children():
#                     self.requests_tree.delete(item)
#                 for req in requests_data:
#                     self.requests_tree.insert("", "end", values=(
#                         req["Request ID"],
#                         req["Employee ID"],
#                         req["Asset ID"],
#                         req["Status"],
#                         req["Type"],
#                         req["Request Date"]
#                     ))
#             else:
#                 messagebox.showerror("Error", "Failed to retrieve requests")
#         except requests.RequestException:
#             messagebox.showerror("Error", "Failed to connect to server")

#     def view_logs(self):
#         self.master.withdraw()
#         log_view_root = tk.Toplevel(self.master)
#         LogViewDashboard(log_view_root)

#     def logout(self):
#         self.master.destroy()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AdminMenu(root, "Admin")
#     root.mainloop()
import tkinter as tk
from tkinter import messagebox, ttk
from log_view_dashboard import LogViewDashboard
import requests

class AdminMenu:
    def __init__(self, master, username):
        self.master = master
        self.username = username
        self.master.title("Admin Dashboard")
        self.master.geometry("1200x800")
        self.master.configure(bg="#f0f0f0")
        self.master.state('zoomed')

        # Main frame
        main_frame = tk.Frame(self.master, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header
        header_frame = tk.Frame(main_frame, bg="#4a4a4a")
        header_frame.pack(fill=tk.X, pady=(0, 20))

        tk.Label(header_frame, text="Admin Dashboard", font=("Arial", 24, "bold"), bg="#4a4a4a", fg="white").pack(side=tk.LEFT, padx=20, pady=10)
        tk.Label(header_frame, text=f"Welcome, {username}", font=("Arial", 14), bg="#4a4a4a", fg="white").pack(side=tk.LEFT, padx=20, pady=10)

        # View Logs Button
        ttk.Button(header_frame, text="View Logs", command=self.view_logs).pack(side=tk.RIGHT, padx=10)

        # Logout Button
        ttk.Button(header_frame, text="Logout", command=self.logout).pack(side=tk.RIGHT, padx=10)

        # Content frame
        content_frame = tk.Frame(main_frame, bg="#f0f0f0", height=600)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Grid configuration
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)

        # Asset Management Frame
        asset_frame = ttk.LabelFrame(content_frame, text="Asset Management", padding=15)
        asset_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(asset_frame, text="Asset Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.asset_name = ttk.Entry(asset_frame, width=30)
        self.asset_name.grid(row=0, column=1, pady=5)

        ttk.Button(asset_frame, text="Add Asset", command=self.add_asset).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(asset_frame, text="Remove Asset", command=self.remove_asset).grid(row=3, column=0, columnspan=2, pady=10)

        # Employee Management Frame
        employee_frame = ttk.LabelFrame(content_frame, text="Employee Management", padding=15)
        employee_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ttk.Label(employee_frame, text="Employee Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.employee_name = ttk.Entry(employee_frame, width=30)
        self.employee_name.grid(row=0, column=1, pady=5)

        ttk.Label(employee_frame, text="Employee ID:").grid(row=1, column=0, sticky="w", pady=5)
        self.employee_id = ttk.Entry(employee_frame, width=30)
        self.employee_id.grid(row=1, column=1, pady=5)

        ttk.Button(employee_frame, text="Add Employee", command=self.add_employee).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(employee_frame, text="Remove Employee", command=self.remove_employee).grid(row=3, column=0, columnspan=2, pady=10)

        # Requests Frame
        requests_frame = ttk.LabelFrame(content_frame, text="Requests", padding=15)
        requests_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.requests_tree = ttk.Treeview(requests_frame, columns=("Request ID", "Employee ID", "Asset ID", "Status", "Type", "Request Date"), show="headings")
        self.requests_tree.heading("Request ID", text="Request ID")
        self.requests_tree.heading("Employee ID", text="Employee ID")
        self.requests_tree.heading("Asset ID", text="Asset ID")
        self.requests_tree.heading("Status", text="Status")
        self.requests_tree.heading("Type", text="Type")
        self.requests_tree.heading("Request Date", text="Request Date")
        self.requests_tree.pack(fill=tk.BOTH, expand=True)

        ttk.Button(requests_frame, text="View Requests", command=self.view_requests).pack(pady=10)

    def add_asset(self):
        asset_name = self.asset_name.get()
        if not asset_name:
            messagebox.showerror("Error", "Asset name cannot be empty")
            return
        try:
            response = requests.post("http://localhost:5000/api/admin/add_asset", json={"asset_name": asset_name})
            if response.status_code == 200:
                messagebox.showinfo("Add Asset", f"Asset '{asset_name}' added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add asset")
        except requests.RequestException:
            messagebox.showerror("Error", "Failed to connect to server")

    def remove_asset(self):
        asset_name = self.asset_name.get()
        if not asset_name:
            messagebox.showerror("Error", "Asset name cannot be empty")
            return
        try:
            response = requests.post("http://localhost:5000/api/admin/remove_asset", json={"asset_name": asset_name})
            if response.status_code == 200:
                messagebox.showinfo("Remove Asset", f"Asset '{asset_name}' removed successfully!")
            else:
                messagebox.showerror("Error", "Failed to remove asset")
        except requests.RequestException:
            messagebox.showerror("Error", "Failed to connect to server")

    def add_employee(self):
        employee_name = self.employee_name.get()
        employee_id = self.employee_id.get()
        if not employee_name or not employee_id:
            messagebox.showerror("Error", "Employee name and ID cannot be empty")
            return
        try:
            response = requests.post("http://localhost:5000/api/admin/add_employee", json={"employee_name": employee_name, "employee_id": employee_id})
            if response.status_code == 200:
                messagebox.showinfo("Add Employee", f"Employee '{employee_name}' added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add employee")
        except requests.RequestException:
            messagebox.showerror("Error", "Failed to connect to server")

    def remove_employee(self):
        employee_name = self.employee_name.get()
        employee_id = self.employee_id.get()
        if not employee_name or not employee_id:
            messagebox.showerror("Error", "Employee name and ID cannot be empty")
            return
        try:
            response = requests.post("http://localhost:5000/api/admin/remove_employee", json={"employee_name": employee_name, "employee_id": employee_id})
            if response.status_code == 200:
                messagebox.showinfo("Remove Employee", f"Employee '{employee_name}' removed successfully!")
            else:
                messagebox.showerror("Error", "Failed to remove employee")
        except requests.RequestException:
            messagebox.showerror("Error", "Failed to connect to server")

    def view_requests(self):
        try:
            response = requests.get("http://localhost:5000/api/admin/view_requests")
            if response.status_code == 200:
                requests_data = response.json().get('requests', [])
                for item in self.requests_tree.get_children():
                    self.requests_tree.delete(item)
                for req in requests_data:
                    self.requests_tree.insert("", "end", values=(
                        req["Request ID"],
                        req["Employee ID"],
                        req["Asset ID"],
                        req["Status"],
                        req["Type"],
                        req["Request Date"]
                    ))
            else:
                messagebox.showerror("Error", "Failed to retrieve requests")
        except requests.RequestException:
            messagebox.showerror("Error", "Failed to connect to server")

    def view_logs(self):
        self.master.withdraw()
        log_view_root = tk.Toplevel(self.master)
        LogViewDashboard(log_view_root)

    def logout(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminMenu(root, "Admin")
    root.mainloop()
