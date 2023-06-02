import streamlit as st
import speech_recognition as sr

def transcribe_speech():
    # Create a recognizer instance
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        st.write("Speak something...")
        audio = r.listen(source)

    try:
        st.write("Transcribing...")
        # Use the recognizer to convert speech to text
        text = r.recognize_google(audio)
        st.write("Text:", text)
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        st.write("Speech recognition service error: {0}".format(e))

def main():
    st.title("Real-time Speech to Text")
    st.write("Click on the button and speak to transcribe your speech.")

    if st.button("Start Transcription"):
        transcribe_speech()

if __name__ == "__main__":
    main()
