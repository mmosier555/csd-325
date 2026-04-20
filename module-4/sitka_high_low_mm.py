import csv
from datetime import datetime

from matplotlib import pyplot as plt
import sys

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)


    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])  # TMAX column
        low = int(row[6]) #TMIN column 
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

def plot_highs(dates, highs):
    plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.title("Daily High Temperatures")
    plt.gcf().autofmt_xdate()
    plt.show()

def plot_lows(dates, lows):
    plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, lows, c='blue')
    plt.title("Daily Low Temperatures") 
    plt.gcf().autofmt_xdate()
    plt.show()  

def main():
    while True:
        print("\nTemperature Menu")
        print("1. Highs")
        print("2. Lows")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice =='1':
            plot_highs(dates, highs)
        elif choice =='2':
            plot_lows(dates, lows)
        elif choice =='3':
            print("Exiting program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__== '__main__':
    main()
