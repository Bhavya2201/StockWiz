# StockWiz
StockWiz is a stock price predictor application, written in Python.
It makes use of python libraries which are mentioned below along with their purpose:

streamlit - to create an interactive interface <br />
yfinance - to fetch data of requested stock from Yahoo Finance <br />
FBProphet - Facebook's Prophet is a library for time series prediction <br />
plotly - to plot interactive plots of predicted values <br />

## Why FBProphet?

To fit the time series data, we need to depict the seasonalities and trends in the data we are goining to use. Also the popular methods like LSTM algorithm available in well-known frameworks like Tensorflow and PyTorch, mandates to individually train and evaluate a model for predicting various stocks and it is a time consumong process as each stock has different seasonalities and trends. <br />

Compared to the above, mentioned approach, FBProphet requires ledd time to fit and predict the data, providing results quickly and it's integration with plotly allows easily for us to create interactive, easy to comprehend plots.
