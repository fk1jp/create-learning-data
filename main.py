#!/bin/env python
#-*- cording: utf-8 -*-

from pydub import AudioSegment
import math

WINDOW = 5
MOVE = 2

mp3_version = AudioSegment.from_mp3("jazz_funk_01.mp3")
print(len(mp3_version))
length = math.floor( len(mp3_version) / 1000 ) - WINDOW
print(length)

for i in range(0,length,MOVE):
  start = i * 1000
  finish = (i + WINDOW) * 1000
  print(start , finish)
  filename = "sound" + str(i) + ".mp3"
  print(filename)
  data=mp3_version[start : finish]
  file_handler=data.export(filename , format="mp3")
