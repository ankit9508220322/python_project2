from gtts import gTTS

text ='''
Python is a programming language that is 
widely used in web applications, software
 development, data science, and machine 
 learning (ML). Developers use Python 
because it is efficient and easy to learn 
and can run on many different platforms.
'''
language = 'hi'

tts_object = gTTS(text=text, lang=language, slow=False, timeout=10)
tts_object.save("python2.mp3")

print("Text:", text)