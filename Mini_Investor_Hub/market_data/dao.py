import yfinance as yf

class MarketDataDAO:
    """
    Data Access Object for Market Data using yfinance API
    """
    def get_historical_data(self, tickers: list, start_date: str, end_date: str) -> dict:
        """
        Get historical data for a given ticker between two dates
        
        Args:
            ticker (list): List of ticker symbols
            start_date: str - Start date in format 'YYYY-MM-DD'
            end_date: str - End date in format 'YYYY-MM-DD'
        Returns:
            dict: Dictionary of tickers as keys and historical data as values
        """
        tickers_str = ' '.join(tickers)
        stocks = yf.Tickers(tickers_str)
        results = {}
        
        for ticker in tickers:
            data = stocks.tickers[ticker].history(start=start_date, end=end_date)
            if data.empty:
                results[ticker] = {"error": f"No data found for {ticker}"}
            else:
                results[ticker] = data.reset_index().to_dict(orient='records')
        
        return results
        
        
    def get_realtime_data(self, tickers: list) -> dict:
        """
        Get real-time data for a given ticker
        
        Args:
            tickers (list): List of ticker symbols
        Returns:
            dict: Dictionary of tickers as keys and real-time data as values
        """
        tickers_str = ' '.join(tickers)
        stocks = yf.Tickers(tickers_str)
        results = {}
        
        for ticker in tickers:
            data = stocks.tickers[ticker].history(period='1d')
            if data.empty:
                results[ticker] = {"error": f"No data found for {ticker}"}
            else:
                latest = data.tail(1).iloc[0]
                results[ticker] = {
                    # Feel free to add more real-time data fields here depending on features
                    "ticker": ticker,
                    "open": float(latest['Open']),
                    "close": float(latest['Close']),
                    "high": float(latest['High']),
                    "low": float(latest['Low']),
                    "volume": int(latest['Volume']),
                    "timestamp": latest.name.strftime('%Y-%m-%d %H:%M:%S')
                }
        
        return results
    
    def get_metadata(self, tickers: list) -> dict:
        """
        Get metadata for a given ticker
        
        Args:
            tickers (list): List of ticker symbols
        Returns:
            dict: Dictionary of tickers as keys and metadata as values
        """
        tickers_str = ' '.join(tickers)
        stocks = yf.Tickers(tickers_str)
        results = {}
        
        for ticker in tickers:
            data = stocks.tickers[ticker].info
            if data:
                results[ticker] = {
                    # Feel free to add more metadata fields here depending on features
                    "ticker": ticker,
                    "name": data.get("shortName", "N/A"),
                    "sector": data.get("sector", "N/A"),
                    "industry": data.get("industry", "N/A"),
                    "country": data.get("country", "N/A"),
                    "market_cap": data.get("marketCap", "N/A"),
                    "logo_url": data.get("logo_url", "N/A")
                }
            else:
                results[ticker] = {"error": f"No metadata found for {ticker}"}
        
        return results
                
        
        