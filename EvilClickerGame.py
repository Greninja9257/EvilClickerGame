import random
import sys
import time
import tkinter as tk
from tkinter import Canvas

class HostileClickerGame:
    def __init__(self, root):
        self.score = 0
        self.game_active = True
        self.root = root
        self.root.title("Hostile Clicker Game")
        self.root.geometry("800x600")  # Enhanced window size for improved gameplay experience
        self.label = tk.Label(root, text="Welcome to the ultimate hostile clicker game!", font=('Helvetica', 18))
        self.label.pack(pady=20)
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=('Helvetica', 18))
        self.score_label.pack(pady=10)
        self.root.bind("<Button-1>", self.player_action)  # Bind left mouse click to player_action
        self.schedule_random_events()
        self.canvas = Canvas(root, width=800, height=600)
        self.canvas.pack()

    def start_game(self):
        self.root.after(100, self.update_game)  # More responsive game loop
        self.root.mainloop()

    def update_game(self):
        if self.game_active:
            self.trigger_random_event()
            self.root.after(100, self.update_game)  # Maintain game updates

    def player_action(self, event):
        if random.randint(1, 300) == 1:  # Extremely rare ghost click event
            self.animate_ghost_clicks()
        elif random.randint(1, 10) > 2:  # 80% chance of disapproval
            self.penalize_player()
        else:
            self.increment_score()

        self.check_game_status()

    def increment_score(self):
        increment = random.randint(1, 5)  # Increased score increment range
        self.score += increment
        self.score_label.config(text=f"Score: {self.score}")
        self.label.config(text=f"Score increased by {increment}!")
        self.animate_score_gain()

    def penalize_player(self):
        penalty_messages = [
            "Game is furious! You lost 1/2 of your score.",  # Increased penalty
            "Game is enraged! Half of your score vanished!",
            "Game is seething! Score slashed by half!",
            "Game is livid! It slashes your score mercilessly!"
        ]
        no_penalty_messages = [
            "Game is fuming! But you keep your score this time.",
            "Game is irate! Luckily, no score lost.",
            "Game is boiling! Yet, your score remains.",
            "Game is wrathful! But it spares your score this time."
        ]
        if random.randint(1, 2) == 1 and self.score > 1:  # 1/2 chance to lose 1/2 of score, only if score is greater than 1
            penalty = self.score // 2
            self.score -= penalty
            self.animate_demon()
            self.label.config(text=random.choice(penalty_messages))
        else:
            self.animate_no_penalty()
            self.label.config(text=random.choice(no_penalty_messages))
        self.score_label.config(text=f"Score: {self.score}")

        # Added more animals
        animals = ["lion", "tiger", "bear", "wolf", "elephant", "rhino", "hippo", "gorilla"]
        animal_action = random.choice(animals)
        if self.score > 3 and random.randint(1, 30) == 1:  # Only % chance of animal attack if score is greater than 3
            animal_penalty = self.score // 3  # Increased animal penalty
            self.score -= animal_penalty
            self.animate_animal(animal_action)
            self.label.config(text=f"{animal_action.capitalize()} attack! You lost 1/3 of your score.")
        else:
            self.label.config(text=f"{animal_action.capitalize()} attack! But your score is too low to be affected.")
        self.score_label.config(text=f"Score: {self.score}")

    def animate_demon(self):
        self.canvas.delete("all")
        demon = self.canvas.create_rectangle(350, 250, 450, 350, fill="red")
        self.canvas.create_text(400, 300, text="Demon Slashes!", fill="white")
        self.canvas.update()
        time.sleep(0.5)
        self.canvas.delete(demon)

    def animate_no_penalty(self):
        self.canvas.delete("all")
        sad_face = self.canvas.create_text(400, 300, text=":(", font=('Helvetica', 48), fill="grey")
        self.canvas.update()
        time.sleep(0.5)
        self.canvas.delete(sad_face)

    def animate_animal(self, animal):
        self.canvas.delete("all")
        animal_image = self.canvas.create_text(400, 300, text=f"{animal.capitalize()} Attacks!", font=('Helvetica', 48), fill="red")
        self.canvas.update()
        time.sleep(0.5)
        self.canvas.delete(animal_image)

    def animate_score_gain(self):
        self.canvas.delete("all")
        star = self.canvas.create_oval(350, 250, 450, 350, fill="yellow")
        self.canvas.create_text(400, 300, text="Score Up!", fill="black")
        self.canvas.update()
        time.sleep(0.5)
        self.canvas.delete(star)

    def animate_ghost_clicks(self):
        self.canvas.delete("all")
        ghost = self.canvas.create_text(400, 300, text="Ghost Clicks!", font=('Helvetica', 48), fill="white")
        self.canvas.update()
        time.sleep(0.5)
        self.canvas.delete(ghost)
        self.label.config(text="All your clicks have flown away as ghost clicks!")

    def check_game_status(self):
        game_over_messages = [
            "Game Over! The game has defeated you.",
            "Game Over! You were overwhelmed by the game.",
            "Game Over! You've been crushed by the game.",
            "Game Over! The game's hostility was too much."
        ]
        win_messages = [
            "You've somehow managed to win. Congratulations!",
            "Miraculously, you've won! Celebrate!",
            "You've triumphed! Against all odds, you won!",
            "You've beaten the game! It's a miracle!"
        ]
        if self.score < 0:
            self.label.config(text=random.choice(game_over_messages))
            self.game_active = False
        elif self.score > 100:  # Increased win score threshold
            self.label.config(text=random.choice(win_messages))
            self.game_active = False

    def trigger_random_event(self):
        random_event_messages = [
            "Oh no! Random event decreased your score by 10.",  # Increased score penalty
            "Disaster! A random event just docked 10 points from your score.",
            "Calamity! Your score drops by 10 due to a random event.",
            "Catastrophe! A random twist reduces your score by 10.",
            "Lucky! Random event had no negative effect.",
            "Fortunate! The random event spared your score.",
            "Serendipity! The random event leaves your score untouched.",
            "A stroke of luck! No harm from the random event."
        ]
        if random.randint(1, 10) == 1:  # 10% chance for a random event
            self.label.config(text="Random event! Something unexpected happens.")
            if random.choice([True, False]) and self.score > 10:  # Only lose score if score is greater than 10
                self.score -= 10
                self.label.config(text=random.choice(random_event_messages[:4]))
            else:
                self.label.config(text=random.choice(random_event_messages[4:]))
            self.score_label.config(text=f"Score: {self.score}")

    def schedule_random_events(self):
        self.root.after(3000, self.trigger_random_event)  # Increased frequency of random events

if __name__ == "__main__":
    root = tk.Tk()
    game = HostileClickerGame(root)
    try:
        game.start_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        sys.exit(0)
