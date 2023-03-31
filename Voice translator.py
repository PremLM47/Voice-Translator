import googletrans
import speech_recognition
import gtts
import playsound

print("The code of different languages are : ")
print(googletrans.LANGUAGES)

a,b=input("Enter code of source and destination language :").split()

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice,language=a)
    print(text)


translator=googletrans.Translator()
translation=translator.translate(text,dest=b)
print(translation.text)

converted_audio = gtts.gTTS(translation.text, lang=b)
converted_audio.save("audio_file.mp3")
playsound.playsound("audio_file.mp3") 