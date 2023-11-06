import tkinter as tk
from tkinter import ttk

# Set the base cost of the computer which includes basic components
BASE_COST = 200.00

# Define a dictionary of components with their codes, descriptions, and prices
components = {
    'cases': {
        'A1': {'description': 'Compact', 'price': 75.00},
        'A2': {'description': 'Tower', 'price': 150.00}
    },
    'rams': {
        'B1': {'description': '8 GB', 'price': 79.99},
        'B2': {'description': '16 GB', 'price': 149.99},
        'B3': {'description': '32 GB', 'price': 299.99}
    },
    'hdds': {
        'C1': {'description': '1 TB HDD', 'price': 49.99},
        'C2': {'description': '2 TB HDD', 'price': 89.99},
        'C3': {'description': '4 TB HDD', 'price': 129.99}
    },
    'ssds': {
        'D1': {'description': '240 GB SSD', 'price': 59.99},
        'D2': {'description': '480 GB SSD', 'price': 119.99}
    },
    'second_hdds': {
        'E1': {'description': '1 TB HDD', 'price': 49.99},
        'E2': {'description': '2 TB HDD', 'price': 89.99},
        'E3': {'description': '4 TB HDD', 'price': 129.99}
    },
    'optical_drives': {
        'F1': {'description': 'DVD/Blu-Ray Player', 'price': 50.00},
        'F2': {'description': 'DVD/Blu-Ray Re-writer', 'price': 100.00}
    },
    'operating_systems': {
        'G1': {'description': 'Standard Version', 'price': 100.00},
        'G2': {'description': 'Professional Version', 'price': 175.00}
    }
}

# Initialize the main window for our application
root = tk.Tk()
root.title("Computer Shop Customization")

# This function is triggered when the user clicks the 'Calculate Price' button
def calculate_total():
    total_cost = BASE_COST  # Start with the base cost of the computer
    additional_items_count = 0  # Counter for additional items
    
    selected_components = {}  # A dictionary to keep track of the selected items
    
    # Go through each category and sum the prices of selected items
    for category, var in dropdown_vars.items():
        selected_code = var.get()
        if selected_code != "None":  # Check if the user made a selection other than 'None'
            selected_components[category] = components[category][selected_code]
            total_cost += selected_components[category]['price']
            if category not in ['cases', 'rams', 'hdds']:  # These are considered basic components
                additional_items_count += 1  # Increment the counter for additional items

    # Calculate discounts based on the number of additional items purchased
    discount = 0
    if additional_items_count == 1:
        discount = 0.05 * total_cost
    elif additional_items_count >= 2:
        discount = 0.10 * total_cost
    
    # Subtract the discount from the total cost
    total_cost -= discount
    
    # Update the label with the total price after discount
    total_cost_label.config(text=f"Total Price after Discount: ${total_cost:.2f} (Saved: ${discount:.2f})")

    # Display a summary of selected components
    summary = f"Base Cost: ${BASE_COST:.2f}\n"
    for category, component in selected_components.items():
        summary += f"{category.capitalize()}: {component['description']} - ${component['price']:.2f}\n"
    summary += f"Discount Applied: -${discount:.2f}\n"
    summary += f"Total Cost after Discount: ${total_cost:.2f}"

    summary_text.delete("1.0", tk.END)  # Clear the previous summary
    summary_text.insert(tk.END, summary)  # Insert the new summary

# Function to create a dropdown menu for selecting components
def create_dropdown(label_text, options, row):
    label = ttk.Label(frame, text=label_text)
    label.grid(column=0, row=row, sticky=tk.W, padx=5, pady=5)

    variable = tk.StringVar(frame)
    # Start with 'None' to not select anything by default
    variable.set('None')
    dropdown = ttk.OptionMenu(frame, variable, *['None'] + list(options.keys()))
    dropdown.grid(column=1, row=row, sticky=tk.W, padx=5, pady=5)
    
    return variable

# Create a frame to organize the widgets in the window
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a dictionary to keep track of the dropdown variables
dropdown_vars = {}

# Create dropdown menus for each category of components
for i, (category, items) in enumerate(components.items()):
    dropdown_vars[category] = create_dropdown(category.capitalize(), items, i)

# Create a button to calculate the total price
calculate_button = ttk.Button(frame, text="Calculate Price", command=calculate_total)
calculate_button.grid(column=1, row=len(components)+1, sticky=tk.W, padx=5, pady=5)

# Label to display the total price after discount
total_cost_label = ttk.Label(frame, text="Total Price after Discount: $0.00")
total_cost_label.grid(column=0, row=len(components)+2, columnspan=2, sticky=tk.W, padx=5, pady=5)

# Create a text widget to display a summary of selected components and the final price
summary_text = tk.Text(frame, width=50, height=10, wrap="word")
summary_text.grid(column=0, row=len(components)+3, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=5)

# Start the GUI event loop to wait for user input
root.mainloop()
