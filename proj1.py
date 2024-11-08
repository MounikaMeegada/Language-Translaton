from googletrans import Translator, LANGUAGES

def translate_text():
    translator = Translator()
    

    print("Available languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")
    
    
    text = input("\nEnter the text to translate: ")
    src_lang = input("Enter the source language code (e.g., 'en' for English): ").lower()
    dest_lang = input("Enter the target language code (e.g., 'es' for Spanish): ").lower()
    
    try:
        
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        print(f"\nTranslated Text ({LANGUAGES[dest_lang]}): {translation.text}")
    except Exception as e:
        print(f"An error occurred: {e}")


translate_text()
