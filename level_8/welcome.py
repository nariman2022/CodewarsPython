# The Task
# Think of a way to store the languages as a database. Write a 'welcome' function that takes a parameter 'language',
# with a type String, and returns a greeting - if you have it in your database. It should default to English
# if the language is not in the database, or in the event of an invalid input.

def greet(language):
    greet = {
            "english": "Welcome",
            "czech": "Vitejte",
             "danish": "Velkomst",
             "dutch": "Welkom",
             "estonian": "Tere tulemast",
             "finnish": "Tervetuloa",
             "flemish": "Welgekomen",
             "french": "Bienvenue",
             "german": "Willkommen",
             "irish": "Failte",
             "italian": "Benvenuto",
             "latvian": "Gaidits",
             "lithuanian": "Laukiamas",
             "polish": "Witamy",
             "spanish": "Bienvenido",
             "swedish": "Valkommen",
             "welsh": "Croeso"
    }
    return greet.get(language) if language in greet else greet.get("english")