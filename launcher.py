import os
import pygame
import subprocess

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ROM_DIRS = {
    "NES": "roms/nes",
    "SNES": "roms/snes",
    "GameBoy": "roms/gb"
}
EMULATOR_CORES = {
    "NES": "nestopia",
    "SNES": "snes9x",
    "GameBoy": "gambatte"
}

class RetroGameConsole:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("🎛️ Retro Game Console")
        self.font = pygame.font.SysFont("Arial", 28)
        self.clock = pygame.time.Clock()
        self.running = True
        self.rom_list = self.load_roms()
        self.selected_index = 0
        self.systems = list(ROM_DIRS.keys())
        self.current_system_index = 0

    def load_roms(self):
        roms = {}
        for system, path in ROM_DIRS.items():
            try:
                roms[system] = [f for f in os.listdir(path) if f.endswith(('.nes', '.sfc', '.gb'))]
            except FileNotFoundError:
                roms[system] = []
        return roms

    def draw(self):
        self.screen.fill((20, 20, 20))
        current_system = self.systems[self.current_system_index]
        roms = self.rom_list[current_system]
        title = self.font.render(f"{current_system} Games", True, (255, 255, 255))
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 20))
        for i, rom in enumerate(roms):
            color = (255, 255, 255) if i == self.selected_index else (100, 100, 100)
            rom_text = self.font.render(rom, True, color)
            self.screen.blit(rom_text, (50, 80 + i * 40))
        pygame.display.flip()

    def launch_game(self):
        current_system = self.systems[self.current_system_index]
        core = EMULATOR_CORES[current_system]
        rom = self.rom_list[current_system][self.selected_index]
        rom_path = os.path.join(ROM_DIRS[current_system], rom)
        subprocess.call(["retroarch", "-L", f"/usr/lib/libretro/{core}_libretro.so", rom_path])

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                current_roms = self.rom_list[self.systems[self.current_system_index]]
                if event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(current_roms)
                elif event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(current_roms)
                elif event.key == pygame.K_RIGHT:
                    self.current_system_index = (self.current_system_index + 1) % len(self.systems)
                    self.selected_index = 0
                elif event.key == pygame.K_LEFT:
                    self.current_system_index = (self.current_system_index - 1) % len(self.systems)
                    self.selected_index = 0
                elif event.key == pygame.K_RETURN:
                    if current_roms:
                        self.launch_game()

if __name__ == "__main__":
    RetroGameConsole().run()
