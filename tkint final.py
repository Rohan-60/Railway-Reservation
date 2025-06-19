import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import os
from datetime import datetime
import re

class RailwayReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Indian Railway Reservation System")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1e3c72')
        
        # Set window icon and make it non-resizable for better layout
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Global variables
        self.current_user = None
        self.ticket_counter = 1256940
        
        # Create main container
        self.main_frame = tk.Frame(root, bg='#1e3c72')
        self.main_frame.pack(fill='both', expand=True)
        
        # Initialize CSV files if they don't exist
        self.initialize_csv_files()
        
        # Create and show login screen
        self.create_login_screen()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f'1200x800+{x}+{y}')
    
    def initialize_csv_files(self):
        """Initialize CSV files with headers if they don't exist"""
        # Create csv directory if it doesn't exist
        if not os.path.exists('csv'):
            os.makedirs('csv')
        
        # Initialize user accounts file
        if not os.path.exists('railway.csv'):
            with open('railway.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['demo_user', 'password123'])
        
        # Initialize admin file (using the provided data)
        if not os.path.exists('csv/admin.csv'):
            with open('csv/admin.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Rohan', 'flowerhorn'])
                writer.writerow(['AtulKrishna', '12345'])
        
        # Initialize train info (using provided data)
        if not os.path.exists('csv/traininfo.csv'):
            with open('csv/traininfo.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                trains = [
                    ['6768', 'Janshadapti Express', '13:00', 'Mumbai Central', 'Delhi Central', '500', '1000'],
                    ['6612', 'Kanyakumari Express', '14:00', 'Trivandrum Junction', 'Kanyakumari Station', '200', '800'],
                    ['6600', 'Chennai Express', '15:00', 'Ernakulam Junction', 'Madras Station', '700', '1400'],
                    ['6998', 'Nagarcoil Express', '17:05', 'Nagarcoil station', 'Mumbai station', '500', '2500'],
                    ['7676', 'Garib Rath Express', '02:37', 'Delhi station', 'Trivandrum station', '200', '700']
                ]
                writer.writerows(trains)
        
        # Initialize tickets file
        if not os.path.exists('csv/tickets.csv'):
            with open('csv/tickets.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                # Headers: ticket_id, train_no, passenger_name, train_name, time, departure, arrival, fare, booked_by
    
    def clear_frame(self):
        """Clear all widgets from main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def create_login_screen(self):
        """Create the main login/signup screen"""
        self.clear_frame()
        
        # Header
        header_frame = tk.Frame(self.main_frame, bg='#1e3c72', height=100)
        header_frame.pack(fill='x', pady=20)
        
        title_label = tk.Label(header_frame, text="🚂 INDIAN RAILWAY", 
                              font=('Arial', 28, 'bold'), 
                              fg='white', bg='#1e3c72')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame, text="Reservation System", 
                                 font=('Arial', 16), 
                                 fg='#ffd700', bg='#1e3c72')
        subtitle_label.pack()
        
        # Main content area
        content_frame = tk.Frame(self.main_frame, bg='white', relief='raised', bd=2)
        content_frame.pack(pady=40, padx=200, fill='both', expand=True)
        
        # Welcome message
        welcome_label = tk.Label(content_frame, text="Welcome to Railway Reservation Portal", 
                                font=('Arial', 18, 'bold'), 
                                fg='#1e3c72', bg='white')
        welcome_label.pack(pady=30)
        
        # Buttons frame
        buttons_frame = tk.Frame(content_frame, bg='white')
        buttons_frame.pack(pady=40)
        
        # Style for buttons
        button_style = {
            'font': ('Arial', 12, 'bold'),
            'width': 20,
            'height': 2,
            'cursor': 'hand2'
        }
        
        # Sign Up button
        signup_btn = tk.Button(buttons_frame, text="📝 Create New Account", 
                              bg='#28a745', fg='white',
                              command=self.show_signup_form,
                              **button_style)
        signup_btn.pack(pady=10)
        
        # Login button
        login_btn = tk.Button(buttons_frame, text="🔐 User Login", 
                             bg='#007bff', fg='white',
                             command=self.show_login_form,
                             **button_style)
        login_btn.pack(pady=10)
        
        # Admin login button
        admin_btn = tk.Button(buttons_frame, text="👨‍💼 Admin Login", 
                             bg='#dc3545', fg='white',
                             command=self.show_admin_login,
                             **button_style)
        admin_btn.pack(pady=10)
        
        # Exit button
        exit_btn = tk.Button(buttons_frame, text="🚪 Exit", 
                            bg='#6c757d', fg='white',
                            command=self.root.quit,
                            **button_style)
        exit_btn.pack(pady=10)
        
        # Footer
        footer_label = tk.Label(self.main_frame, text="© 2024 Indian Railways - Safe & Secure Journey", 
                               font=('Arial', 10), 
                               fg='#ffd700', bg='#1e3c72')
        footer_label.pack(side='bottom', pady=10)
    
    def show_signup_form(self):
        """Show signup form"""
        self.clear_frame()
        
        # Header
        self.create_header("Create New Account")
        
        # Form frame
        form_frame = tk.Frame(self.main_frame, bg='white', relief='raised', bd=2)
        form_frame.pack(pady=40, padx=300, fill='both', expand=True)
        
        tk.Label(form_frame, text="Sign Up for Railway Account", 
                font=('Arial', 16, 'bold'), 
                fg='#1e3c72', bg='white').pack(pady=20)
        
        # Username
        tk.Label(form_frame, text="Username:", font=('Arial', 12), 
                bg='white').pack(anchor='w', padx=40, pady=(10,5))
        username_entry = tk.Entry(form_frame, font=('Arial', 12), width=30, relief='solid', bd=1)
        username_entry.pack(padx=40, pady=(0,10))
        
        # Password
        tk.Label(form_frame, text="Password:", font=('Arial', 12), 
                bg='white').pack(anchor='w', padx=40, pady=(10,5))
        password_entry = tk.Entry(form_frame, font=('Arial', 12), width=30, show='*', relief='solid', bd=1)
        password_entry.pack(padx=40, pady=(0,10))
        
        # Confirm Password
        tk.Label(form_frame, text="Confirm Password:", font=('Arial', 12), 
                bg='white').pack(anchor='w', padx=40, pady=(10,5))
        confirm_entry = tk.Entry(form_frame, font=('Arial', 12), width=30, show='*', relief='solid', bd=1)
        confirm_entry.pack(padx=40, pady=(0,20))
        
        # Buttons
        btn_frame = tk.Frame(form_frame, bg='white')
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Create Account", bg='#28a745', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=lambda: self.signup(username_entry.get(), password_entry.get(), confirm_entry.get())).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Back", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=self.create_login_screen).pack(side='left', padx=10)
    
    def show_login_form(self):
        """Show user login form"""
        self.clear_frame()
        
        # Header
        self.create_header("User Login")
        
        # Form frame
        form_frame = tk.Frame(self.main_frame, bg='white', relief='raised', bd=2)
        form_frame.pack(pady=40, padx=300, fill='both', expand=True)
        
        tk.Label(form_frame, text="Login to Your Account", 
                font=('Arial', 16, 'bold'), 
                fg='#1e3c72', bg='white').pack(pady=20)
        
        # Username
        tk.Label(form_frame, text="Username:", font=('Arial', 12), 
                bg='white').pack(anchor='w', padx=40, pady=(10,5))
        username_entry = tk.Entry(form_frame, font=('Arial', 12), width=30, relief='solid', bd=1)
        username_entry.pack(padx=40, pady=(0,10))
        
        # Password
        tk.Label(form_frame, text="Password:", font=('Arial', 12), 
                bg='white').pack(anchor='w', padx=40, pady=(10,5))
        password_entry = tk.Entry(form_frame, font=('Arial', 12), width=30, show='*', relief='solid', bd=1)
        password_entry.pack(padx=40, pady=(0,20))
        
        # Buttons
        btn_frame = tk.Frame(form_frame, bg='white')
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Login", bg='#007bff', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=lambda: self.login(username_entry.get(), password_entry.get())).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Back", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=self.create_login_screen).pack(side='left', padx=10)
    
    def show_admin_login(self):
        """Show admin login form"""
        self.clear_frame()
        
        # Header
        self.create_header("Admin Login")
        
        # Form frame
        form_frame = tk.Frame(self.main_frame, bg='white', relief='raised', bd=2)
        form_frame.pack(pady=40, padx=300, fill='both', expand=True)
        
        tk.Label(form_frame, text="Admin Access Portal", 
                font=('Arial', 16, 'bold'), 
                fg='#dc3545', bg='white').pack(pady=20)
        
        # Username
        tk.Label(form_frame, text="Admin Username:", font=('Arial', 12), 
                bg='white').pack(anchor='w', padx=40, pady=(10,5))
        username_entry = tk.Entry(form_frame, font=('Arial', 12), width=30, relief='solid', bd=1)
        username_entry.pack(padx=40, pady=(0,10))
        
        # Password
        tk.Label(form_frame, text="Admin Password:", font=('Arial', 12), 
                bg='white').pack(anchor='w', padx=40, pady=(10,5))
        password_entry = tk.Entry(form_frame, font=('Arial', 12), width=30, show='*', relief='solid', bd=1)
        password_entry.pack(padx=40, pady=(0,20))
        
        # Buttons
        btn_frame = tk.Frame(form_frame, bg='white')
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Admin Login", bg='#dc3545', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=lambda: self.admin_login(username_entry.get(), password_entry.get())).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Back", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=self.create_login_screen).pack(side='left', padx=10)
    
    def create_header(self, title):
        """Create header section"""
        header_frame = tk.Frame(self.main_frame, bg='#1e3c72', height=80)
        header_frame.pack(fill='x', pady=(0,20))
        
        tk.Label(header_frame, text=f"🚂 {title}", 
                font=('Arial', 20, 'bold'), 
                fg='white', bg='#1e3c72').pack(pady=20)
    
    def signup(self, username, password, confirm_password):
        """Handle user signup"""
        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long!")
            return
        
        # Check if username already exists
        try:
            with open('railway.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == username:
                        messagebox.showerror("Error", "Username already exists!")
                        return
        except FileNotFoundError:
            pass
        
        # Add new user
        with open('railway.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        
        messagebox.showsuccess("Success", "Account created successfully!")
        self.create_login_screen()
    
    def login(self, username, password):
        """Handle user login"""
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password!")
            return
        
        try:
            with open('railway.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) >= 2 and row[0] == username and row[1] == password:
                        self.current_user = username
                        messagebox.showinfo("Success", f"Welcome {username}!")
                        self.show_user_dashboard()
                        return
            
            messagebox.showerror("Error", "Invalid username or password!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No user accounts found. Please sign up first!")
    
    def admin_login(self, username, password):
        """Handle admin login"""
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password!")
            return
        
        try:
            with open('csv/admin.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) >= 2 and row[0] == username and row[1] == password:
                        messagebox.showinfo("Success", f"Welcome Admin {username}!")
                        self.show_admin_dashboard()
                        return
            
            messagebox.showerror("Error", "Invalid admin credentials!")
        except FileNotFoundError:
            messagebox.showerror("Error", "Admin file not found!")
    
    def show_user_dashboard(self):
        """Show user dashboard"""
        self.clear_frame()
        
        # Header
        header_frame = tk.Frame(self.main_frame, bg='#1e3c72', height=80)
        header_frame.pack(fill='x')
        
        tk.Label(header_frame, text=f"🚂 Welcome {self.current_user}", 
                font=('Arial', 18, 'bold'), 
                fg='white', bg='#1e3c72').pack(side='left', padx=20, pady=20)
        
        tk.Button(header_frame, text="Logout", bg='#dc3545', fg='white',
                 font=('Arial', 10, 'bold'), 
                 command=self.logout).pack(side='right', padx=20, pady=20)
        
        # Dashboard content
        dashboard_frame = tk.Frame(self.main_frame, bg='white')
        dashboard_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(dashboard_frame, text="Railway Services Dashboard", 
                font=('Arial', 16, 'bold'), 
                fg='#1e3c72', bg='white').pack(pady=20)
        
        # Service buttons
        services_frame = tk.Frame(dashboard_frame, bg='white')
        services_frame.pack(pady=40)
        
        button_style = {
            'font': ('Arial', 12, 'bold'),
            'width': 25,
            'height': 3,
            'cursor': 'hand2'
        }
        
        tk.Button(services_frame, text="🎫 Reserve Ticket", 
                 bg='#28a745', fg='white',
                 command=self.show_reservation_form,
                 **button_style).grid(row=0, column=0, padx=20, pady=15)
        
        tk.Button(services_frame, text="📋 View Booked Tickets", 
                 bg='#17a2b8', fg='white',
                 command=self.show_booked_tickets,
                 **button_style).grid(row=0, column=1, padx=20, pady=15)
        
        tk.Button(services_frame, text="❌ Cancel Ticket", 
                 bg='#dc3545', fg='white',
                 command=self.show_cancel_form,
                 **button_style).grid(row=1, column=0, padx=20, pady=15)
        
        tk.Button(services_frame, text="🚄 Train Schedule", 
                 bg='#ffc107', fg='black',
                 command=self.show_train_schedule,
                 **button_style).grid(row=1, column=1, padx=20, pady=15)
    
    def show_admin_dashboard(self):
        """Show admin dashboard"""
        self.clear_frame()
        
        # Header
        header_frame = tk.Frame(self.main_frame, bg='#dc3545', height=80)
        header_frame.pack(fill='x')
        
        tk.Label(header_frame, text="👨‍💼 Admin Dashboard", 
                font=('Arial', 18, 'bold'), 
                fg='white', bg='#dc3545').pack(side='left', padx=20, pady=20)
        
        tk.Button(header_frame, text="Logout", bg='#6c757d', fg='white',
                 font=('Arial', 10, 'bold'), 
                 command=self.logout).pack(side='right', padx=20, pady=20)
        
        # Dashboard content
        dashboard_frame = tk.Frame(self.main_frame, bg='white')
        dashboard_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(dashboard_frame, text="Administration Panel", 
                font=('Arial', 16, 'bold'), 
                fg='#dc3545', bg='white').pack(pady=20)
        
        # Admin buttons
        admin_frame = tk.Frame(dashboard_frame, bg='white')
        admin_frame.pack(pady=40)
        
        button_style = {
            'font': ('Arial', 12, 'bold'),
            'width': 25,
            'height': 3,
            'cursor': 'hand2'
        }
        
        tk.Button(admin_frame, text="🔄 Update Train Schedule", 
                 bg='#007bff', fg='white',
                 command=self.show_update_train_form,
                 **button_style).pack(pady=15)
        
        tk.Button(admin_frame, text="➕ Add New Train", 
                 bg='#28a745', fg='white',
                 command=self.show_add_train_form,
                 **button_style).pack(pady=15)
        
        tk.Button(admin_frame, text="📊 View All Bookings", 
                 bg='#17a2b8', fg='white',
                 command=self.show_all_bookings,
                 **button_style).pack(pady=15)
    
    def show_reservation_form(self):
        """Show ticket reservation form"""
        # Create new window for reservation
        reservation_window = tk.Toplevel(self.root)
        reservation_window.title("Reserve Ticket")
        reservation_window.geometry("600x500")
        reservation_window.configure(bg='white')
        reservation_window.transient(self.root)
        reservation_window.grab_set()
        
        # Center the window
        reservation_window.update_idletasks()
        x = (reservation_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (reservation_window.winfo_screenheight() // 2) - (500 // 2)
        reservation_window.geometry(f'600x500+{x}+{y}')
        
        tk.Label(reservation_window, text="🎫 Ticket Reservation", 
                font=('Arial', 16, 'bold'), 
                fg='#1e3c72', bg='white').pack(pady=20)
        
        # Form fields
        fields_frame = tk.Frame(reservation_window, bg='white')
        fields_frame.pack(pady=20, padx=40, fill='both', expand=True)
        
        # Passenger Name
        tk.Label(fields_frame, text="Passenger Name:", font=('Arial', 12), 
                bg='white').grid(row=0, column=0, sticky='w', pady=10)
        name_entry = tk.Entry(fields_frame, font=('Arial', 12), width=25)
        name_entry.grid(row=0, column=1, padx=20, pady=10)
        
        # Train Number
        tk.Label(fields_frame, text="Train Number:", font=('Arial', 12), 
                bg='white').grid(row=1, column=0, sticky='w', pady=10)
        train_var = tk.StringVar()
        train_combo = ttk.Combobox(fields_frame, textvariable=train_var, width=22, state='readonly')
        
        # Load train numbers
        try:
            with open('csv/traininfo.csv', 'r') as file:
                reader = csv.reader(file)
                trains = [f"{row[0]} - {row[1]}" for row in reader if row]
                train_combo['values'] = trains
        except FileNotFoundError:
            messagebox.showerror("Error", "Train information file not found!")
            reservation_window.destroy()
            return
        
        train_combo.grid(row=1, column=1, padx=20, pady=10)
        
        # Class selection
        tk.Label(fields_frame, text="Class:", font=('Arial', 12), 
                bg='white').grid(row=2, column=0, sticky='w', pady=10)
        class_var = tk.StringVar(value="Non-AC")
        class_frame = tk.Frame(fields_frame, bg='white')
        class_frame.grid(row=2, column=1, padx=20, pady=10, sticky='w')
        
        tk.Radiobutton(class_frame, text="Non-AC", variable=class_var, value="Non-AC", 
                      bg='white', font=('Arial', 10)).pack(side='left')
        tk.Radiobutton(class_frame, text="AC", variable=class_var, value="AC", 
                      bg='white', font=('Arial', 10)).pack(side='left', padx=20)
        
        # Buttons
        btn_frame = tk.Frame(reservation_window, bg='white')
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Reserve Ticket", bg='#28a745', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=lambda: self.reserve_ticket(name_entry.get(), train_var.get(), 
                                                   class_var.get(), reservation_window)).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Cancel", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=reservation_window.destroy).pack(side='left', padx=10)
    
    def reserve_ticket(self, name, train_info, class_type, window):
        """Reserve a ticket"""
        if not name or not train_info:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        train_no = train_info.split(' - ')[0]
        
        # Get train details
        try:
            with open('csv/traininfo.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == train_no:
                        train_name = row[1]
                        time = row[2]
                        departure = row[3]
                        arrival = row[4]
                        fare = row[6] if class_type == "AC" else row[5]
                        break
                else:
                    messagebox.showerror("Error", "Train not found!")
                    return
        except FileNotFoundError:
            messagebox.showerror("Error", "Train information file not found!")
            return
        
        # Generate ticket ID
        self.ticket_counter += 1
        ticket_id = self.ticket_counter
        
        # Save ticket
        with open('csv/tickets.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ticket_id, train_no, name, train_name, time, 
                           departure, arrival, fare, self.current_user])
        
        messagebox.showinfo("Success", f"Ticket reserved successfully!\nTicket ID: {ticket_id}\nFare: ₹{fare}")
        window.destroy()
    
    def show_booked_tickets(self):
        """Show user's booked tickets"""
        tickets_window = tk.Toplevel(self.root)
        tickets_window.title("My Booked Tickets")
        tickets_window.geometry("1000x600")
        tickets_window.configure(bg='white')
        tickets_window.transient(self.root)
        
        tk.Label(tickets_window, text="📋 My Booked Tickets", 
                font=('Arial', 16, 'bold'), 
                fg='#1e3c72', bg='white').pack(pady=20)
        
        # Create treeview for tickets
        columns = ('Ticket ID', 'Train No', 'Passenger', 'Train Name', 'Time', 'From', 'To', 'Fare')
        tree = ttk.Treeview(tickets_window, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        # Load user's tickets
        try:
            with open('csv/tickets.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) >= 9 and row[8] == self.current_user:
                        tree.insert('', 'end', values=row[:8])
        except FileNotFoundError:
            pass
        
        tree.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Close button
        tk.Button(tickets_window, text="Close", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=tickets_window.destroy).pack(pady=20)
    
    def show_train_schedule(self):
        """Show train schedule"""
        schedule_window = tk.Toplevel(self.root)
        schedule_window.title("Train Schedule")
        schedule_window.geometry("1000x600")
        schedule_window.configure(bg='white')
        schedule_window.transient(self.root)
        
        tk.Label(schedule_window, text="🚄 Train Schedule", 
                font=('Arial', 16, 'bold'), 
                fg='#1e3c72', bg='white').pack(pady=20)
        
        # Create treeview for schedule
        columns = ('Train No', 'Train Name', 'Time', 'From', 'To', 'Non-AC Fare', 'AC Fare')
        tree = ttk.Treeview(schedule_window, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=140)
        
        # Load train schedule
        try:
            with open('csv/traininfo.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) >= 7:
                        tree.insert('', 'end', values=row[:7])
        except FileNotFoundError:
            messagebox.showerror("Error", "Train information file not found!")
        
        tree.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Close button
        tk.Button(schedule_window, text="Close", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=schedule_window.destroy).pack(pady=20)
    
    def show_cancel_form(self):
        """Show ticket cancellation form"""
        cancel_window = tk.Toplevel(self.root)
        cancel_window.title("Cancel Ticket")
        cancel_window.geometry("500x300")
        cancel_window.configure(bg='white')
        cancel_window.transient(self.root)
        cancel_window.grab_set()
        
        # Center the window
        cancel_window.update_idletasks()
        x = (cancel_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (cancel_window.winfo_screenheight() // 2) - (300 // 2)
        cancel_window.geometry(f'500x300+{x}+{y}')
        
        tk.Label(cancel_window, text="❌ Cancel Ticket", 
                font=('Arial', 16, 'bold'), 
                fg='#dc3545', bg='white').pack(pady=30)
        
        tk.Label(cancel_window, text="Enter Passenger Name:", 
                font=('Arial', 12), bg='white').pack(pady=10)
        
        name_entry = tk.Entry(cancel_window, font=('Arial', 12), width=30)
        name_entry.pack(pady=10)
        
        # Buttons
        btn_frame = tk.Frame(cancel_window, bg='white')
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Cancel Ticket", bg='#dc3545', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=lambda: self.cancel_ticket(name_entry.get(), cancel_window)).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Close", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=cancel_window.destroy).pack(side='left', padx=10)
    
    def cancel_ticket(self, passenger_name, window):
        """Cancel a ticket"""
        if not passenger_name:
            messagebox.showerror("Error", "Please enter passenger name!")
            return
        
        tickets = []
        ticket_found = False
        
        try:
            with open('csv/tickets.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) >= 9:
                        if row[2] == passenger_name and row[8] == self.current_user:
                            ticket_found = True
                            messagebox.showinfo("Success", f"Ticket for {passenger_name} cancelled successfully!")
                        else:
                            tickets.append(row)
            
            if not ticket_found:
                messagebox.showerror("Error", "Ticket not found or you don't have permission to cancel it!")
                return
            
            # Write back remaining tickets
            with open('csv/tickets.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(tickets)
            
            window.destroy()
            
        except FileNotFoundError:
            messagebox.showerror("Error", "No tickets found!")
    
    def show_update_train_form(self):
        """Show update train form (Admin)"""
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Train Schedule")
        update_window.geometry("600x600")
        update_window.configure(bg='white')
        update_window.transient(self.root)
        update_window.grab_set()
        
        # Center the window
        update_window.update_idletasks()
        x = (update_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (update_window.winfo_screenheight() // 2) - (600 // 2)
        update_window.geometry(f'600x600+{x}+{y}')
        
        tk.Label(update_window, text="🔄 Update Train Schedule", 
                font=('Arial', 16, 'bold'), 
                fg='#007bff', bg='white').pack(pady=20)
        
        # Form fields
        fields_frame = tk.Frame(update_window, bg='white')
        fields_frame.pack(pady=20, padx=40, fill='both', expand=True)
        
        # Train selection
        tk.Label(fields_frame, text="Select Train:", font=('Arial', 12), 
                bg='white').grid(row=0, column=0, sticky='w', pady=10)
        train_var = tk.StringVar()
        train_combo = ttk.Combobox(fields_frame, textvariable=train_var, width=30, state='readonly')
        
        # Load existing trains
        try:
            with open('csv/traininfo.csv', 'r') as file:
                reader = csv.reader(file)
                trains = [f"{row[0]} - {row[1]}" for row in reader if row]
                train_combo['values'] = trains
        except FileNotFoundError:
            messagebox.showerror("Error", "Train information file not found!")
            update_window.destroy()
            return
        
        train_combo.grid(row=0, column=1, padx=20, pady=10)
        
        # Other fields
        fields = [
            ("Train Name:", 1),
            ("Time:", 2),
            ("Departure Station:", 3),
            ("Arrival Station:", 4),
            ("Non-AC Fare:", 5),
            ("AC Fare:", 6)
        ]
        
        entries = {}
        for field_name, row in fields:
            tk.Label(fields_frame, text=field_name, font=('Arial', 12), 
                    bg='white').grid(row=row, column=0, sticky='w', pady=10)
            entry = tk.Entry(fields_frame, font=('Arial', 12), width=32)
            entry.grid(row=row, column=1, padx=20, pady=10)
            entries[field_name] = entry
        
        def load_train_details():
            """Load selected train details"""
            selected = train_var.get()
            if not selected:
                return
            
            train_no = selected.split(' - ')[0]
            try:
                with open('csv/traininfo.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row and row[0] == train_no:
                            entries["Train Name:"].delete(0, tk.END)
                            entries["Train Name:"].insert(0, row[1])
                            entries["Time:"].delete(0, tk.END)
                            entries["Time:"].insert(0, row[2])
                            entries["Departure Station:"].delete(0, tk.END)
                            entries["Departure Station:"].insert(0, row[3])
                            entries["Arrival Station:"].delete(0, tk.END)
                            entries["Arrival Station:"].insert(0, row[4])
                            entries["Non-AC Fare:"].delete(0, tk.END)
                            entries["Non-AC Fare:"].insert(0, row[5])
                            entries["AC Fare:"].delete(0, tk.END)
                            entries["AC Fare:"].insert(0, row[6])
                            break
            except FileNotFoundError:
                pass
        
        train_combo.bind('<<ComboboxSelected>>', lambda e: load_train_details())
        
        # Buttons
        btn_frame = tk.Frame(update_window, bg='white')
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Update Train", bg='#007bff', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=lambda: self.update_train(train_var.get(), entries, update_window)).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Cancel", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=update_window.destroy).pack(side='left', padx=10)
    
    def update_train(self, selected_train, entries, window):
        """Update train information"""
        if not selected_train:
            messagebox.showerror("Error", "Please select a train!")
            return
        
        train_no = selected_train.split(' - ')[0]
        
        # Validate inputs
        for field_name, entry in entries.items():
            if not entry.get().strip():
                messagebox.showerror("Error", f"Please fill {field_name}")
                return
        
        # Update train info
        trains = []
        train_found = False
        
        try:
            with open('csv/traininfo.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == train_no:
                        updated_row = [
                            train_no,
                            entries["Train Name:"].get().strip(),
                            entries["Time:"].get().strip(),
                            entries["Departure Station:"].get().strip(),
                            entries["Arrival Station:"].get().strip(),
                            entries["Non-AC Fare:"].get().strip(),
                            entries["AC Fare:"].get().strip()
                        ]
                        trains.append(updated_row)
                        train_found = True
                    else:
                        trains.append(row)
            
            if train_found:
                with open('csv/traininfo.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(trains)
                
                messagebox.showinfo("Success", "Train information updated successfully!")
                window.destroy()
            else:
                messagebox.showerror("Error", "Train not found!")
                
        except FileNotFoundError:
            messagebox.showerror("Error", "Train information file not found!")
    
    def show_add_train_form(self):
        """Show add new train form (Admin)"""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Train")
        add_window.geometry("600x500")
        add_window.configure(bg='white')
        add_window.transient(self.root)
        add_window.grab_set()
        
        # Center the window
        add_window.update_idletasks()
        x = (add_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (add_window.winfo_screenheight() // 2) - (500 // 2)
        add_window.geometry(f'600x500+{x}+{y}')
        
        tk.Label(add_window, text="➕ Add New Train", 
                font=('Arial', 16, 'bold'), 
                fg='#28a745', bg='white').pack(pady=20)
        
        # Form fields
        fields_frame = tk.Frame(add_window, bg='white')
        fields_frame.pack(pady=20, padx=40, fill='both', expand=True)
        
        fields = [
            ("Train Number:", 0),
            ("Train Name:", 1),
            ("Time:", 2),
            ("Departure Station:", 3),
            ("Arrival Station:", 4),
            ("Non-AC Fare:", 5),
            ("AC Fare:", 6)
        ]
        
        entries = {}
        for field_name, row in fields:
            tk.Label(fields_frame, text=field_name, font=('Arial', 12), 
                    bg='white').grid(row=row, column=0, sticky='w', pady=10)
            entry = tk.Entry(fields_frame, font=('Arial', 12), width=32)
            entry.grid(row=row, column=1, padx=20, pady=10)
            entries[field_name] = entry
        
        # Buttons
        btn_frame = tk.Frame(add_window, bg='white')
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Add Train", bg='#28a745', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=lambda: self.add_train(entries, add_window)).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Cancel", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=add_window.destroy).pack(side='left', padx=10)
    
    def add_train(self, entries, window):
        """Add new train"""
        # Validate inputs
        for field_name, entry in entries.items():
            if not entry.get().strip():
                messagebox.showerror("Error", f"Please fill {field_name}")
                return
        
        train_no = entries["Train Number:"].get().strip()
        
        # Check if train number already exists
        try:
            with open('csv/traininfo.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == train_no:
                        messagebox.showerror("Error", "Train number already exists!")
                        return
        except FileNotFoundError:
            pass
        
        # Add new train
        new_train = [
            train_no,
            entries["Train Name:"].get().strip(),
            entries["Time:"].get().strip(),
            entries["Departure Station:"].get().strip(),
            entries["Arrival Station:"].get().strip(),
            entries["Non-AC Fare:"].get().strip(),
            entries["AC Fare:"].get().strip()
        ]
        
        with open('csv/traininfo.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_train)
        
        messagebox.showinfo("Success", "New train added successfully!")
        window.destroy()
    
    def show_all_bookings(self):
        """Show all bookings (Admin)"""
        bookings_window = tk.Toplevel(self.root)
        bookings_window.title("All Bookings")
        bookings_window.geometry("1200x600")
        bookings_window.configure(bg='white')
        bookings_window.transient(self.root)
        
        tk.Label(bookings_window, text="📊 All Ticket Bookings", 
                font=('Arial', 16, 'bold'), 
                fg='#dc3545', bg='white').pack(pady=20)
        
        # Create treeview for all bookings
        columns = ('Ticket ID', 'Train No', 'Passenger', 'Train Name', 'Time', 'From', 'To', 'Fare', 'Booked By')
        tree = ttk.Treeview(bookings_window, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=130)
        
        # Load all bookings
        try:
            with open('csv/tickets.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) >= 9:
                        tree.insert('', 'end', values=row)
        except FileNotFoundError:
            pass
        
        tree.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Close button
        tk.Button(bookings_window, text="Close", bg='#6c757d', fg='white',
                 font=('Arial', 12, 'bold'), width=15, height=2,
                 command=bookings_window.destroy).pack(pady=20)
    
    def logout(self):
        """Logout user"""
        self.current_user = None
        messagebox.showinfo("Logout", "You have been logged out successfully!")
        self.create_login_screen()


# Custom messagebox for success (since tkinter doesn't have showsuccess)
def show_success_message(title, message):
    messagebox.showinfo(title, message)

# Monkey patch messagebox to add showsuccess
messagebox.showsuccess = show_success_message

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = RailwayReservationSystem(root)
    root.mainloop()
