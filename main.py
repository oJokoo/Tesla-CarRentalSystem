from tkinter import messagebox
from tkinter import *
import mysql.connector
from PIL import ImageTk, Image
import time

db = mysql.connector.connect(
    host = "127.0.0.1",
    user= "root",
    passwd = "1234",
    database = 'car rental',
    auth_plugin='mysql_native_password')

mycursor = db.cursor(buffered=True)
mycursor.execute('SELECT * FROM customer')
for x in mycursor:
    print(x)

# global variables defined here
username = ''
password = ''
email = ''
balance = ''
enterBalance = ''
id = ''
userExistCheck = []
loginSuccess = []
currentRentals = ''
count = 0
usernameLab = ''
emailLab = ''
carDetails = ''
imagesArray = ['ModelCybertruck', 'Model3', 'ModelRoadster', 'ModelS', 'ModelX', 'ModelY']

def login(username, password, loginScreen, dashboardScreen, welcomeLabel, rentLabel, rentDetails, carImage, imageArray):
    global customerID
    global usernameU
    global passwordU
    global carDetails
    global carimage
    global imagearray
    global currentRentals
    global rentdetails
    global rentlabel
    global currentRentalsCount
    global userName
    global passWord
    userName = username
    passWord = password
    currentRentalsCount = []
    rentlabel = rentLabel
    carimage = carImage
    imagearray = imageArray
    rentdetails = rentDetails
    passwordU = password
    usernameU = username
    carImage.config(image='')
    rentDetails.config(text = '')
    mycursor.execute(f'SELECT first_name FROM customer WHERE user_name = \'{username}\' AND passwd = \'{password}\'')
    for x in mycursor:
        loginSuccess.append(x)
    if not loginSuccess:
        messagebox.showerror('Error', 'Invalid Login')
        loginSuccess.clear()
        return
    codeZ = str(loginSuccess[0])
    index1 = codeZ.find("'")
    index2 = codeZ[index1 + 1:].find("'")
    firstname = codeZ[index1 + 1:index2 + 2]
    if firstname:
        loginScreen.forget()
        dashboardScreen.pack(fill = 'both', expand = 1)
        welcomeLabel.config(text = f'Welcome {firstname}!')
        mycursor.execute(f'SELECT current_rentals FROM customer WHERE user_name = \'{username}\' AND passwd = \'{password}\'')
        for x in mycursor:
            currentRentalsCount.append(x)
        rentals = str(currentRentalsCount[0])
        rentalCount = rentals[2]
        rentLabel.config(text = f'Your Current Rentals: {rentalCount}')
        mycursor.execute(f'SELECT id FROM customer WHERE user_name = \'{username}\' AND passwd = \'{password}\'')
        for x in mycursor:
            customerIDs = x
        customerID = x[0]
        try:
            mycursor.execute(f'SELECT year, make, model, city, dateRented FROM cars, customer, currentrentals, location WHERE \'{customerID}\' = currentrentals.customerID AND currentrentals.carID = cars.car_id AND location.cityID = cars.locationID')
            for x in mycursor:
                currentRentals = x
            carDetails = f'Model{currentRentals[2]}'
            print(carDetails)
            for index in range(len(imagesArray)):
                if imagesArray[index] == carDetails:
                    carImage.config(image=imageArray[index])
                    pass
            rentDetails.config(text = f'{currentRentals[0]} {currentRentals[1]} Model {currentRentals[2]} rented from {currentRentals[3]} on {currentRentals[4]}')
        except:
            pass
        loginSuccess.clear()
        currentRentalsCount.clear()
        currentRentals = ''
        carDetails = ''
        return
    else:
        loginSuccess.clear()
        return
