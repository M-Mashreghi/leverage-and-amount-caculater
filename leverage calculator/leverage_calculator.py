import tkinter as tk

def calculate_leverage():
    try:
        P_n = float(entry_price.get())
        P_sl = float(entry_stop_loss.get())
        M = float(entry_money.get()) if entry_money.get() else 2
        LM = float(entry_loss_money.get()) if entry_loss_money.get() else 0.2
        
        leverage = LM * P_n / (M * abs(P_n - P_sl))
        label_result.config(text=f"Leverage: {leverage:.2f}")
    except ValueError:
        label_result.config(text="Please enter valid numbers")

# Create the main window
window = tk.Tk()
window.title("Leverage Calculator without fee")

# Create labels and entry widgets
label_price = tk.Label(window, text="Entry Price:")
label_price.grid(row=0, column=0, padx=5, pady=5)
entry_price = tk.Entry(window)
entry_price.grid(row=0, column=1, padx=5, pady=5)

label_stop_loss = tk.Label(window, text="Stop Loss Price:")
label_stop_loss.grid(row=1, column=0, padx=5, pady=5)
entry_stop_loss = tk.Entry(window)
entry_stop_loss.grid(row=1, column=1, padx=5, pady=5)

label_money = tk.Label(window, text="Money in Position (Default: 2$):")
label_money.grid(row=2, column=0, padx=5, pady=5)
entry_money = tk.Entry(window)
entry_money.grid(row=2, column=1, padx=5, pady=5)

label_loss_money = tk.Label(window, text="Money Want to Lose (Default: 0.2$):")
label_loss_money.grid(row=3, column=0, padx=5, pady=5)
entry_loss_money = tk.Entry(window)
entry_loss_money.grid(row=3, column=1, padx=5, pady=5)

# Button to calculate leverage
calculate_button = tk.Button(window, text="Calculate Leverage", command=calculate_leverage)
calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Label to display result
label_result = tk.Label(window, text="")
label_result.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
window.mainloop()
