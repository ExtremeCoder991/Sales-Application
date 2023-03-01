from tkinter import *
root=Tk()
root.title("C151 Project")
root.geometry("600x400")

label_month = Label(root)
label_profit = Label(root)
label_max_profit = Label(root)
label_min_profit = Label(root)

month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
profits = (10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000)
label_month["text"] = "Months: " + str(month)
label_profit["text"] = "Proft: " + str(profits)

def maxprofit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = month[max_profit_index]
    label_max_profit["text"] = "Maximum Profit of: " + str(max_profit) + " was given in the month of " + str(max_profit_month)
    
def minprofit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    min_profit_month = month[min_profit_index]
    label_min_profit["text"] = "Minimum Profit of: " + str(min_profit) + " was given in the month of " + str(min_profit_month)
    
label_month.place(relx = 0.5, rely = 0.2, anchor = CENTER)
label_profit.place(relx = 0.5, rely = 0.3, anchor = CENTER)
label_max_profit.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label_min_profit.place(relx = 0.5, rely = 0.7, anchor = CENTER)

btn_max = Button(root, text = "Show Max Profitable Month", command = maxprofit)
btn_min = Button(root, text = "Show Minimum Profitable Month", command = minprofit)

btn_max.place(relx = 0.5, rely = 0.4, anchor = CENTER)
btn_min.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()