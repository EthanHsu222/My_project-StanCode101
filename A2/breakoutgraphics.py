"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random as r

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 30       # Width of a brick (in pixels)
BRICK_HEIGHT = 10      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 50      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 10     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
FRAME_RATE = 1000/120


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - PADDLE_WIDTH) / 2, y=window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - ball_radius * 2) / 2, y=(window_height - ball_radius * 2) / 2)
        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = r.randint(1, MAX_X_SPEED)
        if r.random() > 0.5:
            self.__dx = - self.__dx
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        self.begin = False
        self.on_off = True
        onmouseclicked(self.on_off)
        # Draw bricks
        for i in range(BRICK_COLS):
            self.Rec = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=BRICK_SPACING+i*(BRICK_SPACING+BRICK_WIDTH), y=BRICK_OFFSET)
            self.Rec.filled = True
            self.window.add(self.Rec)
            for j in range(BRICK_ROWS):
                self.Rec = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=BRICK_SPACING + i * (BRICK_SPACING + BRICK_WIDTH),
                                 y=BRICK_OFFSET+j*(BRICK_SPACING+BRICK_HEIGHT))
                self.Rec.filled = True
                if j == 1 or j == 2:
                    self.Rec.fill_color = 'black'
                elif j == 3 or j == 4:
                    self.Rec.fill_color = 'green'
                elif j == 5 or j == 6:
                    self.Rec.fill_color = 'red'
                elif j == 7 or j == 8:
                    self.Rec.fill_color = 'orange'
                else:
                    self.Rec.fill_color = 'blue'
                self.window.add(self.Rec)
        # Score label
        self.score_speed = 0
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-20'
        self.window.add(self.score_label, (self.window.width - self.score_label.width) / 2, self.score_label.height)

        # Life label
        self.life_label = GLabel('Life: ')
        self.life_label.font = '-20'
        self.window.add(self.life_label, 0, self.score_label.height)

    def on_off(self,mouse):
        if self.on_off is False:
            self.on_off = True
            self.begin = True
        else:
            if mouse.y < self.paddle.y and self.window.get_object_at(mouse.x, mouse.y) is not None:
                for i in range(0, self.window.width):
                    self.window.remove(self.window.get_object_at(i, mouse.y))

    def paddle_move(self, mouse):
        self.paddle.y = self.window.height - PADDLE_OFFSET
        self.paddle.x = mouse.x - self.paddle.width / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def get_vx(self):
        vx = r.randint(-MAX_X_SPEED, MAX_X_SPEED)
        self.__dx = vx
        return self.__dx

    def get_vy(self):
        return self.__dy

    def dead(self):
        self.dead_label = GLabel('Final Score: ' + str(self.score)+ '& You are FINISHED')
        self.dead_label.font = '-35'
        self.window.add(self.dead_label, (self.window.width - self.dead_label.width) / 2, (self.window.height - self.dead_label.height)/2)

