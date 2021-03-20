import pyautogui
import pyttsx3 
import speech_recognition as sr 
import webbrowser as wb
import time
def speak(audio): 
	engine = pyttsx3.init()
	engine.setProperty('rate', 120)
	voices = engine.getProperty('voices')  
	engine.setProperty('voice', voices[1].id)           
	engine.say(audio) 
	engine.runAndWait()
def takeCommand(): 
	r = sr.Recognizer() 
	with sr.Microphone() as source: 
		print('Listening') 
		r.pause_threshold = 0.8
		audio = r.listen(source) 
		try: 
			print("Recognizing") 
			Query = r.recognize_google(audio, language='en-in') 
			print("the command is printed: ", Query) 			
		except Exception as e: 
			print(e) 
			print("Say that again sir") 
			return takeCommand()
		return Query
#--------------------------------------------------------------------------------------
com_in = False
speak(str("What do you want to spam?: "))
Y = takeCommand()
speak(str("How many times?: "))
while com_in == False:
	try:
		X = int(takeCommand())
		com_in = True
	except Exception as e:
		print(e)
BrowserD = wb.get('windows-default')
BrowserD.open_new("https://web.whatsapp.com/")
time.sleep(20)
for j in range(X):
    pyautogui.typewrite(Y)
    pyautogui.press("enter")
