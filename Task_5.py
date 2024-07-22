import tkinter as tk
from tkinter import messagebox, ttk
import requests

# Function to fetch exchange rates from the API
def fetch_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rate = data['rates'].get(target_currency)
        if rate is None:
            raise ValueError("Target currency not available")
        return rate
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch exchange rates: {e}")
        return None
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
        return None

# Function to perform currency conversion
def perform_conversion(amount, rate):
    return amount * rate

# Function to handle conversion logic
def handle_conversion():
    try:
        # Get amount from entry field
        amount_in_usd = float(entry_amount.get())
        # Get selected target currency
        selected_currency = dropdown_currency.get()
        # Fetch exchange rate
        exchange_rate = fetch_exchange_rate('USD', selected_currency)
        if exchange_rate is not None:
            # Convert amount and display result
            converted_amount = perform_conversion(amount_in_usd, exchange_rate)
            result_label.config(text=f"Converted Amount: {converted_amount:.2f} {selected_currency}")
        else:
            result_label.config(text="Conversion failed.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create and configure the main application window
def create_main_window():
    root = tk.Tk()
    root.title("USD Currency Converter")
    root.geometry("400x250")
    root.resizable(False, False)

    # Apply styling
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12), padding=5)
    style.configure("TEntry", font=("Arial", 12), padding=5)
    style.configure("TCombobox", font=("Arial", 12), padding=5)

    # Create and place frame and widgets
    frame = ttk.Frame(root, padding="20 20 20 20")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Instructions Label
    ttk.Label(frame, text="Enter the amount in USD and select the currency to convert to:", wraplength=350, 
              anchor=tk.W).grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 10), sticky=tk.W)

    ttk.Label(frame, text="Amount in USD:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    global entry_amount
    entry_amount = ttk.Entry(frame, width=20)
    entry_amount.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(frame, text="Convert to:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    available_currencies = ["EUR", "GBP", "JPY", "AUD", "CAD", "INR", "CHF", "CNY"]
    global dropdown_currency
    dropdown_currency = ttk.Combobox(frame, values=available_currencies, state="readonly", width=18)
    dropdown_currency.set(available_currencies[0])
    dropdown_currency.grid(row=2, column=1, padx=10, pady=5)

    convert_button = ttk.Button(frame, text="Convert", command=handle_conversion)
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

    global result_label
    result_label = ttk.Label(frame, text="Converted Amount: ", font=("Arial", 12, "bold"))
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    return root

# Run the application
if __name__ == "__main__":
    app = create_main_window()
    app.mainloop()
