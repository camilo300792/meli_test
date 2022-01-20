from is_mutant import is_mutant
from fastapi import Request, Response, status, FastAPI

# data = json.loads('{"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}')
# data = json.loads('{"dna":["ATGCGA","CAGTGC","TTATTT","AGACGG","GCGTCA","TCACTG"]}')
app = FastAPI()

@app.get("/")
def index():
    return {
        "message": "Welcome to Xmen API!",
        "repository": "https://github.com/camilo300792/meli_test",
        "author": "Elias Camilo Martinez Salcedo"
    }

@app.post("/mutant", status_code=200)
async def mutant(request: Request, response: Response):
    data = await request.json()
    mutant = is_mutant(data['dna'])
    if mutant == False:
        response.status_code = status.HTTP_403_FORBIDDEN
    return {"is_mutant": mutant}
