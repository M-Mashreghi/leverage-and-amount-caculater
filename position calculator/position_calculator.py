import tkinter as tk

def calculate_position():
    try:
        P_n = float(entry_price.get())
        P_sl = float(entry_stop_loss.get())
        L = float(entry_leverage.get())
        LM = float(entry_loss_money.get())
        
        M = LM * P_n / (L * abs(P_n - P_sl))
        
        result_label.config(text=f"Money in Position: {M}$")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
window = tk.Tk()
window.title("Position Calculator without fee")

# Create labels and entry widgets
label_price = tk.Label(window, text="Entry Price:")
label_price.grid(row=0, column=0, padx=5, pady=5)
entry_price = tk.Entry(window)
entry_price.grid(row=0, column=1, padx=5, pady=5)

label_stop_loss = tk.Label(window, text="Stop Loss Price:")
label_stop_loss.grid(row=1, column=0, padx=5, pady=5)
entry_stop_loss = tk.Entry(window)
entry_stop_loss.grid(row=1, column=1, padx=5, pady=5)

label_leverage = tk.Label(window, text="Leverage (L):")
label_leverage.grid(row=2, column=0, padx=5, pady=5)
entry_leverage = tk.Entry(window)
entry_leverage.insert(0, "20")  # default value
entry_leverage.grid(row=2, column=1, padx=5, pady=5)

label_loss_money = tk.Label(window, text="Money Want to Lose (Default: 0.2$):")
label_loss_money.grid(row=3, column=0, padx=5, pady=5)
entry_loss_money = tk.Entry(window)
entry_loss_money.insert(0, "0.2")  # default value
entry_loss_money.grid(row=3, column=1, padx=5, pady=5)





# Button to calculate position
calculate_button = tk.Button(window, text="Calculate", command=calculate_position)
calculate_button.grid(row=4, columnspan=2)

# Label to display result
result_label = tk.Label(window, text="")
result_label.grid(row=5, columnspan=2)

window.mainloop()
