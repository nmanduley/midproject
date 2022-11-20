import pandas as pd
from datetime import datetime
import requests
import plotly.graph_objs as go

# Visualization parameters
AXIS_FONT_SIZE = 20
FIG_HEIGHT = 400
FIG_WIDTH = 600
MIN_DATE = datetime.date(datetime(2020,1,22))
MAX_DATE = datetime.date(datetime(2021,4,10))


def get_db_name(database):
    if database == 'Muertes':
        db_name = 'deaths'
    elif database == 'Recuperados':
        db_name = 'recovered'
    else:
        db_name = 'confirmed'
    return db_name


def build_dataframe(res, date_range):
    MIN_DATE = date_range[0]
    MAX_DATE = date_range[1]
    data = res.json()
    raw =[list(data.keys()), list(data.values())]
    dates = [datetime.date(datetime.strptime(date_string, '%m/%d/%y')) for date_string in raw[0]]
    cases = [int(n) for n in raw[1]]

    df = pd.DataFrame([dates, cases]).T
    df.columns = ["Date", "Cases"]
    return df.loc[(df['Date']>=MIN_DATE) & (df['Date']<=MAX_DATE)]


def gen_figure(countries, date_range, chosen_db):
    db_name = get_db_name(chosen_db)
    fig = go.Figure()
    for country in countries:
        res = requests.get(f"http://127.0.0.1:8000/{db_name}/{country}")
        df = build_dataframe(res, date_range)
        fig.add_trace(go.Scatter(x=df["Date"], y=df["Cases"], name=country, mode='lines'))

    fig.update_yaxes(tickfont=dict(size=AXIS_FONT_SIZE))
    fig.update_xaxes(tickfont=dict(size=AXIS_FONT_SIZE))
    fig.update_layout(title=f"Numero total de {chosen_db.lower()} entre {date_range[0]} y {date_range[1]}",
        xaxis_title="Fecha",
        yaxis_title=f"{chosen_db}",
        legend_title="Paises:",
        font=dict(size=AXIS_FONT_SIZE)
        )
    return fig
