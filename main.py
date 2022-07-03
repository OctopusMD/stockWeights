from Stock import Stock
if __name__ == '__main__':
    test1 = Stock("F")
    test1.getChanges()
    test2 = Stock("GE")
    test2.getChanges()
    comp = Stock.matchStocks(test1, test2)
    print("Test")
