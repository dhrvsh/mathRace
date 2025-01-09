import matplotlib.pyplot as plt
import customtkinter
from pyfonts import load_font

font = load_font(
    font_url=r"D:\MajorProjects\mathRace\mathRace\Bricolage_Grotesque\BricolageGrotesque.ttf"
)
inputScreen = customtkinter.CTk()
inputScreen.geometry("600x350")
inputScreen.resizable(False, False)
inputScreen.title("Project Castor")

title = customtkinter.CTkLabel(inputScreen, text="Project Castor", fg_color="transparent", font=('Cartograph CF', 40)).place(x=200, y=10)

# label = customtkinter.CTkLabel(inputScreen, text="CTkLabel", fg_color="transparent", font=("Cascadia Mono", 40)).place(x=0, y=0)

x1entry = customtkinter.CTkEntry(inputScreen, placeholder_text="Enter first X", width=250)
x1entry.place(x=0, y=75)

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