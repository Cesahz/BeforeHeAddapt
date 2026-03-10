from dominio.ataques import Ataque
#lista con tecnicas
ataques_gojo = [

    Ataque(
        nombre="Golpe Basico",
        costo_ce=30,
        dano_base=35,
        tags=["Fisico", "Contundente"]
    ),

    Ataque(
        nombre="Golpe Reforzado",
        costo_ce=60,
        dano_base=70,
        tags=["Fisico", "Impacto_Puro"]
    ),

    Ataque(
        nombre="Golpe Blue",
        costo_ce=90,
        dano_base=85,
        tags=["Fisico", "Compresion","Convergencia"]
    ),

    Ataque(
        nombre="Blue",
        costo_ce=120,
        dano_base=110,
        tags=["Atraccion", "Compresion", "Convergencia","Espacio"]
    ),

    Ataque(
        nombre="Red",
        costo_ce=150,
        dano_base=160,
        tags=["Espacio", "Explosivo","Divergencia","Conjuro Inverso"]
    ),

    Ataque(
        nombre="Hollow Purple",
        costo_ce=300,
        dano_base=400,
        tags=["Desintegracion","Espacio","Vacio"]
    ),



    Ataque(
        nombre="Unlimited Void",
        costo_ce=500,
        dano_base=0,
        tags=["Sobrecarga_Informacion","Dominio","Vacio"]
    )
]