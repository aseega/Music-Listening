import os
import random
from pydub import AudioSegment
from pydub.utils import which
import genres as db

db.chosePiece() #chose piece

id = db.genre_ID[db.chosen_genre] #assign id to genre (baroque being 0 etc)

composers = db.ranComposers() #choses 4 composers
print(composers[id])

print(composers)

AudioSegment.converter = r"C:\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"  
AudioSegment.ffprobe = r"C:\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffprobe.exe"

file_path = rf"C:\Users\alexa\Documents\projects\Music Listening\{db.chosen_path}"

audio = AudioSegment.from_file(file_path)

# Select a 15-second random segment
start_time = random.randint(0, len(audio) - 20000) 
end_time = start_time + 20000
segment = audio[start_time:end_time]

faded_segment = segment.fade_in(2000).fade_out(2000)

output_path = r"C:\Users\alexa\Documents\projects\Music Listening\output_piece.mp3"
faded_segment.export(output_path, format="mp3")

