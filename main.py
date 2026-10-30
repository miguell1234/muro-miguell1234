from fastapi import FastAPI

app = FastAPI(title="Muro")

# 1. GET /salud → {"ok": True, "app": "Muro"}


# ---------- PRUEBA (en el Aula; en tu ordenador: python main.py) ----------
if __name__ == "__main__":
    from aula import Cliente
    c = Cliente(app)
    print(c.get("/salud").json())

@app.get("/salud")
def salud():
    return {"ok": True, "app": "Muro"}

@app.get("/hola/{nombre}")
def hola(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}!"}
