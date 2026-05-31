import pygame
import sys

# ---- CONFIG ----
WIDTH, HEIGHT = 1920, 1080
FPS = 60
PLAYER_SPEED = 5
DISC_SPEED = 700  # pixels per second
# ----------------


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.vel = pygame.math.Vector2(0, 0)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.vel.x = (keys[pygame.K_d] - keys[pygame.K_a]) * PLAYER_SPEED * 1.5
            self.vel.y = (keys[pygame.K_s] - keys[pygame.K_w]) * PLAYER_SPEED * 1.5
        else:
            self.vel.x = (keys[pygame.K_d] - keys[pygame.K_a]) * PLAYER_SPEED
            self.vel.y = (keys[pygame.K_s] - keys[pygame.K_w]) * PLAYER_SPEED
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

        # keep inside window
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))


class Disc(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 10)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(0, 0)

    def launch(self, direction):
        # direction: any Vector2; normalize and scale
        if direction.length() > 0:
            if pygame.K_LSHIFT:
                self.vel = direction.normalize() * DISC_SPEED * 2
            else:
                self.vel = direction.normalize() * DISC_SPEED

    def update(self, dt):
        # move
        self.pos += self.vel * dt
        self.rect.center = self.pos

        # bounce off edges
        if self.rect.left <= 0 or self.rect.right  >= WIDTH:
            self.vel.x *= -0.95
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vel.y *= -0.95


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ultimate Frisbee Demo")
    clock = pygame.time.Clock()

    # Sprites
    player = Player((WIDTH//2, HEIGHT//2))
    disc = Disc(player.rect.center)

    all_sprites = pygame.sprite.Group(player, disc)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # seconds since last frame

        # --- EVENTS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # launch disc from player toward mouse
                    mouse_pos = pygame.mouse.get_pos()
                    direction = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(player.rect.center)
                    disc.pos = pygame.math.Vector2(player.rect.center)
                    disc.launch(direction)

        # --- UPDATE ---
        all_sprites.update(dt)

        # --- DRAW ---
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
