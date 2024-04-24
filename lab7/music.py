import pygame

pygame.init()

def make_pL(playList, musicname):
    playList.append(musicname)

# Initialize Pygame mixer
pygame.mixer.init()

# Load music files
music_files = [
    "C:\\Users\\Lenovo\\Downloads\\Mysterions_-_Mysterions_-_Asyl_anim_2013_75079894.mp3",
    "C:\\Users\\Lenovo\\Downloads\\Imagine_Dragons_-_Thunder_62574883.mp3",
    "C:\\Users\\Lenovo\\Downloads\\SHIZA_-_Shym_II_75935681.mp3"
]

# Create playlist
playlist = []
for file in music_files:
    make_pL(playlist, file)

# Start playing the first song in the playlist
pygame.mixer.music.load(playlist[2])
pygame.mixer.music.play()

# Set up the display
screen = pygame.display.set_mode((200, 100))
clock = pygame.time.Clock()

# Variables
pause = False
volume = 1.0
current_track_index = 0

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_1:
                volume -= 0.1
                if volume < 0.0:
                    volume = 0.0
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_2:
                volume += 0.1
                if volume > 1.0:
                    volume = 1.0
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_z:
                current_track_index -= 1
                if current_track_index < 0:
                    current_track_index = len(playlist) - 1
                pygame.mixer.music.load(playlist[current_track_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_x:
                current_track_index += 1
                if current_track_index >= len(playlist):
                    current_track_index = 0
                pygame.mixer.music.load(playlist[current_track_index])
                pygame.mixer.music.play()

    pygame.display.update()
    clock.tick(60)
