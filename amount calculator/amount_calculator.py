import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        P_n = float(entry_price.get())
        P_sl = float(entry_stop_loss.get())
        LM = float(entry_lm.get()) if entry_lm.get() else 0.2  # Use input value if provided, else default to 0.2
        M = money_in_position.get()
        L = leverage.get()
        
        if M and L:
            messagebox.showerror("Error", "Please enter only one of Money in Position or Leverage.")
            return
        elif not M and not L:
            messagebox.showerror("Error", "Please enter either Money in Position or Leverage.")
            return
        elif M:
            M = float(M)
            L = LM * P_n / (abs(P_n - P_sl) * M)
            A = M / P_n * L
        else:
            L = float(L)
            M = LM * P_n / (abs(P_n - P_sl) * L)
            A = M / P_n * L

        label_L.config(text=f"Leverage: {L}")
        label_A.config(text=f"Amount: {A}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create the main window
window = tk.Tk()
window.title("Amount Calculator")

# # Set window size and position
# window.geometry("400x300")
# window.resizable(False, False)

# Create input fields
label_price = tk.Label(window, text="Entry Price:")
label_price.grid(row=0, column=0, padx=5, pady=5)
entry_price = tk.Entry(window)
entry_price.grid(row=0, column=1, padx=5, pady=5)

label_stop_loss = tk.Label(window, text="Stop Loss Price:")
label_stop_loss.grid(row=1, column=0, padx=5, pady=5)
entry_stop_loss = tk.Entry(window)
entry_stop_loss.grid(row=1, column=1, padx=5, pady=5)

label_lm = tk.Label(window, text="LM (default 0.2):")
label_lm.grid(row=2, column=0, padx=5, pady=5)
entry_lm = tk.Entry(window)
entry_lm.grid(row=2, column=1, padx=5, pady=5)

label_M = tk.Label(window, text="Money in Position:")
label_M.grid(row=3, column=0, padx=5, pady=5)
money_in_position = tk.Entry(window)
money_in_position.grid(row=3, column=1, padx=5, pady=5)

label_L = tk.Label(window, text="Leverage:")
label_L.grid(row=4, column=0, padx=5, pady=5)
leverage = tk.Entry(window)
leverage.grid(row=4, column=1, padx=5, pady=5)

# Create buttons
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

label_A = tk.Label(window, text="Amount:")
label_A.grid(row=6, column=0, columnspan=2)

# Start the GUI
window.mainloop()
