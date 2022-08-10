import smogn
import pandas
import seaborn
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def btncommand():
    try:
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        product = pandas.read_csv(file_path)

        product_smogn = smogn.smoter(
            data = product,
            y = Entry1.get()
        )

        print("PRODUCT_SHAPE: ", product.shape)

        print("PRODUCT_SMOGN.SHAPE: " ,product_smogn.shape)


        print(smogn.box_plot_stats(product[Entry1.get()])['stats'])

        print(smogn.box_plot_stats(product_smogn[Entry1.get()])['stats'])

        seaborn.kdeplot(product[Entry1.get()], label="ORIGINAL")
        seaborn.kdeplot(product_smogn[Entry1.get()], label="MODIFIED")
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", e)

root = Tk()
root.title("SMOGN Algorithm Test GUI")
root.geometry("400x400")

Label1 = Label(root, text="SMOGN Algorithm Test GUI")
Label1.pack()

Entry1 = Entry(root, width=30, border=1, relief='solid')
Entry1.pack()

Button1 = Button(root, text="EXECUTE", command=btncommand)
Button1.pack()

root.mainloop()