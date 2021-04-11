from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import yfinance as yf
import datetime

def get_stock_data(stock, dataShown):
    yf.pdr_override()

    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=dataShown)

    df = pdr.get_data_yahoo(stock, start=start_date, end=end_date)

    df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1)

    return df

# (Max price - lowest price) * golden ratio + lowest price
def fibonacci(yCoords):
    # Collect the amount of X positons there are
    theXs = []
    for j in range(0, len(yCoords)):
        theXs.append(j)
    # Find the highest price and lowest price
    maxPrice = max(yCoords)
    minPrice = min(yCoords)
    goldenNums = [0.382, 0.50, 0.618, 0.236]
    goldenNums.sort(reverse=True)
    maxPriceList = [maxPrice] * len(yCoords)
    minPriceList = [minPrice] * len(yCoords)
    # Plot the 100% fibonacci ceiling
    plt.plot(theXs, maxPriceList, "--", label=('100% - $' + str(round(maxPrice, 2))))
    for i in range(0, len(goldenNums)):
        evalu = (maxPrice - minPrice) * goldenNums[i] + minPrice
        theYs = [evalu] * len(yCoords)
        plt.plot(theXs, theYs, "--", label=(str(goldenNums[i]) + '% - $' + str(round(evalu, 2))))
    # Plot the 0% fibonacci ceiling
    plt.plot(theXs, minPriceList, "--", label='0% - $' + str(round(minPrice, 2)))

# Main
def main():
    # download data from yahoo finance
    print("Welcome! Please either enter the stock ticker (from yahoo finance)")
    stock = input("")

    print("Please enter how many days you would want to view.")
    dataShown = input()
    dataShown = int(dataShown)

    df = get_stock_data(stock, dataShown)
    index = df.index

    # Used to display the max amout of viewable days
    number_of_rows = len(index)

    # Label the x and y axis
    plt.xlabel('Days')
    plt.ylabel('Closes')

    # Creates the graph and plots the
    # Closing price
    xCoords = []
    yCoords = []

    x = 0
    for i in range(number_of_rows - dataShown, number_of_rows):
        try:
            y = df['Adj Close'][i]
        except:
            y = (df['Adj Close'][i + 1] + df['Adj Close'][i - 1]) / 2
        xCoords.append(x)
        yCoords.append(y)
        x = x + 1

    # Formats the graph
    plt.title("Fibonacci Retracements")
    plt.tick_params(axis='x', which='major', labelsize=8)
    plt.tick_params(axis='y', which='major', labelsize=8)

    # Connects the points
    plt.plot(xCoords, yCoords, 'g', label='Market')
    fibonacci(yCoords)
    # Displays the graph
    plt.legend()
    plt.show()
    main()


main()