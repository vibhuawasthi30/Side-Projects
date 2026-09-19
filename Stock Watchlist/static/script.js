var input = document.getElementById("stockInput");
var button = document.getElementById("addButton");
var list = document.getElementById("stockList");
const existingSymbols = new Set();

function createStockLi(stock){
    var li = document.createElement("li");
    existingSymbols.add(stock["Symbol"]);

    var summaryDiv = document.createElement("div");
    summaryDiv.className = "summary";

    const currentPrice = stock["Current Price"] !== null ? stock["Current Price"].toFixed(2) : "N/A"; //ROunding 
    const percentChange = stock["Percent Change"] !== null ? stock["Percent Change"].toFixed(2) : "N/A"; // Rounding

    summaryDiv.textContent = `${stock["Symbol"]} $${currentPrice} ${percentChange}%`;
            
    // When Clicked
    var detailsDiv = document.createElement("div");
    detailsDiv.className = "details";
    detailsDiv.style.display = "none";

    // Rounding All The Number
    const previousClose = stock["Previous Close"] !== null ? stock["Previous Close"].toFixed(2) : "N/A";
    const volume = stock["Stock Volume"] !== null ? stock["Stock Volume"].toLocaleString() : "N/A"; 
    const tenDayAvg = stock["Ten Day Average"] !== null ? stock["Ten Day Average"].toFixed(2) : "N/A";
    const marketCap = stock["Market Cap"] !== null ? stock["Market Cap"].toFixed(2) : "N/A";


    detailsDiv.innerHTML = `Previous Close: $${previousClose}<br>
                            Volume: ${volume}<br>
                            10-Day Avg: ${tenDayAvg}<br>
                            Market Cap: ${marketCap} `;
    
                            
    
    // Click Event
    summaryDiv.addEventListener("click", () => {
    detailsDiv.style.display = detailsDiv.style.display === "none" ? "block" : "none";
    });

    // Creating A Remove Button
    var removeBtn = document.createElement("button");
    removeBtn.textContent = "Remove"

    removeBtn.addEventListener("click", (e) => {
        e.stopPropagation();

        fetch("/remove_stock", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ symbol: stock["Symbol"] })
        })
        .then(() => {
            existingSymbols.delete(stock["Symbol"]);
            li.remove();
        });
    });

    li.appendChild(summaryDiv);
    li.appendChild(detailsDiv);
    li.appendChild(removeBtn);

    return li;
}


button.addEventListener("click", function(){
    var stockName = input.value.toUpperCase();

    if(existingSymbols.has(stockName))
    {
        alert("Stock already added");
        return;
    }

    if(stockName == "")
    {
        alert("Enter a stock name");
        return;
    }

    // Send Info Back TO Python
    fetch("/add_stock", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({symbol: stockName})
    })
        .then(res => res.json())
        .then(stock => {
            if (stock.error) {
                alert(stock.error);
                return;
            }

            list.appendChild(createStockLi(stock));
            input.value = "";
        
    });
});

fetch("/stocks")
    .then(response => response.json())
    .then(data =>{ console.log(data);  

        data.forEach(stock => {
            existingSymbols.add(stock["Symbol"]);
            list.appendChild(createStockLi(stock));
        });
    });
    
