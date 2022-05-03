import main
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.ttk import Combobox

# Count variable and initial tkinter gui initizialization
count = None
root = Tk()

# Screens created using frames
loginScreen = tk.Frame(root)
createAccountScreen = tk.Frame(root)
loginHelpScreen = tk.Frame(root)
dashboardScreen = tk.Frame(root)
makeReservationScreen = tk.Frame(root)
cancelReservationScreen = tk.Frame(root)

# Car Availability Arrays

# Screen size set
root.geometry("600x600")

#Images
img2 = Image.open('ModelCybertruck.jpg')
img3 = ImageTk.PhotoImage(Image.open('Model3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('ModelRoadster.jpg'))
img5 = ImageTk.PhotoImage(Image.open('ModelS.jpg'))
img6 = ImageTk.PhotoImage(Image.open('ModelX.jpg'))
img7 = ImageTk.PhotoImage(Image.open('ModelY.jpg'))
imageArray = [img2, img3, img4, img5, img6, img7]

# Login screen gui variables and functions stated here
# Username Entry Widgets
usernameText = tk.Entry(loginScreen)
usernameText.place(relx=0.5, rely=.425, anchor=CENTER)
usernameText.insert(0, 'Username')
usernameText.config(foreground='gray')
my_pic = Image.open("CompanyPic.png")
resized = my_pic.resize((200, 200), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
loginImage = Label(loginScreen, image=new_pic).place(relx=0.5, rely=.2, anchor=CENTER)

mypic = Image.open('CompanyPic.png')
resize = mypic.resize((300, 200), Image.ANTIALIAS)
newpic = ImageTk.PhotoImage(resize)
CarImage = Label(dashboardScreen, image=newpic)
CarImage.place(relx=0.5, rely=.55, anchor=CENTER)

# Password Entry Widgets
passwordText = tk.Entry(loginScreen)
passwordText.place(relx=0.5, rely=.5, anchor=CENTER)
passwordText.insert(0, 'Password')
passwordText.config(foreground='gray')
# Login buttons
loginButton = Button(loginScreen, text="Login", height=3, width=20, command=lambda: main.login(usernameText.get(), passwordText.get(), loginScreen, dashboardScreen, welcomeLabel, currentRentalLabel, currentRentalDetails, CarImage, imageArray)).place(relx=0.5, rely=.6, anchor=CENTER)
createButton = Button(loginScreen, text="Create an Account", height=3, width=20, command=lambda: main.createScreen(0, loginScreen, createAccountScreen, loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen)).place(relx=0.5, rely=.725, anchor=CENTER)
helpLoginButton = Button(loginScreen, text="Help", height=2, width=10,command=lambda: main.createScreen(2, loginScreen, createAccountScreen, loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen)).place(relx=0.50, rely=.90, anchor=CENTER)
loginScreen.pack(fill='both', expand=1)

# Help Screen from the login screen
helpLoginLabel = Label(loginHelpScreen, text="Help Menu:", font=('Helvatical bold', 15)).place(relx=.5, rely=0.1,
                                                                                               anchor=CENTER)
hLoginReturnButton = Button(loginHelpScreen, text="Back", height=2, width=10).place(relx=0, rely=0)
phoneNumberLoginLabel = Label(loginHelpScreen, text="214-696-9420", font=('Helvatical bold', 15)).place(relx=.5,
                                                                                                        rely=0.4,
                                                                                                        anchor=CENTER)

# Create new account screen with labels, text boxes, and button
dropMenu = StringVar()
dropMenu.set("City")
drop = OptionMenu(createAccountScreen, dropMenu, "1:Richardson", "2:Plano", "3:Irving", "4:Grapevine", "5:Flower Mound",
                  "6:Coppell", "7:Lewisville", "8:Sherman", "9:Southlake", "10:Denton", "11:Dallas")
drop.place(relx=0.5, rely=.8, anchor=CENTER)
createAccountLabel = Label(createAccountScreen, text="Create an Account", font=('Helvatical bold', 20)).place(relx=0.5,
                                                                                                              rely=.1,
                                                                                                              anchor=CENTER)


userFirstName = tk.Entry(createAccountScreen)
userFirstName.place(relx=0.5, rely=.2, anchor=CENTER)
userFirstName.insert(0, 'First Name')
userFirstName.config(foreground='gray')
userLastName = tk.Entry(createAccountScreen)
userLastName.place(relx=0.5, rely=.3, anchor=CENTER)
userLastName.insert(0, 'Last name')
userLastName.config(foreground='gray')
createUsernameText = tk.Entry(createAccountScreen)
createUsernameText.place(relx=0.5, rely=.4, anchor=CENTER)
createUsernameText.insert(0, 'Username')
createUsernameText.config(foreground='gray')
createPasswordText = tk.Entry(createAccountScreen)
createPasswordText.place(relx=0.5, rely=.5, anchor=CENTER)
createPasswordText.insert(0, 'Password')
createPasswordText.config(foreground='gray')
userAge = tk.Entry(createAccountScreen)
userAge.place(relx=0.5, rely=.6, anchor=CENTER)
userAge.insert(0, 'Age')
userAge.config(foreground='gray')
createEmailText = tk.Entry(createAccountScreen)
createEmailText.place(relx=0.5, rely=.7, anchor=CENTER)
createEmailText.insert(0, 'Email Address')
createEmailText.config(foreground='gray')
createAccountButton = Button(createAccountScreen, text="Create Account", height=3, width=20,
                             command=lambda: main.createAccount(createUsernameText.get(), createPasswordText.get(),
                                                                createEmailText.get(), userFirstName.get(), userLastName.get(), userAge.get(), dropMenu.get(), createAccountScreen, loginScreen)).place(relx=0.5, rely=.9,
                                                                                              anchor=CENTER)
createAccountBackButton = Button(createAccountScreen, text="Back", height=2, width=10,
                                 command=lambda: main.createScreen(1, loginScreen, createAccountScreen,
                                                                   loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen)).place(relx=0, rely=0)

helpLabel = Label(loginHelpScreen, text="Help Menu:", font=('Helvatical bold', 15)).place(relx=.5, rely=0.1,
                                                                                          anchor=CENTER)
hImage = Label(loginHelpScreen, image=new_pic).place(relx=0.5, rely=.2, anchor=CENTER)
hReturnButton = Button(loginHelpScreen, text="Back", height=2, width=10,
                       command=lambda: main.createScreen(3, loginScreen, createAccountScreen, loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen)).place(
    relx=0, rely=0)
emailLabel = Label(loginHelpScreen, text="Help@NorthTexasTesla.com", font=('Helvatical bold', 15)).place(relx=.5, rely=0.5,
                                                                                                  anchor=CENTER)


# Dashboard Screen Widgets
welcomeLabel=Label(dashboardScreen, text=f"Welcome, !", fg='black', font=("Helvetica", 15))
welcomeLabel.place(relx=0.5, rely=0.125, anchor=CENTER)
currentRentalLabel=Label(dashboardScreen, text="Your Current Rentals: ", fg='black', font=("Helvetica", 15))
currentRentalLabel.place(relx=0.325, rely=0.25)
currentRentalDetails = Label(dashboardScreen, text = '', fg = 'black', font = ("Helvetica", 13))
currentRentalDetails.place(relx=.1, rely=.3)
logoutButton=Button(dashboardScreen, text="Logout", fg='black', font= ("Times New Roman",12), command=lambda: main.createScreen(4, loginScreen, createAccountScreen,
                                                                   loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen)).place(relx=0.05, rely=0.03)
reservationButton=Button(dashboardScreen, text="Make a Reservation Now", fg='blue', font=("Times New Roman", 10), command=lambda: main.createScreen(5, loginScreen, createAccountScreen,
                                                                   loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen)).place(relx=0.2, rely=0.8)
cancelReservationButton=Button(dashboardScreen, text="Cancel a Reservation", fg='red', font=("Times New Roman", 10), command=lambda: main.createScreen(7, loginScreen, createAccountScreen,
                                                                   loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen)).place(relx=0.62, rely = 0.8)


# Make Reservation Screen
returnButton = Button(makeReservationScreen, text="Back", height=2, width=10, command=lambda: main.createScreen(6, loginScreen, createAccountScreen, loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen)).place(relx=0.05, rely=0.03)
teslaLabel = Label(makeReservationScreen, text='Making Reservation', fg='black', font= ('Helvetia bold', 20)).place(relx=.3, rely=.15)
createReservation = Button(makeReservationScreen, text="Reserve", height=2, width=10, command=main.createReservation).place(relx=0.5, rely=0.6)

# Cancel Reservation Screen
returnButtonC = Button(cancelReservationScreen, text="Back", height=2, width=10, command=lambda: main.createScreen(8, loginScreen, createAccountScreen, loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen)).place(relx=0.05, rely=0.03)
CancelReservation = Button(cancelReservationScreen, text="Cancel Reservation", command=lambda: main.cancelReservation(cancelReservationScreen)).place(relx=0.42, rely=0.5)



# all following functions are used to clear the text within the box once clicked on (ex. gray text for "password"
# within box is removed once box is clicked)
def usernameCallback(event):
    usernameText.delete(0, END)
    return None


usernameText.bind("<Button-1>", usernameCallback)


def passwordCallback(event):
    passwordText.delete(0, END)
    return None


passwordText.bind("<Button-1>", passwordCallback)


def createUsernameCallback(event):
    createUsernameText.delete(0, END)
    return None


createUsernameText.bind("<Button-1>", createUsernameCallback)


def createPasswordCallback(event):
    createPasswordText.delete(0, END)
    return None


createPasswordText.bind("<Button-1>", createPasswordCallback)


def userFirstNameCallback(event):
    userFirstName.delete(0, END)
    return None


userFirstName.bind("<Button-1>", userFirstNameCallback)


def userLastNameCallback(event):
    userLastName.delete(0, END)
    return None


userLastName.bind("<Button-1>", userLastNameCallback)


def userAgeCallback(event):
    userAge.delete(0, END)
    return None


userAge.bind("<Button-1>", userAgeCallback)


def createEmailCallback(event):
    createEmailText.delete(0, END)
    return None


createEmailText.bind("<Button-1>", createEmailCallback)


def dcustomCallback(event):
    # dCustomEntry.delete(0, END)
    return None


# dCustomEntry.bind("<Button-1>", dcustomCallback)
root.mainloop()
