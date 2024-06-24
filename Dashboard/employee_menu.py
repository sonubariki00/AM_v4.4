import sys
import tkinter as tk
from tkinter import messagebox,ttk
import requests

import tkinter as tk
from tkinter import ttk

class EmployeeMenu:
    def __init__(self, master, user_id):
        self.master = master
        self.user_id = user_id
        self.master.title("Employee Asset Management")
        self.master.geometry("1024x768")
        self.master.configure(bg="#f0f0f0")

        # Header
        header_frame = tk.Frame(self.master, bg="#4a4a4a", pady=10)
        header_frame.pack(fill=tk.X)
        
        tk.Label(header_frame, text="Employee Asset Management", font=("Arial", 20, "bold"), fg="white", bg="#4a4a4a").pack()

        # Main content
        main_frame = tk.Frame(self.master, bg="#f0f0f0", pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)

        left_frame = tk.Frame(main_frame, bg="#f0f0f0")
        left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20)

        right_frame = tk.Frame(main_frame, bg="#f0f0f0")
        right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=20)

        # Request Asset Frame
        request_frame = ttk.LabelFrame(left_frame, text="Request Asset", padding=10)
        request_frame.pack(fill=tk.X, pady=10)

        self.request_id = ttk.Entry(request_frame, width=30)
        self.request_id.pack(side=tk.LEFT, padx=(0, 10))

        ttk.Button(request_frame, text="Request Asset", command=self.request_asset).pack(side=tk.LEFT)

        # Search Asset Frame
        search_frame = ttk.LabelFrame(left_frame, text="Asset Search", padding=10)
        search_frame.pack(fill=tk.X, pady=10)

        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=(0, 10))

        ttk.Button(search_frame, text="Search Asset", command=self.search_asset).pack(side=tk.LEFT)

        self.search_result = tk.Label(search_frame, text="", font=("Arial", 12), bg="#f0f0f0", wraplength=400)
        self.search_result.pack(pady=10)

        # Release Asset Frame
        release_frame = ttk.LabelFrame(right_frame, text="Release Asset", padding=10)
        release_frame.pack(fill=tk.X, pady=10)

        self.release_id = ttk.Entry(release_frame, width=30)
        self.release_id.pack(side=tk.LEFT, padx=(0, 10))

        ttk.Button(release_frame, text="Release Asset", command=self.release_asset).pack(side=tk.LEFT)

        # Tagged Assets Frame
        tagged_frame = ttk.LabelFrame(right_frame, text="Tagged Assets", padding=10)
        tagged_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.tagged_result = tk.Text(tagged_frame, font=("Arial", 12), bg="white", wrap=tk.WORD, height=10)
        self.tagged_result.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        ttk.Button(tagged_frame, text="View Tagged Assets", command=self.view_tagged_assets).pack()

        # Footer
        footer_frame = tk.Frame(self.master, bg="#4a4a4a", pady=10)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        ttk.Button(footer_frame, text="Logout", command=self.logout).pack()

    def search_asset(self):
        asset_name = self.search_entry.get()
        print(asset_name)
        response = requests.post(f"http://localhost:5000/api/employee/search_asset", params={"asset_name": asset_name})
        if response.status_code == 200:
            asset_data = response.json()
            if asset_data:
                self.search_result.config(text=f"Asset ID: {asset_data['asset_id']}")
            else:
                self.search_result.config(text="Asset not found")
        else:
            self.search_result.config(text="Error searching for asset")

    def request_asset(self):
        asset_id = self.request_id.get()
        print(asset_id)
        response = requests.post("http://localhost:5000/api/employee/request_asset", params={"user_id": self.user_id, "asset_id": asset_id})
        
        if response.status_code == 200:
            messagebox.showinfo("Request Asset", f"Asset {asset_id}  requested successfully!")
        else:
            messagebox.showerror("Error", "Failed to request asset")

    def release_asset(self):
        asset_id = self.release_id.get()
        response = requests.post("http://localhost:5000/api/employee/release_asset", params={"user_id": self.user_id, "asset_id": asset_id})
        if response.status_code == 200:
            messagebox.showinfo("Release Asset", f"Asset (ID: {asset_id}) Pending for Release")
        else:
            messagebox.showerror("Error", "Failed to release asset")
            
    def view_tagged_assets(self):
        response = requests.get("http://localhost:5000/api/employee/view_tagged_assets", 
                                params={"employee_id": self.user_id})
        if response.status_code == 200:
            tagged_assets = response.json()
            if tagged_assets:
                asset_info = "\n".join([f"Asset ID: {asset['asset_id']}, Date: {asset['Date']}" 
                                        for asset in tagged_assets])
                self.tagged_result.delete('1.0', tk.END)
                self.tagged_result.insert(tk.END, asset_info)
            else:
                self.tagged_result.delete('1.0', tk.END)
                self.tagged_result.insert(tk.END, "No tagged assets found.")
        else:
            messagebox.showerror("Error", "Failed to view tagged assets")

    def logout(self):
        self.master.destroy()
        sys.exit(0)