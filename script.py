import os
import random
from pydub import AudioSegment
from pydub.utils import which
import genres as db

db.chosePiece() #chose piece

AudioSegment.converter = r"C:\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"  
AudioSegment.ffprobe = r"C:\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffprobe.exe"

file_path = rf"{db.chosen_path}"

audio = AudioSegment.from_file(file_path)

# Select a 15-second random segment
start_time = random.randint(0, len(audio) - 20000) 
end_time = start_time + 20000
segment = audio[start_time:end_time]

faded_segment = segment.fade_in(2000).fade_out(2000)

output_path = r"C:\Users\alexa\Documents\projects\Music Listening\output_piece.mp3"
faded_segment.export(output_path, format="mp3")

#blank divider

id = db.genre_ID[db.chosen_genre] #assign id to genre (baroque being 0 etc)

composers = db.ranComposers() #choses 4 composers
print(composers[id])

print(composers) # prints correct answer - REMOVE WHEN DONE

#divider

print('Enter the time signature of this piece. Please structure it as x/y: ')
userTS = input()
if userTS == db.chosen_time:
    print('Correct')
else:
    print(f'Incorrect. The answer is: {db.chosen_time}')

#divider
ranList = [0,1,2,3]
ranList = random.shuffle(ranList)
print('Which of the following is a style of the genre of this piece? Enter the number. ')
for i in range(4):
    print(f'{i+1}: {random.choice(db.music_features[ranList[i]])}')
user_choice = int(input())
if user_choice == (id+1):
    print('Correct')
else:
    print(f'Incorrect, the answer was x')

    





