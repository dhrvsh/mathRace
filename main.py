# pip install matplotlib
# pip install customtkinter

import matplotlib.pyplot as plt
import customtkinter

mainy = 85
addition = 30

inputScreen = customtkinter.CTk()
inputScreen.geometry("600x"+str(mainy+addition*8))
inputScreen.resizable(False, False)
inputScreen.title("Project Castor")

title = customtkinter.CTkLabel(inputScreen, text="Project Castor", fg_color="transparent", font=('Cartograph CF', 35)).place(x=150, y=20)

xx = 250
lbl = 50

def saveVars():
    x = [int(x1entry.get()),int(x2entry.get()),int(x3entry.get()),int(x4entry.get()),int(x5entry.get())]
    y = [int(y1entry.get()),int(y2entry.get()),int(y3entry.get()),int(y4entry.get()),int(y5entry.get())]

    plt.plot(x, y)

    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.title('Plotted Graph')
    plt.xlabel('x axis')
    plt.ylabel('y axis')

    plt.grid(True)

    inputScreen.destroy()
    plt.show()


firstlabel = customtkinter.CTkLabel(inputScreen, text="First X and Y values: ", fg_color="transparent", font=('Cartograph CF', 15)).place(x=lbl, y=mainy)
secondlabel = customtkinter.CTkLabel(inputScreen, text="Second X and Y values: ", fg_color="transparent", font=('Cartograph CF', 15)).place(x=lbl, y=mainy+addition)
thirdlabel = customtkinter.CTkLabel(inputScreen, text="Third X and Y values: ", fg_color="transparent", font=('Cartograph CF', 15)).place(x=lbl, y=mainy+addition*2)
fourthlabel = customtkinter.CTkLabel(inputScreen, text="Fourth X and Y values: ", fg_color="transparent", font=('Cartograph CF', 15)).place(x=lbl, y=mainy+addition*3)
fifthlabel = customtkinter.CTkLabel(inputScreen, text="Fifth X and Y values: ", fg_color="transparent", font=('Cartograph CF', 15)).place(x=lbl, y=mainy+addition*4)

x1entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter first X", width=150)
x1entry.place(x=xx, y=mainy)

x2entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter second X", width=150)
x2entry.place(x=xx, y=mainy+addition)

x3entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter third X", width=150)
x3entry.place(x=xx, y=mainy+addition*2)

x4entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter fourth X", width=150)
x4entry.place(x=xx, y=mainy+addition*3)

x5entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter fifth X", width=150)
x5entry.place(x=xx, y=mainy+addition*4)


y1entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter first Y", width=150)
y1entry.place(x=xx+160, y=mainy)

y2entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter second Y", width=150)
y2entry.place(x=xx+160, y=mainy+addition)

y3entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter third Y", width=150)
y3entry.place(x=xx+160, y=mainy+addition*2)

y4entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter fourth Y", width=150)
y4entry.place(x=xx+160, y=mainy+addition*3)

y5entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter fifth Y", width=150)
y5entry.place(x=xx+160, y=mainy+addition*4)

plotGraph = customtkinter.CTkButton(inputScreen, text="Plot the Graph", font=('Cartograph CF', 20), command=saveVars)
plotGraph.place(x=210, y=mainy+addition*5+20)

inputScreen.mainloop()

