from typing import Optional
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/listar")
def listar():
    f = open("demofile.txt", "r")
    return f.read()

@app.post("/alta/{nombre}/{telefono}")
def dar_alta(nombre: str, telefono: str):
    f = open("demofile.txt", "w")
    # {
    # "nombre": "pepe",
    # "telefono": "5551234"
    # }
    f.write("{\"nombre\":\"" + nombre + "\",\"telefono\":\"" + telefono + "\"}")
    f.close()
    return {"alta":"ok"}

@app.delete("/borrar/{nombre}")
def eliminar_contacto(nombre: str):
    f = open("demofile.txt", "w")
    f.write("")
    f.close()
    return {"borrado":"ok"}


