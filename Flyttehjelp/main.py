from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import csv
from pathlib import Path

app = FastAPI()

# Tillat frontend (juster hvis du hoster et domene senere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # Endre til frontend-URL i produksjon
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send-lead")
async def send_lead(
    from_address: str = Form(...),
    to_address: str = Form(...),
    date: str = Form(...),
    volume: str = Form(...),
    name: str = Form(...),
    contact: str = Form(...)
):
    filepath = Path("leads.csv")
    write_header = not filepath.exists()

    with open(filepath, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["Fra-adresse", "Til-adresse", "Dato", "Volum", "Navn", "Kontaktinfo"])
        writer.writerow([from_address, to_address, date, volume, name, contact])

    return {"message": "Lead mottatt, takk!"}
