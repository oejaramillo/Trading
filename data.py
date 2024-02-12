import yfinance as yf

# Par
par_monedas = 'EURUSD=X'
forex_data = yf.Ticker(par_monedas)

# Get the last 12 days of data
hist_data = forex_data.history(period="2d", interval="5m")

# Display the data
print(len(hist_data))


print("Hola Mundo")
