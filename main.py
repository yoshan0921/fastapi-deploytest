import uvicorn
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

world_population = {
    "India": 1433176492,
    "China": 1425499682,
    "U.S.A.": 340628952,
    "Indonesia": 278320971,
    "Pakistan": 242121515,
    "Nigeria": 225653847,
    "Brazil": 216845027,
    "Bangladesh": 173561086,
    "Russia": 144274364,
    "Mexico": 128779899,
    "Ethiopia": 127630621,
    "Japan": 123063036,
    "Philippines": 117950779,
    "Egypt": 113329472,
    "D.R. Congo": 103422181,
    "Vietnam": 99081069,
    "Iran": 89394240,
    "Turkey": 85970740,
    "Germany": 83279939,
    "Thailand": 71830722
}


@app.get("/population/")
async def population(country_name: Optional[str] = None, rank: Optional[int] = None):
    if country_name is None and rank is None:
        return {"message": "Please provide either country_name or rank"}

    # Country name is specified
    if country_name:
        if country_name not in world_population:
            return {"message": "Country name not found"}
        else:
            rank = list(world_population.keys()).index(country_name) + 1

    # Rank is specified
    elif rank:
        if rank > len(world_population):
            return {"message": "Please specify a number up to the 20th place."}
        else:
            country_name = list(world_population.keys())[rank - 1]

    return {
        "country_name": country_name,
        "rank": rank,
        "population": world_population[country_name]
        # "population": '{:,}'.format(world_population[country_name])
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="info")
