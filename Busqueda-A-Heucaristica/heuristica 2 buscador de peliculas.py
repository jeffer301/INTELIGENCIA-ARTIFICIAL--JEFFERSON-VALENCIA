import math

# Base de datos: Película -> [Lista de géneros/etiquetas]
MOVIES = {
    "Toy Story": ["Animación", "Infantil", "Aventura"],
    "Shrek": ["Animación", "Infantil", "Comedia"],
    "Matrix": ["Acción", "Sci-Fi", "Misterio"],
    "Inception": ["Acción", "Sci-Fi", "Thriller"],
    "El padrino": ["Drama", "Crimen"],
    "Pulp Fiction": ["Drama", "Crimen", "Comedia"],
    "Buscando a Nemo": ["Animación", "Infantil", "Aventura"],
    "Blade Runner 2049": ["Sci-Fi", "Acción", "Drama"]
}

def get_cosine_similarity(vec1, vec2):
    """
    Heurística matemática: Calcula el coseno del ángulo entre dos vectores.
    Cuanto más cercano a 1, más similares son los contenidos.
    """
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a**2 for a in vec1))
    mag2 = math.sqrt(sum(b**2 for b in vec2))
    
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot_product / (mag1 * mag2)

def run_recommender():
    # 1. Crear una lista numerada de películas
    movie_list = list(MOVIES.keys())
    all_genres = sorted(list(set(g for genres in MOVIES.values() for g in genres)))

    print("--- SISTEMA DE RECOMENDACIÓN HEURÍSTICO ---")
    print("Selecciona una película que hayas visto:")
    for i, title in enumerate(movie_list, 1):
        print(f"{i}. {title}")

    # 2. Captura de datos con validación
    try:
        choice = int(input("\nIngresa el número de la película: "))
        if not (1 <= choice <= len(movie_list)):
            print("Número fuera de rango.")
            return
    except ValueError:
        print("Entrada no válida. Por favor, usa números.")
        return

    selected_movie = movie_list[choice - 1]
    
    # 3. Vectorizar la película seleccionada
    target_genres = MOVIES[selected_movie]
    target_vector = [1 if g in target_genres else 0 for g in all_genres]

    # 4. Calcular similitud con el resto usando la heurística
    scores = []
    for title, genres in MOVIES.items():
        if title == selected_movie:
            continue
        
        current_vector = [1 if g in genres else 0 for g in all_genres]
        similarity = get_cosine_similarity(target_vector, current_vector)
        scores.append((title, similarity))

    # 5. Mostrar resultados ordenados
    scores.sort(key=lambda x: x[1], reverse=True)

    print(f"\nComo viste '{selected_movie}', estas son tus recomendaciones:")
    print("-" * 45)
    for title, score in scores:
        # Solo mostrar si tienen algo en común (score > 0)
        if score > 0:
            porcentaje = score * 100
            print(f"[{porcentaje:.1f}% de similitud] -> {title}")
    
    if not any(s[1] > 0 for s in scores):
        print("No encontramos películas similares en nuestra base de datos.")

if __name__ == "__main__":
    run_recommender()