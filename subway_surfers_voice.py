import speech_recognition as sr
import keyboard

r = sr.Recognizer()

while (True):

	with sr.Microphone() as source:
		try:
			print("waiting")

			r.adjust_for_ambient_noise(source)
			audio = r.listen(source,timeout=2.5)

			print("listened")

			cmd = r.recognize_google(audio)
			print(cmd)
			
			if(cmd=="close"):
				print("closing")
				break

			elif(cmd=="jump"):
				print("jumping")
				keboard.press_and_release("up")

			elif(cmd=="roll"):
				print("rolling")
				keyboard.press_and_release("down")

			elif cmd=="right" or "write":
				print(cmd)
				keyboard.press_and_release("right")

			elif cmd=="left":
				print(cmd)
				keyboard.press_and_release("left")

		except:
			print("speak ")
			