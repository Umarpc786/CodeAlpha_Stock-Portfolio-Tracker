import streamlit as st


# ------------------------------------------
# Stock Prices
# ------------------------------------------

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 175,
    "AMZN": 185
}


# ------------------------------------------
# Page Configuration
# ------------------------------------------

st.set_page_config(
    page_title="Stock Portfolio Tracker",
    page_icon="📈",
    layout="centered"
)


# ------------------------------------------
# Application Title
# ------------------------------------------

st.title("📈 Stock Portfolio Tracker")

st.write(
    "Enter your stocks and quantities to calculate "
    "your total investment."
)


# ------------------------------------------
# Available Stocks
# ------------------------------------------

st.subheader("Available Stocks")

for stock, price in stock_prices.items():
    st.write(f"**{stock}** — ${price}")


st.divider()


# ------------------------------------------
# Portfolio Input
# ------------------------------------------

st.subheader("Add Stocks to Your Portfolio")

number_of_stocks = st.number_input(
    "How many different stocks do you want to add?",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)


portfolio = {}


for i in range(int(number_of_stocks)):

    st.markdown(f"### Stock {i + 1}")

    stock_name = st.selectbox(
        f"Select stock {i + 1}",
        list(stock_prices.keys()),
        key=f"stock_{i}"
    )

    quantity = st.number_input(
        f"Quantity of {stock_name}",
        min_value=1,
        value=1,
        step=1,
        key=f"quantity_{i}"
    )

    portfolio[stock_name] = quantity


# ------------------------------------------
# Calculate Portfolio
# ------------------------------------------

if st.button("Calculate Investment", type="primary"):

    total_investment = 0

    results = []

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]

        investment = price * quantity

        total_investment += investment

        results.append({
            "Stock": stock,
            "Price": price,
            "Quantity": quantity,
            "Investment": investment
        })


    # --------------------------------------
    # Portfolio Summary
    # --------------------------------------

    st.subheader("Portfolio Summary")

    for result in results:

        st.write(
            f"**{result['Stock']}** | "
            f"Price: ${result['Price']} | "
            f"Quantity: {result['Quantity']} | "
            f"Investment: ${result['Investment']}"
        )


    st.divider()

    st.metric(
        label="Total Investment",
        value=f"${total_investment}"
    )


    # --------------------------------------
    # Save Result
    # --------------------------------------

    file_content = "STOCK PORTFOLIO TRACKER\n"
    file_content += "=" * 40 + "\n\n"

    for result in results:

        file_content += (
            f"{result['Stock']} | "
            f"Price: ${result['Price']} | "
            f"Quantity: {result['Quantity']} | "
            f"Investment: ${result['Investment']}\n"
        )

    file_content += "\n"
    file_content += f"Total Investment: ${total_investment}\n"


    st.download_button(
        label="Download Portfolio Result",
        data=file_content,
        file_name="portfolio_result.txt",
        mime="text/plain"
    )
