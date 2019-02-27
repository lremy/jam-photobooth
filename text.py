# English
text_en = {
    'ready': "Ready for the photo?",
    'processing': "Processing the photo...",
}

# German - Deutsche
text_de = {
    'ready': "Bereit fur das Foto?",
    'processing': "Fotobearbeitung...",
}

# French - Français
text_fr = {
    'ready': "Pret(s) pour la photo?",
    'processing': "Traitement de la photo...",
}

# Spanish - Español
text_es = {
    'ready': "Listo para la foto?",
    'processing': "Procesamiento de fotos...",
}

language_dicts = {
    'en': text_en,
    'de': text_de,
    'fr': text_fr,
    'es': text_es,
}

def get_text(language='en'):
    """
    Retrieve a dictionary of text in the specified language, if available
    """
    return language_dicts[language]

# test for non-ascii characters not supported by the camera firmware
for language in language_dicts.values():
    for key, text in language.items():
        assert all(ord(c) in range(128) for c in text), text
