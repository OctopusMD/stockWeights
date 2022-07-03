import yfinance as yf

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = yf.Ticker(self.symbol)
        self.history = self.data.history(period="max")
        self.closeChanges = []
        self.openChanges = []
        self.highChanges = []
        self.lowChanges = []
        self.volumeChanges = []

    def getChanges(self):
        for i in range(1, len(self.history.Close)):
            self.closeChanges.append(self.history.Close[i-1]/self.history.Close[i])

        for i in range(1, len(self.history.Open)):
            self.openChanges.append(self.history.Open[i-1]/self.history.Open[i])

        for i in range(1, len(self.history.High)):
            self.highChanges.append(self.history.High[i-1]/self.history.High[i])

        for i in range(1, len(self.history.Low)):
            self.lowChanges.append(self.history.Low[i-1]/self.history.Low[i])

        for i in range(1, len(self.history.Volume)):
            self.volumeChanges.append(self.history.Volume[i-1]/self.history.Volume[i])

    @staticmethod
    def matchStocks(stock1, stock2, time=100):
        comparisions = []

        for i in range(0, time):
            closedCompare = stock1.closeChanges[-i]/stock2.closeChanges[-i]
            openCompare = stock1.openChanges[-i] / stock2.openChanges[-i]
            highCompare = stock1.highChanges[-i] / stock2.highChanges[-i]
            lowCompare = stock1.lowChanges[-i] / stock2.lowChanges[-i]
            volumeCompare = stock1.volumeChanges[-i] / stock2.volumeChanges[-i]

            if closedCompare > 100:
                closedCompare = 100 - (closedCompare - 100)
            if openCompare > 100:
                openCompare = 100 - (openCompare - 100)
            if highCompare > 100:
                highCompare = 100 - (highCompare - 100)
            if lowCompare > 100:
                lowCompare = 100 - (lowCompare - 100)
            if volumeCompare > 100:
                volumeCompare = 100 - (volumeCompare - 100)

            comparisions.append({"close": closedCompare, "open": openCompare, "high": highCompare, "low": lowCompare, "volume": volumeCompare})

        return comparisions