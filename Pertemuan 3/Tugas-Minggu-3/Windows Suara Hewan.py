import pygame

pygame.init()

# definisikan suara hewan
suara_kucing = pygame.mixer.Sound("Cat.mp3")
suara_anjing = pygame.mixer.Sound("Dog.mp3")
suara_sapi = pygame.mixer.Sound("Cow.mp3")
suara_kuda = pygame.mixer.Sound("Horse.mp3")
suara_domba = pygame.mixer.Sound("Sheep.mp3")
suara_babi = pygame.mixer.Sound("Pig.mp3")
suara_ayam = pygame.mixer.Sound("Rooster.mp3")
suara_bebek = pygame.mixer.Sound("Duck.mp3")
suara_gajah = pygame.mixer.Sound("Elephant.mp3")
suara_singa = pygame.mixer.Sound("Lion.mp3")

# buat daftar hewan dan suara mereka
daftar_hewan = ['Kucing', 'Anjing', 'Sapi', 'Kuda',
                'domba', 'Babi', 'Ayam', 'Bebek', 'Gajah', 'Singa']
daftar_suara = [suara_kucing, suara_anjing, suara_sapi, suara_kuda,
                suara_domba, suara_babi, suara_ayam, suara_bebek, suara_gajah, suara_singa]

# buat tampilan window
lebar = 600
tinggi = 400
layar = pygame.display.set_mode((lebar, tinggi))

# buat font untuk tulisan
font = pygame.font.Font(None, 36)

# tampilkan daftar hewan
for i in range(len(daftar_hewan)):
    teks = font.render(daftar_hewan[i], 1, (255, 255, 255))
    layar.blit(teks, (100, 50+i*30))

pygame.display.flip()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(len(daftar_hewan)):
                if y >= 50+i*30 and y <= 80+i*30:
                    daftar_suara[i].play()
