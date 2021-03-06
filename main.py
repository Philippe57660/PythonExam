from fastapi import Request, FastAPI
from json import JSONDecodeError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from vehicules import Voiture, Bateau, Avion, Moto, v2, v3, v5, a1

app = FastAPI()

#1ère route : Une route qui va permettre de savoir si l'API est lancée -> FAIT
@app.get('/start')
async def getInfo(request: Request):
    try:
        data = await request.json()
        for i in data:
            print(i)
    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body'})
    except:
        return JSONResponse({'error': 'interne depuis le serveur'})
    print(f'{data}')
    return JSONResponse({'test': "test"})

#2ème route : Une route pour la création de véhicules(à vous de voir comment vous pouvez-faire pour chaque type) -> FAIT
@app.get('/add/voiture')
def ajoutVoiture():
    return "Ajout de voiture"

@app.get('/add/bateau')
def ajoutVoiture():
    return "Ajout de bateau"

@app.get('/add/avion')
def ajoutVoiture():
    return "Ajout d'avion"

@app.get('/add/moto')
def ajoutVoiture():
    return "Ajout de moto"

#3ème route : Une route pour le nombre total de véhicule -> FAIT
@app.get('/nbvehicules')
def getNombreTotal():
    return "Nombre de véhicules au total :", {Voiture.counter+Moto.counter+Avion.counter+Bateau.counter}

#4ème route : Une route qui permet de savoir pour un type de véhicule combien il y en a -> FAIT
@app.get('/nbvehicules/voitures')
def getNombreVoitures():
    return "Nombre de voitures : ", {Voiture.counter}

@app.get('/nbvehicules/bateaux')
def getNombreBateaux():
    return "Nombre de bateaux : ", {Bateau.counter}

@app.get('/nbvehicules/avions')
def getNombreBateaux():
    return "Nombre d'avions : ", {Avion.counter}

@app.get('/nbvehicules/motos')
def getNombreBateaux():
    return "Nombre de motos : ", {Moto.counter}


#5ème route : Une route qui va permettre de retrouver un véhicule par différent moyen(name, nombre km etc...)
@app.get('/km=20000')
def getNombreBateaux():
    return "Voici les véhicules ayant 20000km : ", {v2, v3, v5, a1}

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "endpoint not found" })
