import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(page_title="Language Translator", page_icon="🌐")

st.title("🌐 Language Translation Tool")
st.write("Enter text, choose your languages, and get an instant translation.")

# Supported languages from deep-translator
languages = GoogleTranslator().get_supported_languages(as_dict=True)  # {'english': 'en', ...}
language_names = list(languages.keys())

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", ["auto"] + language_names, index=0)
with col2:
    target_lang = st.selectbox("Target Language", language_names, index=language_names.index("english"))

input_text = st.text_area("Enter text to translate:", height=150)

if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        try:
            src = "auto" if source_lang == "auto" else languages[source_lang]
            tgt = languages[target_lang]

            translated = GoogleTranslator(source=src, target=tgt).translate(input_text)

            st.success("Translation:")
            st.write(translated)

            tts = gTTS(text=translated, lang=tgt)
            tts.save("output.mp3")
            st.audio("output.mp3")

        except Exception as e:
            st.error(f"Something went wrong: {e}")