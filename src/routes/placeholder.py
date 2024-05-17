from fastapi import APIRouter
from src.db.redis import r
import requests
import json

router = APIRouter(prefix="/placeholder")


@router.get("/posts/{id}")
async def get_post(id: int):
    # On va d'abord chercher dans Redis si on a l'info
    cache = r.get(f"post:{id}")
    if cache:
        # Si on a l'info, tout va bien !
        return json.loads(cache)
    else:
        # Sinon, on va chercher dans l'API
        res = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
        # PUIS ! On oublie pas de sauvegarder dans Redis pour les prochaines fois
        r.set(f"post:{id}", res.text)
        return res.json()
