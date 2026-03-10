from dominio.ataques import Ataque

#lista con tecnicas
ataques_gojo = [

    Ataque(
        nombre="Golpe Basico",
        costo_ce=0, 
        dano_base=40,
        tags=["Fisico"] 
    ),

    Ataque(
        nombre="Golpe Reforzado",
        costo_ce=100,
        dano_base=80,
        tags=["Fisico", "Impacto_Puro"]
    ),

    Ataque(
        nombre="Golpe Blue",
        costo_ce=200,
        dano_base=120,
        tags=["Fisico", "Espacio"]
    ),

    Ataque(
        nombre="Blue",
        costo_ce=400,
        dano_base=180,
        tags=["Espacio", "Atraccion"] 
    ),

    Ataque(
        nombre="Red",
        costo_ce=600,
        dano_base=250,
        tags=["Espacio", "Repulsion"]
    ),

    Ataque(
        nombre="Hollow Purple",
        costo_ce=1100, 
        dano_base=600,
        tags=["Espacio", "Masa_Virtual"]
    ),

    Ataque(
        nombre="Unlimited Void",
        costo_ce=2500,
        dano_base=0,
        tags=["Dominio", "Vacio"]
    )
]