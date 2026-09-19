import csv
import datetime
import yfinance as yf
from flask import Flask, jsonify, send_file, request
app = Flask(__name__)
stock_list = ["META", "AAPL", "TSLA"]
real_stock_list = []
dic_stock_list = []

def initialize_stocks():
    for symbol in stock_list:
        ticker = yf.Ticker(symbol)
        info = ticker.fast_info
        
        # Keeping real stocks
        if info.last_price and info.previous_close:
            real_stock_list.append(symbol)
        
        # Stock Price
        current_price = info.last_price 
        perious_close = info.previous_close
        #print(f"{item} Current Price: ${round(current_price, 2)}") 
        #print(f"{item} Previous Close: ${round(perious_close, 2)}")
            
        # Stock Change
        change = ((current_price - perious_close) / perious_close) * 100
        #print(f"{item} Change: %{round(change, 2)}")
        
            
        # Stock Volume
        stock_volume = info.last_volume 
        #print(f"{item} Last Volume: {round(stock_volume)}")
            
        # 10d Volume 
        ten_day_average = info.ten_day_average_volume
        #print(f"{item} 10-Day Average Volume: {round(ten_day_average)}")
            
        # Market Cap 
        market_cap = info.market_cap
        #print(f"{item} Market Cap: {round(market_cap)}")
            
            # Dictionary
        stock_record = {
                "Symbol": symbol,
                "Current Price": current_price,
                "Previous Close" : perious_close,
                "Percent Change": change,
                "Stock Volume": stock_volume,
                "Ten Day Average": ten_day_average,
                "Market Cap": market_cap
            }
        dic_stock_list.append(stock_record)
        
initialize_stocks()

# Sending Info To CSV 
with open('Stock_List.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for x in real_stock_list:
        writer.writerow([x])
                        
print("Stock List a successfully has been transfered to Stock_List.csv")
                
with open('Stock_Data.csv', 'w', newline='') as g:
    fieldnames = dic_stock_list[0].keys()
    writer = csv.DictWriter(g, fieldnames = fieldnames)
    writer.writeheader()
    for record in dic_stock_list:
        writer.writerow(record)
                        
print("Stock Data a successfully has been transfered to Stock_Data.csv")


@app.route("/remove_stock", methods=["POST"])
def remove_stock():
    symbol = request.json.get("symbol", "").upper()
    
    global real_stock_list, dic_stock_list
    real_stock_list = [s for s in real_stock_list if s != symbol]
    dic_stock_list = [d for d in dic_stock_list if d["Symbol"] != symbol]
    
    # Rewrite CSV
    with open("Stock_List.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for s in real_stock_list:
            writer.writerow([s])
    
    # Rewrite Stock_Data.csv
    if dic_stock_list:
        with open("Stock_Data.csv", "w", newline="") as g:
            writer = csv.DictWriter(g, fieldnames=dic_stock_list[0].keys())
            writer.writeheader()
            writer.writerows(dic_stock_list)
    return jsonify({"status": "removed", "symbol": symbol})

        
@app.route('/stocks')
def index():
    return jsonify(dic_stock_list)

@app.route('/')
def home():
    return send_file('index.html')

# User Input
@app.route('/add_stock', methods=["POST"])
def add_stock():
    symbol = request.json.get('symbol', '').upper()
    if symbol in real_stock_list:
        return jsonify({"error": "Stock Already Exits"})
    try: 
        stock = yf.Ticker(symbol)
        info1 = stock.fast_info
        current_price = info1.last_price
        perious_close = info1.previous_close
        if(current_price != None and perious_close != None and current_price > 0 and perious_close > 0 and perious_close != 0):
            pass
        else:
            print(f"Error")
    except Exception as e:
        print(f"{symbol} removed becuase of {e}")
    
    ticker = yf.Ticker(symbol)
    info = ticker.fast_info
    item = symbol
        
    # Stock Price
    current_price = info.last_price 
    perious_close = info.previous_close
    #print(f"{item} Current Price: ${round(current_price, 2)}") 
    #print(f"{item} Previous Close: ${round(perious_close, 2)}")
        
    # Stock Change
    change = ((current_price - perious_close) / perious_close) * 100
    #print(f"{item} Change: %{round(change, 2)}")
    
        
    # Stock Volume
    stock_volume = info.last_volume 
    #print(f"{item} Last Volume: {round(stock_volume)}")
        
    # 10d Volume 
    ten_day_average = info.ten_day_average_volume
    #print(f"{item} 10-Day Average Volume: {round(ten_day_average)}")
        
    # Market Cap 
    market_cap = info.market_cap
    #print(f"{item} Market Cap: {round(market_cap)}")
        
        # Dictionary
    stock_record = {
            "Symbol": item,
            "Current Price": current_price,
            "Previous Close" : perious_close,
            "Percent Change": change,
            "Stock Volume": stock_volume,
            "Ten Day Average": ten_day_average,
            "Market Cap": market_cap
        }
    dic_stock_list.append(stock_record)
    real_stock_list.append(item)
    
    return jsonify(stock_record)


if __name__ == "__main__":
    app.run(debug=True)

    
    