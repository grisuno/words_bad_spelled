from fuzzywuzzy import fuzz

# lista de palabras objetivo
target_words = ["facebook", "youtube", "gcp", "google", "azure"]

# palabra a comparar
input_word = "gugle"

# comparar la palabra de entrada con cada palabra objetivo
scores = {word: fuzz.token_set_ratio(input_word, word) for word in target_words}

# imprimir la palabra objetivo con la mayor similitud
best_match = max(scores, key=scores.get)
print("La palabra más similar es: ", best_match)
