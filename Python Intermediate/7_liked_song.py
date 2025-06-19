
liked_song={
'Bad Habits':'Ed Sheeran',
'Im Just Ken':'Ryan Gosling',
'Mastermind':' Taylor Swift',
'Uptown Funk':'  Mark Ronson ft. Bruno Mars',
'Ghost ':'Justin Bieber'}

def write_liked_songs_to_file(liked_song,file):
    with open(file,'w') as files:
        for s,a in liked_song.items():
            files.write(f'{s} by {a}\n')
            
    files.close()

write_liked_songs_to_file(liked_song,'test.txt')
