# Intro
# Coin Flip
# Initialize Players
# # Movement
# #
# Initialize Disc
# Initialize Field
#


import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.animation import FuncAnimation
import random


class VectorCalc:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z  # Added height component (default to 0 for 2D behavior)

    def __add__(self, other):
        return VectorCalc(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return VectorCalc(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):  # scaling
        return VectorCalc(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):  # support scalar * vector
        return self.__mul__(scalar)

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def magnitude_2d(self):
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return VectorCalc(0, 0, 0)
        return VectorCalc(self.x / mag, self.y / mag, self.z / mag)

    def to_tuple(self):
        return self.x, self.y, self.z


class Player:
    def __init__(self, name, team, position, opposing_player=0, offense=True):
        self.name = name
        self.team = team
        self.offense = offense
        self.opposing_player = opposing_player
        self.position = position
        self.velocity = VectorCalc(0, 0)
        self.acceleration = VectorCalc(0, 0)
        self.color = 'blue' if team == 'A' else 'red'

    def apply_force_toward(self, target_pos, max_acc=1):
        """Generate acceleration toward a target position."""
        direction = target_pos - self.position
        self.acceleration = direction.normalize() * max_acc

    def move(self, dt=1, damping=0.9):
        """Physics-style movement update"""
        self.velocity = (self.velocity + self.acceleration) * damping
        self.position = self.position + self.velocity * dt


class Disc:
    def __init__(self, position, possession="home"):
        self.position = position
        self.possession = possession
        self.velocity = VectorCalc(0, 0)
        self.acceleration = VectorCalc(0, 0)
        self.disc_circle = 0

    def throw(self):
        print("Not Ready")


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.players = []
        self.disc = Disc((0, 0))
        self.disc_circles = []
        self.disc_labels = []

    def add_player(self, player):
        self.players.append(player)

    def setup_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 4))
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal')
        self.ax.set_title("Ultimate Frisbee Simulation")
        self.ax.grid(True)

        # Draw field + endzones
        self.ax.add_patch(Rectangle((0, 0), self.width, self.height, edgecolor='green', facecolor='lightgreen'))
        ez = 75
        self.ax.add_patch(Rectangle((0, 0), ez, self.height, color='darkgreen', alpha=0.3))
        self.ax.add_patch(Rectangle((self.width - ez, 0), ez, self.height, color='darkgreen', alpha=0.3))

        # Create player circles
        self.player_circles = []
        self.player_labels = []
        for player in self.players:
            circle = Circle(player.position.to_tuple(), radius=1, color=player.color)
            self.ax.add_patch(circle)
            label = self.ax.text(player.position.x, player.position.y + 1.5, player.name, ha='center', fontsize=8)
            self.player_circles.append(circle)
            self.player_labels.append(label)

    def update(self, frame):
        for i, player in enumerate(self.players):
            # Example: move toward a target point (randomly chosen for now)
            if player.offense:
                if frame % 50 == 0:  # change target every so often
                    player.target = VectorCalc(random.uniform(0, self.width), random.uniform(0, self.height))
            else:
                if frame % 3 == 0:  # change target every so often
                    player.target = player.opposing_player.position

            player.apply_force_toward(player.target, max_acc=1)
            player.move()

            # Keep in bounds
            player.position.x = max(0, min(self.width, player.position.x))
            player.position.y = max(0, min(self.height, player.position.y))

            # Update visuals
            self.player_circles[i].center = player.position.to_tuple()
            self.player_labels[i].set_position((player.position.x, player.position.y + 1.5))


field = Field(360, 120)

# Add some players
charlie = Player("Charlie", "B", VectorCalc(285, 50))
dana = Player("Dana", "B", VectorCalc(285, 90))
alice = Player("Alice", "A", VectorCalc(75, 80), charlie)
bob = Player("Bob", "A", VectorCalc(75, 60), dana)
charlie = Player("Charlie", "B", VectorCalc(285, 50), alice, False)
dana = Player("Dana", "B", VectorCalc(285, 90), bob, False)
field.add_player(alice)
field.add_player(bob)
field.add_player(charlie)
field.add_player(dana)

field.setup_plot()

ani = FuncAnimation(field.fig, field.update, frames=60, interval=200)  # 200ms per frame
plt.show()
