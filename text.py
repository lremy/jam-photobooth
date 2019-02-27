# English
text_en = {
    'photo number': "Photo {} of {}",
    'press to capture': "Press the button to capture...",
    'ready': "Ready!\n" "Press the button to start...",
}

# German - Deutsche
text_de = {
    'photo number': "Foto {} von {}",
    'press to capture': "Drucke den Knopf fur ein Foto...",
    'ready': "Bereit!\n" "Drucke den Knopf um zu starten...",
}

# French - Français
text_fr = {
    'photo number': "Photo {} de {}",
    'press to capture': "Appuyez sur le bouton pour capturer...",
    'ready': "Pret!\n" "Appuyez sur le bouton pour commencer...",
}

# Spanish - Español
text_es = {
    'photo number': "Foto {} de {}",
    'press to capture': "Presione el boton para sacar fotos...",
    'ready': "Listo!\n" "Presione el boton para comenzar...",
}

# Welsh - Cymraeg
text_cy = {
    'photo number': "Llun {} o {}",
    'press to capture': "Gwasgwch y botwm i'w dal...",
    'ready': "Barod!\n" "Gwasgwch y botwm i ddechrau...",
}

language_dicts = {
    'en': text_en,
    'de': text_de,
    'fr': text_fr,
    'es': text_es,
    'cy': text_cy,
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
