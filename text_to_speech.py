import pyttsx3

text_speech=pyttsx3.init()
answer=input("Enter your text:")
text_speech.say(answer)
text_speech.runAndWait()
