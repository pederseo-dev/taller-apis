from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

pedidos = {}

menu = {
    "comidas": ["pizza", "hamburguesa", "ensalada"],
    "bebidas": ["agua", "refresco", "jugo"],
    "postres": ["helado", "pastel", "fruta"]
}

# Menú premium para usuarios autenticados
menu_premium = {
    "comidas": ["pizza", "hamburguesa", "ensalada", "lobster", "filete wagyu", "caviar"],
    "bebidas": ["agua", "refresco", "jugo", "champagne", "vino tinto premium", "whisky 18 años"],
    "postres": ["helado", "pastel", "fruta", "soufflé de chocolate", "tiramisú italiano", "crème brûlée"]
}

class Pedido(BaseModel):
    numero_mesa: int
    comida: str
    bebida: str
    postre: str

class Modificar(BaseModel):
    comida: str
    bebida: str
    postre: str
#----------------------------------------------------------------------------------- Ver menu
@app.get("/ver_menu")
def ver_menu(authorization: str = Header(None)):
    # Verificar si viene el header de autorización
    if authorization and authorization == "cheto":
        return {
            "mensaje": "🎉 ¡Bienvenido al menú premium!",
            "menu": menu_premium
        }
    else:
        return {
            "mensaje": "🍽️ Menú estándar disponible",
            "menu": menu
        }
    
#----------------------------------------------------------------------------------- Hacer pedido
@app.post("/hacer_pedido")
def crear_pedido(pedido: Pedido):
    if pedido.numero_mesa in pedidos:
        raise HTTPException(status_code=400, detail="Ya existe un pedido para esta mesa")
    
    if pedido.comida not in menu["comidas"]:
        raise HTTPException(status_code=400, detail=f"{pedido.comida} no está en el menú de comidas")
    if pedido.bebida not in menu["bebidas"]:
        raise HTTPException(status_code=400, detail=f"{pedido.bebida} no está en el menú de bebidas")
    if pedido.postre not in menu["postres"]:
        raise HTTPException(status_code=400, detail=f"{pedido.postre} no está en el menú de postres")

    pedidos[pedido.numero_mesa] = {
        "comida": pedido.comida,
        "bebida": pedido.bebida,
        "postre": pedido.postre
    }
    return {"mensaje": "Pedido creado correctamente", "pedido": pedidos[pedido.numero_mesa]}

#----------------------------------------------------------------------------------- Modifcar pedido
@app.put("/modificar_pedido/{numero_mesa}")
def modificar_pedido(numero_mesa: int, nuevo: Modificar):
    if numero_mesa not in pedidos:
        raise HTTPException(status_code=404, detail="El pedido que quieres modificar no existe")
    
    if nuevo.comida not in menu["comidas"]:
        raise HTTPException(status_code=400, detail=f"{nuevo.comida} no está en el menú de comidas")
    if nuevo.bebida not in menu["bebidas"]:
        raise HTTPException(status_code=400, detail=f"{nuevo.bebida} no está en el menú de bebidas")
    if nuevo.postre not in menu["postres"]:
        raise HTTPException(status_code=400, detail=f"{nuevo.postre} no está en el menú de postres")

    pedidos[numero_mesa] = {
        "comida": nuevo.comida,
        "bebida": nuevo.bebida,
        "postre": nuevo.postre
    }
    return {"mensaje": "Pedido modificado correctamente", "nuevo_pedido": pedidos[numero_mesa]}

#----------------------------------------------------------------------------------- Eliminar pedido
@app.delete("/eliminar_pedido/{numero_mesa}")
def eliminar_pedido(numero_mesa: int):
    if numero_mesa not in pedidos:
        raise HTTPException(status_code=404, detail="El pedido que quieres eliminar no existe")
    
    del pedidos[numero_mesa]
    return {"mensaje": f"Pedido de la mesa {numero_mesa} eliminado correctamente"}

#----------------------------------------------------------------------------------- Menú Premium (con autenticación básica)
@app.get("/menu_premium")
def menu_premium_route(authorization: str = Header(None)):
    """
    Ruta para demostrar autenticación básica.
    Envía el header 'authorization' con valor 'cheto' para acceder.
    """
    if not authorization:
        raise HTTPException(
            status_code=401, 
            detail="🔒 Acceso denegado. Necesitas enviar el header 'authorization' con valor 'cheto'"
        )
    
    if authorization != "cheto":
        raise HTTPException(
            status_code=403, 
            detail="❌ Credenciales incorrectas. Usa 'cheto' como valor del header authorization"
        )
    
    return {
        "mensaje": "🎉 ¡Acceso premium concedido!",
        "menu_premium": menu_premium,
        "instrucciones": "Para probar esta ruta, envía el header: authorization: cheto"
    }
