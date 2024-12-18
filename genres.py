import random

   
chosen_name = ''
chosen_composer = ''
chosen_genre = ''
chosen_path = ''
chosen_piece = ''
chosen_time = ''

fourComp = ''

timeSig = []



genre_ID = {
    'Baroque':0,
    'Classical':1,
    'Romantic':2,
    'Twentieth Century':3
}

piece_types = [
    ['Oratorio', 'Aria', 'Fugue','Recicitative'],
    ['Sonata', 'Minuet and Trio'],
    ['Waltz','March', 'Programme Music'],
    ['Jazz', 'Minimalism','Neo Classisism', 'Neo Romantisism','Musical']
]

music_features = [
    ["Basso Continuo", "Ornamentation", "Terraced Dynamics", "Ground Bass", "Trumpet using notes only in harmonic series"],
    ["Clear homophonic texture", "Simple and functional Melody", "Regular Rhythms"],
    ["Virtuosic Technique", "Extended range of Brass", "Rubato", "Use of chromatisism", "High Dynamic range", "Expressive/Lyrical Melody"],
    ["Dissonant Harmony", "Extended Playing Technique", "Playing at extremes of registers", "Large and varied Percussion Sections", "Irregular Rhythms", "Angular or Fragmented Melodies"]
]

genre_composers = [
    ["J.S. Bach", "George Frideric Handel", "Antonio Vivaldi", "Henry Purcell", "Johann Pachelbel", "Dietrich Buxtehude"],
    ["Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Joseph Haydn", "Franz Schubert", "Domenico Clementi", "Frédéric Chopin", "Felix Mendelssohn"],
    ["Pyotr Ilyich Tchaikovsky", "Gustav Mahler", "Hector Berlioz", "Richard Wagner", "Giuseppe Verdi", "Johannes Brahms", "Johann Strauss", "Gioachino Rossini", "Robert Schumann", "Franz Liszt"],
    ["Igor Stravinsky", "Sergie Prokofiev", "Dmitri Shostakovich", "Claude Debussy", "Maurice Ravel", "Philip Glass", "Béla Bartók", "Oliver Messiaen", "Francis Poulenc", "Steve Reich", "John Cage", "Arnold Schoenberg", "Benjamin Britten", "John Rutter", "Edward Elgar", "Terry Riley", "George Gershwin", "Glen Miller", "Duke Ellington"]
]

pieces = [
    ['Concerto Grosso in G Major','Geroge Friederic Handel','Baroque','4/4','music\HWV-314.mp3'],
    ['Serenade Number 9, in D Major VI - 2nd Menuetto','Wolfgang Amadeus Mozart','Classical','3/4','music\SerenadeN9-Dmj.mp3']
]




def ranComposers():
    global fourComp
    tempID = genre_ID[chosen_genre]
    fourComp = []
    for i in range(4):
        fourComp.append(random.choice(genre_composers[i]))
    fourComp[tempID] = chosen_composer
    return fourComp

def chosePiece():
    global chosen_name
    global chosen_piece
    global chosen_genre
    global chosen_composer
    global chosen_time
    global chosen_path

    chosen_piece = random.choice(pieces)
    chosen_name = chosen_piece[0]
    chosen_composer = chosen_piece[1]
    chosen_genre = chosen_piece[2]
    chosen_time = chosen_piece[3]
    chosen_path = chosen_piece[4]

