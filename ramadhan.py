#!/usr/env python3

import time, os

#sahur = "02:30:00"
sahur = input("[?] Sahur Jam: ")
while True:
	waktu = time.ctime(time.time()).split(" ")
	print ("\r[#] Skrng Jam: "+waktu[3], end="", flush=True) #Supaya Tidak Kebawah
	if waktu[3] == sahur:
		print ("\n[*] Saat Nya Sahur")
		print ("[*] Memutar Alarm")
		os.system("mpv /sdcard/Music/sahur.mp3 > .x && rm -rf .x") # Memutar Ringtone
		break
	else:
		continue
