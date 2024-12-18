import pyttsx3
if __name__ == '__main__':
    engine = pyttsx3.init()
    print("welcome to RoboSpeaker 1.1 Created by Trishla")
    while True:
        x = input("enter what youme to speak")
        if x.lower() == "q":
            break
        
        engine.say(x)
        engine.runAndWait()
 