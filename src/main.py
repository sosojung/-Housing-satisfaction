from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

app = FastAPI()

templates = Jinja2Templates(directory="templates")

CSV_FILE_PATH = "live_satisfied.csv"

data = pd.read_csv(CSV_FILE_PATH)

@app.get("/")
def read_root(request: Request):
    table_html = data.to_html(index=False, escape=False, justify="center", border=1)
    return templates.TemplateResponse("index.html", {"request": request, "table_html": table_html})
    
@app.get("/infra")
def visualize_infra(request: Request):
    region = data['주거지역']
    
    living_infra = data['생활 인프라']

    fig = px.bar(
        x = region,
        y = living_infra,
        labels = {'x': '주거지역', 'y': '생활 인프라 만족도'},
    )
    fig.update_traces(marker_color="skyblue")

    graph_html = fig.to_html(full_html = False)

    return templates.TemplateResponse("infra.html", {"request": request, "graph_html": graph_html})

@app.get("/traffic")
def visualize_infra(request: Request):
    region = data['주거지역']
    
    living_infra = data['대중교통']

    fig = px.bar(
        x = region,
        y = living_infra,
        labels = {'x': '주거지역', 'y': '대중교통 만족도'},
    )
    fig.update_traces(marker_color="blue")

    graph_html = fig.to_html(full_html = False)

    return templates.TemplateResponse("traffic.html", {"request": request, "graph_html": graph_html})

@app.get("/crime")
def visualize_infra(request: Request):
    region = data['주거지역']
    
    living_infra = data['방범 상태']

    fig = px.bar(
        x = region,
        y = living_infra,
        labels = {'x': '주거지역', 'y': '방범 상태 만족도'},
    )
    fig.update_traces(marker_color="black")

    graph_html = fig.to_html(full_html = False)

    return templates.TemplateResponse("crime.html", {"request": request, "graph_html": graph_html})

@app.get("/clean")
def visualize_infra(request: Request):
    region = data['주거지역']
    
    living_infra = data['위생 환경']

    fig = px.bar(
        x = region,
        y = living_infra,
        labels = {'x': '주거지역', 'y': '위생 환경 만족도'},
    )
    fig.update_traces(marker_color="green")

    graph_html = fig.to_html(full_html = False)

    return templates.TemplateResponse("clean.html", {"request": request, "graph_html": graph_html})

@app.get("/green")
def visualize_infra(request: Request):
    region = data['주거지역']
    
    living_infra = data['녹지 공간']

    fig = px.bar(
        x = region,
        y = living_infra,
        labels = {'x': '주거지역', 'y': '녹지 공간 만족도'},
    )
    fig.update_traces(marker_color="gray")

    graph_html = fig.to_html(full_html = False)

    return templates.TemplateResponse("green.html", {"request": request, "graph_html": graph_html})

@app.get("/culture")
def visualize_infra(request: Request):
    region = data['주거지역']
    
    living_infra = data['문화 시설']

    fig = px.bar(
        x = region,
        y = living_infra,
        labels = {'x': '주거지역', 'y': '문화 시설 만족도'},
    )
    fig.update_traces(marker_color="orange")

    graph_html = fig.to_html(full_html = False)

    return templates.TemplateResponse("culture.html", {"request": request, "graph_html": graph_html})

@app.get("/education")
def visualize_infra(request: Request):
    region = data['주거지역']
    
    living_infra = data['교육 환경']

    fig = px.bar(
        x = region,
        y = living_infra,
        labels = {'x': '주거지역', 'y': '교육 환경 만족도'},
    )
    fig.update_traces(marker_color="yellow")

    graph_html = fig.to_html(full_html = False)

    return templates.TemplateResponse("education.html", {"request": request, "graph_html": graph_html})

@app.get("/naver")
def visualize_infra(request: Request):
    region = data['주거지역']
    
    living_infra = data['이웃 관계']

    fig = px.bar(
        x = region,
        y = living_infra,
        labels = {'x': '주거지역', 'y': '이웃 관계 만족도'},
    )
    fig.update_traces(marker_color="red")

    graph_html = fig.to_html(full_html = False)

    return templates.TemplateResponse("naver.html", {"request": request, "graph_html": graph_html})