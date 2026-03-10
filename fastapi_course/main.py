from fastapi import FastAPI, HTTPException

app = FastAPI()

BANDS = [
    {"id": 1, "name": "Blink 182", "genre": "pop rock"},
    {"id": 2, "name": "Oasis", "genre": "british rock"},
    {"id": 3, "name": "Kiss", "genre": "Glam rock"},
    {"id": 4, "name": "Wu-Tang Clan", "genre": "Hip-hop"},
]


@app.get("/bands")
async def index() -> list[dict]:
    return BANDS


@app.get("/about")
async def about() -> str:
    return "Some gachi company"


@app.get("/bands/{band_id}")
async def get_band_id(band_id: int) -> dict:
    band = next((b for b in BANDS if b["id"] == band_id), None)
    if band is None:
        raise HTTPException(404, "No page found")
    return band
