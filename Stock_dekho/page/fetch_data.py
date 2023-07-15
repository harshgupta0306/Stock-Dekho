import yfinance as yf 
import pandas as pd
import json     
import plotly.graph_objects as go
from plotly.graph_objs import *
import os 
def fetch(sname):
    data_stock  = yf.download(sname,period="1y")
    yf.Tickers
    data = pd.DataFrame(data_stock).reset_index()

    
    layout = Layout(
        paper_bgcolor='#393939',
        plot_bgcolor='#393939',
        margin=go.layout.Margin(
                l=10, #left margin
                r=5, #right margin
                b=5, #bottom margin
                t=30, #top margin
                ),
        hoverlabel=go.layout.Hoverlabel(
        # bgcolor="#696969"
        ))
    fig = go.Figure(data=[
                    go.Candlestick(x=data["Date"],
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'])],layout=layout
                    )
    dt_all = pd.date_range(start=data['Date'].iloc[0],end=data['Date'].iloc[-1], freq = '1d')
    dt_obs = [d.strftime("%Y-%m-%d %H:%M:%S") for d in data['Date']]
    dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d %H:%M:%S").tolist() if not d in dt_obs]
    # print(dt_all)
    fig.update_xaxes(rangebreaks=[dict( values=dt_breaks)],
                     rangeslider_yaxis_rangemode="auto")
    fig.update_layout(font = dict(color = '#ffffff'))
    fig.update_coloraxes()
    print(os.getcwd())
    fig.write_html(os.getcwd()+"\\page\\templates\\plot.html")
    
    last_date_data = [data["Date"].iloc[-1].strftime("%Y-%m-%d"),
                      round(data["Open"].iloc[-1],2),
                      round(data["High"].iloc[-1],2),
                      round(data["Low"].iloc[-1],2),
                      round(data["Close"].iloc[-1],2),
                      round(max(data["Close"].max(),data["Open"].max(),data["High"].max(),data["Low"].max()),2),
                      round(min(data["Close"].min(),data["Open"].min(),data["High"].min(),data["Low"].min()),2)
                      ]
   
    return last_date_data

