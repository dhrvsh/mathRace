import matplotlib.pyplot as plt
import customtkinter
from pyfonts import load_font

font = load_font(
    font_url=r"https://github.com/dhrvsh/mathRace/blob/main/Bricolage_Grotesque/BricolageGrotesque.ttf?raw=true"
)
inputScreen = customtkinter.CTk()
inputScreen.geometry("600x350")
inputScreen.resizable(False, False)
inputScreen.title("Project Castor")

title = customtkinter.CTkLabel(inputScreen, text="Project Castor", fg_color="transparent", font=('Cartograph CF', 35)).place(x=150, y=10)

# label = customtkinter.CTkLabel(inputScreen, text="CTkLabel", fg_color="transparent", font=("Cascadia Mono", 40)).place(x=0, y=0)

xx = 270

firstlabel = customtkinter.CTkLabel(inputScreen, text="First X and Y values: ", fg_color="transparent", font=('Cartograph CF', 15)).place(x=20, y=85)
secondlabel = customtkinter.CTkLabel(inputScreen, text="Second X and Y values: ", fg_color="transparent", font=('Cartograph CF', 15)).place(x=20, y=135)
thirdlabel = customtkinter.CTkLabel(inputScreen, text="Third X and Y values: ", fg_color="transparent", font=('Cartograph CF', 15)).place(x=20, y=185)

x1entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter first X", width=150)
x1entry.place(x=xx, y=85)

x2entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter second X", width=150)
x2entry.place(x=xx, y=135)

x3entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter third X", width=150)
x3entry.place(x=xx, y=185)


y1entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter first Y", width=150)
y1entry.place(x=xx+160, y=85)

y2entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter second Y", width=150)
y2entry.place(x=xx+160, y=135)

y3entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter third Y", width=150)
y3entry.place(x=xx+160, y=185)

inputScreen.mainloop()

x1 = int(input("Enter the first X value: "))
y1 = int(input("Enter the first Y value: "))

x2 = int(input("Enter the second X value: "))
y2 = int(input("Enter the second Y value: "))

x3 = int(input("Enter the third X value: "))
y3 = int(input("Enter the third Y value: "))


# x axis values
x = [x1,x2,x3]
# corresponding y axis values
y = [y1,y2,y3]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()