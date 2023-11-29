import pandas as pd
from thetadata import ThetaClient, OptionReqType, OptionRight, StockReqType, DateRange

# Set up ThetaData credentials
your_username = "your_username"
your_password = "your_password"

# Function to get option trades for a particular contract
def get_option_trades(root_ticker, exp_date, strike, start_date, end_date, opt_type=OptionRight.CALL) -> pd.DataFrame:
    client = ThetaClient(username=your_username, passwd=your_password)

    with client.connect():
        data = client.get_hist_option(
            req=OptionReqType.TRADE_QUOTE,
            root=root_ticker,
            exp=exp_date,
            strike=strike,
            right=opt_type,
            date_range=DateRange(start_date, end_date)
        )

    return data

# Main function to analyze options data
def analyze_options_data(root_ticker, exp_date, strike, start_date, end_date) -> None:
    # Get option trades
    option_trades = get_option_trades(root_ticker, exp_date, strike, start_date, end_date)

    # Print the option trades
    print(option_trades)

# Analyze options data for a particular underlying (e.g., MSFT) and date range
analyze_options_data('MSFT', '2023-01-01', 150, '2023-12-31')
