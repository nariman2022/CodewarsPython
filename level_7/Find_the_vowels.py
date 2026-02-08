# We want to know the index of the vowels in a given word, for example, there are two vowels in the word super
# (the second and fourth letters).

def vowel_indices(word):
    return [i+1 for i in range(len(word)) if word[i].lower() in "aeiouy"]