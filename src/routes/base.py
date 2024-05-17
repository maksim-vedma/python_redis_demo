from fastapi import APIRouter
from src.db.redis import r
from src.models.keyval import Keyval, HashKeyval, ZetKeyval

router = APIRouter(prefix="/base")


@router.get("/ping")
async def ping():
    return r.ping()


# String ==============================
@router.get("/string/{key}")
async def string(key: str):
    return r.get(key)


@router.post("/string")
async def post_coucou(keyval: Keyval):
    return r.set(keyval.key, keyval.value)


@router.delete("/string/{key}")
async def string_del(key: str):
    return r.delete(key)


# Hash ==============================
@router.get("/hash/{key}")
async def hash_get(key: str):
    return r.hgetall(key)


@router.get("/hash/{name}/{field}")
async def hash_get_one_field(name: str, key: str):
    return r.hget(name, key)


@router.post("/hash")
async def hash_create(hash: HashKeyval):
    return r.hset(hash.key, hash.field, hash.value)


@router.get("/list/{key}")
async def list_get(key: str):
    return r.lrange(key, 0, -1)


@router.post("/list")
async def list_get_one_field(keyval: Keyval):
    return r.lpush(keyval.key, keyval.value)


#
@router.get("/set/{key}")
async def set_get(key: str):
    return r.smembers(key)


@router.post("/set")
async def post_set(keyval: Keyval):
    return r.sadd(keyval.key, keyval.value)


@router.get("/oset/{key}")
async def oset_get(key: str):
    return r.smembers(key)


@router.post("/oset")
async def post_oset(keyval: ZetKeyval):
    return r.zadd(keyval.key, {keyval.value: keyval.score})
