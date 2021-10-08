import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('StockWiz - Stock Price Predictor')
stocks = ('GOOG', 'AAPL', 'MSFT', 'TSLA','FB','NVDA','TWTR','HP','DELL')
selected_stock = st.selectbox('Select the stock which you want to predict ', stocks)
n_years = st.slider('Select the number of years for which you want the forecast ', 1, 5)
period = n_years * 365

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data



data_load_state = st.text('Please wait, loading your requested data.')

data = load_data(selected_stock)
data_load_state.text('Your data is loaded, it will take a while to compute the predictions!')

st.subheader('Here is a slice of your raw data')
st.write(data.head())


def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Plot of opening and closing stock values', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()


df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)


st.subheader('Predicted raw data')
st.write(forecast.head())

st.subheader(f'Interactive plot for {n_years} years')

fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

