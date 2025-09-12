import matplotlib.pyplot as plt
import yfinance as yf


stocks = ["AAF", "BARC", "BATS", "EXPN", "GLEN", "HLMA", "ITM", "MNG", "NG"]

for stock in stocks:
    print(f'Getting data for stock: {stock}...')
    stock_data = yf.Ticker(f"{stock}.L")
    df = stock_data.history(period="60d")
    print(df)

    plt.figure(figsize=(10, 5))
    plt.bar(df.index, df['Close'], color='blue')
    plt.title(f'{stock} Trading Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.show()

