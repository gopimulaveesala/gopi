import mysql.connector
import random
import time
from faker import Faker
from datetime import datetime

fake = Faker()

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",          
    password="root", 
    database="ecom_realtime_db"
)
cursor = db.cursor()

def seed_initial_data():
    """To insert initial data into the Customers and Products tables"""
    cursor.execute("SELECT COUNT(*) FROM Customers")
    if cursor.fetchone()[0] == 0:
        print("Inserting initial Customers and Products...")
        
        # Insert 50 Customers
        for _ in range(50):
            sql = "INSERT INTO Customers (customer_name, email, phone) VALUES (%s, %s, %s)"
            val = (fake.name(), fake.unique.email(), fake.phone_number()[:15])
            cursor.execute(sql, val)
            
        # Insert 20 Products
        categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Toys']
        for _ in range(20):
            sql = "INSERT INTO Products (product_name, category, base_price) VALUES (%s, %s, %s)"
            val = (fake.word().capitalize(), random.choice(categories), round(random.uniform(10.0, 500.0), 2))
            cursor.execute(sql, val)
            
        db.commit()
        print("Initial data seeded successfully!\n")

def start_streaming():
    """Continuou's live data generating loop"""
    print("Starting Live Data Stream... Press Ctrl+C to stop.")
    
    # Get max IDs to know the range
    cursor.execute("SELECT MAX(customer_id) FROM Customers")
    max_customer_id = cursor.fetchone()[0]
    
    cursor.execute("SELECT MAX(product_id) FROM Products")
    max_product_id = cursor.fetchone()[0]

    try:
        while True:
            # 1. Create Order
            customer_id = random.randint(1, max_customer_id)
            order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            status = random.choices(['Placed', 'Shipped', 'Delivered'], weights=[60, 30, 10])[0]
            
            # Temporary total amount, will update after adding items
            cursor.execute("INSERT INTO Orders (customer_id, order_date, status, total_amount) VALUES (%s, %s, %s, %s)", 
                           (customer_id, order_date, status, 0))
            order_id = cursor.lastrowid
            
            # 2. Add Order Items (1 to 3 items per order)
            num_items = random.randint(1, 3)
            order_total = 0
            
            for _ in range(num_items):
                product_id = random.randint(1, max_product_id)
                quantity = random.randint(1, 5)
                
                # Get product price
                cursor.execute("SELECT base_price FROM Products WHERE product_id = %s", (product_id,))
                price_per_item = cursor.fetchone()[0]
                total_price = quantity * price_per_item
                order_total += total_price
                
                cursor.execute("INSERT INTO Order_Items (order_id, product_id, quantity, price_per_item, total_price) VALUES (%s, %s, %s, %s, %s)",
                               (order_id, product_id, quantity, price_per_item, total_price))
            
            # Update order total
            cursor.execute("UPDATE Orders SET total_amount = %s WHERE order_id = %s", (order_total, order_id))
            
            # 3. Add Payment (80% success rate)
            payment_method = random.choice(['UPI', 'Card', 'COD'])
            payment_status = random.choices(['Success', 'Failed', 'Pending'], weights=[80, 10, 10])[0]
            cursor.execute("INSERT INTO Payments (order_id, payment_method, payment_status, payment_date, amount) VALUES (%s, %s, %s, %s, %s)",
                           (order_id, payment_method, payment_status, order_date, order_total))
            
            db.commit()
            print(f"[{order_date}] Order #{order_id} generated for Customer #{customer_id} | Total: ${order_total:.2f} | Status: {payment_status}")
            
            # Wait for 3 to 7 seconds before next order
            time.sleep(random.randint(3, 7))
            
    except KeyboardInterrupt:
        print("\nData streaming stopped by user.")
    finally:
        cursor.close()
        db.close()

# Run the functions
seed_initial_data()
start_streaming()