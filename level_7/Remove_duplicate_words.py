# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

def remove_duplicate_words(s):
    new = []
    for w in s.split():
        if w not in new:
            new.append(w)
    return " ". join(new)