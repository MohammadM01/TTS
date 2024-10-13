import streamlit as st
import pyttsx3
import speech_recognition as sr

# Initialize session state for recording if not already set
if 'recording' not in st.session_state:
    st.session_state['recording'] = False

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

# Function to handle recording and convert speech to text
def record_audio():
    recognizer = sr.Recognizer()

    try:
        # Use the first available microphone
        with sr.Microphone() as source:
            st.write("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            st.write("Listening... Speak something (stop speaking to finish):")
            # This listens for a continuous period
            audio = recognizer.listen(source, timeout=10)  # You can adjust timeout as necessary

            st.write("Processing the speech...")
            # Using Google Web Speech API to recognize the speech
            text = recognizer.recognize_google(audio)
            return text

    except sr.UnknownValueError:
        st.error("Sorry, I did not understand the audio.")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    return None

# Streamlit webpage layout
st.title("Text to Speech and Speech to Text Converter")

# Option to choose between Text-to-Speech and Speech-to-Text
st.subheader("Choose an option:")
option = st.selectbox("Select what you want to do", ["Text to Speech", "Speech to Text"])

if option == "Text to Speech":
    input_text = st.text_area("Enter your text/code to convert into speech:")
    if st.button("Convert to Speech", key="text_to_speech_button"):
        if input_text:
            st.success("Speaking out the text/code...")
            text_to_speech(input_text)
        else:
            st.error("Please enter some text or code!")

elif option == "Speech to Text":
    st.write("Please allow microphone access for speech recognition to work.")
    if st.button("Click to Record", key="record_again_button"):
        st.write("Recording and converting speech to text...")
        speech_text = record_audio()
        if speech_text:
            st.write(f"Recognized text: {speech_text}")
