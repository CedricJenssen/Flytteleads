@echo off
start python -m http.server 5500
start uvicorn main:app --reload

