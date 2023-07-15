# Stock Forecasting App with ARIMA Model and Django

This repository contains a stock forecasting application built using the ARIMA (AutoRegressive Integrated Moving Average) model and Django framework. The application allows users to input stock data and obtain forecasted values based on the ARIMA model's predictions.

## Features

- **ARIMA Model:** The application utilizes the ARIMA model, a popular time series forecasting technique, to predict future stock prices based on historical data.
- **Interactive Web Interface:** The application provides a web-based interface built with Django, allowing users to interact with the ARIMA model easily.
- **Visualization:** The predicted stock values are visualized using charts, providing users with an intuitive representation of the forecasted trends.

## Installation

To set up the Stock Forecasting App, follow these steps:

1. Clone the repository:

   ```bash
   https://github.com/rahim-khan-iitg/stock_forecasting.git
   ```

2. Change to the project directory:

   ```bash
   cd stock_forecasting
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **Unix/Linux:**

     ```bash
     source venv/bin/activate
     ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Perform database migrations:

   ```bash
   python manage.py migrate
   ```

7. Run the application:

   ```bash
   python manage.py runserver
   ```

8. Access the Stock Forecasting App by visiting `http://localhost:8000` in your web browser.

## Usage

1. Open the Stock Forecasting App in your web browser.
2. Select the company name from the search box .
3. select the select the option what to forecast.
4. then click on the load data.

## Contributing

Contributions to the Stock Forecasting App are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or inquiries, please contact Rahim Khan at rahimkhan7627047457@gmail.com.

---

We hope you find this Stock Forecasting App useful! Enjoy forecasting stock prices with the power of ARIMA and Django!
