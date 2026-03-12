from contextlib import asynccontextmanager
from typing import Annotated, get_type_hints

from db import get_session, init_db
from fastapi import Depends, FastAPI, HTTPException, Path, Query
from models import Album, Band, BandCreate, GenreChoises
from sqlmodel import Session, select

"""
curl -X POST http://localhost:8000/bands/ \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Boards of Canada",
        "genre": "Electronic"
        }'
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/bands", status_code=206, response_model=list[Band])
async def bands(
    genre: GenreChoises | None = None, q: Annotated[str | None, Query(max_length=10)] = None, session: Session = Depends(get_session)
) -> list[Band]:

    band_list = session.exec(select(Band)).all()

    if genre:
        band_list = [b for b in band_list if b.genre.value.lower() == genre.value.lower()]

    if q:
        band_list = [b for b in band_list if q.lower() in b.name.lower()]
    return band_list


@app.get("/about")
async def about() -> str:
    return "Some gachi company"


@app.get("/bands/{band_id}", status_code=206, response_model=Band)
async def get_band_id(band_id: Annotated[int, Path(title="The band ID")], session: Session = Depends(get_session)) -> Band:
    band = session.get(Band, band_id)

    if band is None:
        raise HTTPException(404, "No page found")
    return band


@app.post("/bands", status_code=200, response_model=Band)
async def create_band(band_data: BandCreate, session: Session = Depends(get_session)) -> Band:
    band = Band(name=band_data.name, genre=band_data.genre)

    session.add(band)

    if band_data.albums:
        for album in band_data.albums:
            album_obj = Album(title=album.title, release_date=album.release_date, band=band)
            session.add(album_obj)

    session.commit()
    session.refresh(band)
    return band


# @app.get("/bands/genre/{genre}", status_code=206, response_model=list[Band])
# async def bands_for_genre(genre: GenreURLChoises) -> list[Band]:
#     result = [Band(**b) for b in BANDS if b["genre"] == genre]  # ...  b["genre"] == genre == b["genre"].value == genre.value
#     if len(result) == 0:
#         raise HTTPException(status_code=404, detail="No genres found")
#     return result
