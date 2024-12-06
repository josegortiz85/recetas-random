import random

# Definimos una lista de ingredientes comunes
ingredientes = [
    "pollo", "carne de res", "pescado", "tofu", "pasta", "arroz", 
    "tomate", "cebolla", "zanahoria", "pimiento", "ajo", "champiñones",
    "leche", "queso", "mantequilla", "huevo", "aceite de oliva", 
    "espinaca", "pepino", "maíz", "chocolate", "miel", "limón", "sal"
]

# Lista de tipos de recetas
tipos_de_recetas = ["Plato Principal", "Ensalada", "Postre", "Entrada"]

def generar_receta_random():
    # Elegir tres ingredientes al azar
    ingredientes_random = random.sample(ingredientes, 3)
    
    # Elegir un tipo de receta al azar
    tipo_de_receta = random.choice(tipos_de_recetas)

    # Crear la receta con una descripción básica
    receta = f"Tipo de receta: {tipo_de_receta}\n"
    receta += f"Ingredientes: {', '.join(ingredientes_random)}\n"

    # Sugerir preparación básica para hacerlo más divertido
    receta += "Instrucciones: \n"
    receta += "- Mezcla los ingredientes seleccionados.\n"
    receta += "- Cocina según el tipo de receta (por ejemplo, saltear, hervir, hornear).\n"
    receta += "- ¡Disfruta tu {tipo_de_receta.lower()} creativo!"

    return receta

# Generar y mostrar una receta aleatoria
print(generar_receta_random())
