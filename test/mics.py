import pyaudio

audio=pyaudio.PyAudio()

for i in range(audio.get_device_count()):
	info = audio.get_device_info_by_index(i)
	print info['name']
	print info
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"