def createAccount(username, password, email, firstName, lastName, age, country, createAccountScreen, loginScreen):
    if not firstName or firstName == 'First Name':
        messagebox.showerror('Error', 'Invalid First Name: Enter a first name')
        return
    if not lastName or lastName == 'Last name':
        messagebox.showerror('Error', 'Invalid Last Name: Enter a last name')
        return
    mycursor.execute(f'SELECT * FROM CUSTOMER WHERE user_name=\'{username}\'')
    for x in mycursor:
        userExistCheck.append(x)
    if userExistCheck:
        messagebox.showerror('Error', 'Invalid Username: Username already taken')
        userExistCheck.clear()
        return
    if not username or username == 'Username':
        messagebox.showerror('Error', 'Invalid Username: Enter a username')
        return
    if not password or password == 'Password':
        messagebox.showerror('Error', 'Invalid Password: Enter a password')
        return
    try:
        if int(age) < 21 or int(age) > 90:
            messagebox.showerror('Error', 'Valid Age to rent cars: 21-90: Account not created')
            return
    except:
        messagebox.showerror('Error', 'Please enter an age')
        return
    if ('@' not in email) or ('.' not in email):
        messagebox.showerror('Error', 'Invalid Email: Account not created.')
        return
    if country == 'Country':
        messagebox.showerror('Error', 'Invalid Country: Please choose a country option')
        return
    mycursor.execute("INSERT INTO customer(first_name, last_name, user_name, passwd, age, email, country_id, current_rentals) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (firstName, lastName, username, password, age, email, country[0], 0))

    mycursor.execute('SELECT * FROM customer')
    #for x in mycursor:
        #print(x)

    createScreen(1, loginScreen, createAccountScreen, 0)

def createReservation():
    CarSelection = dropMenuCars.get()
    if CarSelection == 'Tesla Model Not Available':
        messagebox.showerror('Error', 'Car Selection is not available.')
        return
    elif 'Tesla Model (\'Roadster\'' in CarSelection:
        model = CarSelection[14:22]
        year = CarSelection[25:29]
    else:
        model = CarSelection[14:15]
        year = CarSelection[18:22]
    mycursor.execute(f'UPDATE cars SET rented = 1 WHERE model = \'{model}\' AND year = \'{year}\'')
    mycursor.execute(f'UPDATE customer SET current_rentals = 1 WHERE user_name = \'{userName}\' AND passwd = \'{passWord}\'')
    mycursor.execute(f'SELECT * from customer')
    for x in mycursor:
        print(x)
    mycursor.execute(f'SELECT car_id FROM cars WHERE model = \'{model}\' AND year = \'{year}\'')
    for x in mycursor:
        car_id = x
    car_id_stringz = str(car_id)
    car_id_string = car_id_stringz[1:2]
    currentDate = time.strftime("%m/%d/%Y")
    try:
        mycursor.execute(f'INSERT INTO currentrentals(customerID, carID, dateRented) VALUES (%s, %s, %s)', (customerID, car_id_string, currentDate))
        mycursor.execute('Select * FROM currentrentals')
    except:
        mycursor.execute(f'UPDATE cars SET rented = 0 WHERE model = \'{model}\' AND year = \'{year}\'')
        messagebox.showerror('Error', 'Only one reservation allowed at a time per customer.')
        return
    mycursor.execute(f'SELECT year, make, model, city, dateRented FROM cars, customer, currentrentals, location WHERE \'{customerID}\' = currentrentals.customerID AND currentrentals.carID = cars.car_id AND location.cityID = cars.locationID')
    for x in mycursor:
        currentRentals = x
    carDetails = f'Model{currentRentals[2]}'
    for index in range(len(imagesArray)):
        if imagesArray[index] == carDetails:
            carimage.config(image=imagearray[index])
            pass
    rentdetails.config(text=f'{currentRentals[0]} {currentRentals[1]} Model {currentRentals[2]} rented from {currentRentals[3]} on {currentRentals[4]}')
    mycursor.execute(f'SELECT current_rentals FROM customer WHERE user_name = \'{userName}\' AND passwd = \'{passWord}\'')
    for x in mycursor:
        currentRentalsCount.append(x)
    rentals = str(currentRentalsCount[0])
    rentalCount = rentals[2]
    rentlabel.config(text = f'Your Current Rentals: {rentalCount}')

def cancelReservation(ReservationScreen):
    print()

def createScreen(screenNumber, loginScreen, createAccountScreen, loginHelpScreen, dashboardScreen, makeReservationScreen, cancelReservationScreen):
    global dropMenuCars
    global dropCars
    global i
    global availableCars
    availableCars = ['Not Available', 'Not Available', 'Not Available', 'Not Available', 'Not Available', 'Not Available',
                     'Not Available', 'Not Available', 'Not Available', 'Not Available']
    i=0
    if screenNumber == 0:
        loginScreen.forget()
        createAccountScreen.pack(fill='both', expand=1)
    elif screenNumber == 1:
        createAccountScreen.forget()
        loginScreen.pack(fill='both', expand=1)
    elif screenNumber == 2:
        loginScreen.forget()
        loginHelpScreen.pack(fill='both', expand=1)
    elif screenNumber == 3:
        loginHelpScreen.forget()
        loginScreen.pack(fill='both', expand=1)
    elif screenNumber == 4:
        dashboardScreen.forget()
        loginScreen.pack(fill = 'both', expand = 1)
    elif screenNumber == 5:
        mycursor.execute('SELECT model, year, city FROM cars, location WHERE cars.locationID = cityID AND rented = 0')
        for x in mycursor:
            availableCars[i] = x
            i += 1
        for i in range(len(availableCars), 10):
            availableCars[i] = 'Not Available'
        dropMenuCars = StringVar()
        dropMenuCars.set("Car Reservation")
        dropCars = OptionMenu(makeReservationScreen, dropMenuCars, f'Tesla Model {availableCars[0]}',
                              f'Tesla Model {availableCars[1]}', f'Tesla Model {availableCars[2]}',
                              f'Tesla Model {availableCars[3]}', f'Tesla Model {availableCars[4]}',
                              f'Tesla Model {availableCars[5]}', f'Tesla Model {availableCars[6]}',
                              f'Tesla Model {availableCars[7]}', f'Tesla Model {availableCars[8]}',
                              f'Tesla Model {availableCars[9]}')
        dropCars.place(relx=0.5, rely=.3, anchor=CENTER)
        dashboardScreen.forget()
        makeReservationScreen.pack(fill = 'both', expand = 1)
        availableCars.clear()
    elif screenNumber == 6:
        dropCars.destroy()
        makeReservationScreen.forget()
        dashboardScreen.pack(fill = 'both', expand = 1)
    elif screenNumber == 7:
        dashboardScreen.forget()
        print(customerID)
        mycursor.execute(f'SELECT year, make, model, city, dateRented FROM cars, customer, currentrentals, location WHERE id = \'{customerID}\' AND currentrentals.carID = cars.car_id AND location.cityID = cars.locationID')
        for x in mycursor:
            print(x)
        dropMenuReservations = StringVar()
        dropMenuReservations.set("Car Reservation")
        dropReservations = OptionMenu(cancelReservationScreen, dropMenuReservations)
        cancelReservationScreen.pack(fill = 'both', expand = 1)
    elif screenNumber == 8:
        cancelReservationScreen.forget()
        dashboardScreen.pack(fill = 'both', expand = 1)

