import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_RADIUS = 10
BRICK_WIDTH = 50
BRICK_HEIGHT = 20
BRICK_ROWS = 4
BRICK_COLS = 12
PADDLE_SPEED = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
PADDLE_COLOR = "blue"
BALL_COLOR = "red"
BRICK_COLOR = "green"

class BreakoutGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.create_game_objects()  

        self.dx = BALL_SPEED_X
        self.dy = BALL_SPEED_Y

        self.canvas.bind_all('<KeyPress-Left>', self.move_paddle_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_paddle_right)
        self.started = False  

        self.update()

    def create_game_objects(self):
        self.paddle = self.canvas.create_rectangle(WIDTH/2 - PADDLE_WIDTH/2, HEIGHT - PADDLE_HEIGHT - 20,
                                                   WIDTH/2 + PADDLE_WIDTH/2, HEIGHT - 20, fill=PADDLE_COLOR)
        self.ball = self.canvas.create_oval(WIDTH/2 - BALL_RADIUS, HEIGHT/2 - BALL_RADIUS,
                                             WIDTH/2 + BALL_RADIUS, HEIGHT/2 + BALL_RADIUS, fill=BALL_COLOR)
        self.bricks = []
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                x1 = j * BRICK_WIDTH
                y1 = i * BRICK_HEIGHT
                x2 = x1 + BRICK_WIDTH
                y2 = y1 + BRICK_HEIGHT
                self.bricks.append(self.canvas.create_rectangle(x1, y1, x2, y2, fill=BRICK_COLOR))

    def move_paddle_left(self, event):
        if not self.started: self.started=True
        if self.canvas.coords(self.paddle)[0]>PADDLE_SPEED:
            self.canvas.move(self.paddle, -PADDLE_SPEED, 0)

    def move_paddle_right(self, event):
        if not self.started: self.started=True
        if self.canvas.coords(self.paddle)[2]<WIDTH-PADDLE_SPEED:

            self.canvas.move(self.paddle, PADDLE_SPEED, 0)

    def update(self):
        if self.started:
            self.canvas.move(self.ball, self.dx, self.dy)
            ball_pos = self.canvas.coords(self.ball)
            paddle_pos = self.canvas.coords(self.paddle)
            if ball_pos[0] <= 0 or ball_pos[2] >= WIDTH:
                self.dx = -self.dx
            if ball_pos[1] <= 0:
                self.dy = -self.dy
            if ball_pos[3] >= HEIGHT:
                self.canvas.create_text(WIDTH/2, HEIGHT/2, text="Game Over", fill="white", font=("Arial", 30))
                self.master.after(600, self.restart_game)
            if ball_pos[3] >= paddle_pos[1]  and ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
                self.dy = -self.dy

            for brick in self.bricks:
                brick_pos = self.canvas.coords(brick)
                if ball_pos[1] <= brick_pos[3] and ball_pos[3] >= brick_pos[1] and ball_pos[2] >= brick_pos[0] and ball_pos[0] <= brick_pos[2]:
                    self.canvas.delete(brick)
                    self.bricks.remove(brick)
                    self.dy = -self.dy

            if not self.bricks:
                self.canvas.create_text(WIDTH/2, HEIGHT/2, text="You Win!", fill="white", font=("Arial", 30))
                self.master.after(2000, self.restart_game)

        self.master.after(20, self.update)

    def restart_game(self):
        self.canvas.delete("all")  
        self.create_game_objects()  

def main():
    root = tk.Tk()
    root.title("Breakout")
    game = BreakoutGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
