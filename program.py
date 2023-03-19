import pickle

import train
import predict
import learn


def train_console():
    print("___________________________________________________________")
    print("Training the model")
    print("___________________________________________________________")
    print("TODO : Copy your data file and holidays file to data folder")
    print("___________________________________________________________")
    data = input("Enter your data file name (relative) : ")
    holidays = input("Enter your holidays file name (relative) : ")

    data = "data/" + data
    holidays = "data/" + holidays

    df = train.train_model(data, holidays)

    return df


def predict_console(df):
    print("___________________________________________________________")
    print("Ready to make predictions")
    isNotValid = True
    days = 0

    while (isNotValid):
        try:
            print('Enter for how many days you need the forecast :')
            days = int(input())
            isNotValid = False

        except:
            print('Enter a valid input....')

    model = pickle.load(open('model.pkl', 'rb'))

    predict.make_predictions(days,model,df)

    predict.make_predictions(days, model)



def learn_console():
    print("___________________________________________________________")
    print("Re-train the model with new data")
    print("___________________________________________________________")
    print("TODO : Copy your data files to data folder")
    print("___________________________________________________________")
    old_data = input("Enter your old data file name (relative) : ")
    new_data = input("Enter your new data file name (relative) : ")

    old_data = "data/" + old_data
    new_data = "data/" + new_data

    learn.learn(old_data, new_data)


def switch_console(option):
    if option == 1:
        train_console()
    elif option == 2:
        predict_console()
    elif option == 3:
        learn_console()
    else:
        print("Not a valid option")


def welcome_screen():
    print("Time Series Solution")
    print("Options : ")
    print("     1 - train the model")
    print("     2 - predict")
    print("     3 - learn")
    option = int(input("What do you want to do (enter the number) :"))
    switch_console(option)
