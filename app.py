import pyttsx3

engine = pyttsx3.init()

while True:

    x = input('Enter what you want me to speak (or type "exit" to quit): ')

    if x.lower() == 'exit':
        print("Goodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()
        break  
    
    engine.say(x)
    engine.runAndWait()
