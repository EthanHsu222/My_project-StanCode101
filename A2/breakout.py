"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import random as r
# Constants
FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    vy2 = vy
    vx = r.randint(-vy, vy)
    # Add the animation loop here!
    life = NUM_LIVES
    graphics.life_label.text = "Life left : " + str(life)
    while True:
        if life > 0:
            if graphics.begin is False:
                graphics.ball.move(vx, vy)
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    vx = -vx
                if graphics.ball.y <= 0:
                    vy = -vy
                if graphics.ball.y + graphics.ball.height < graphics.paddle.y:
                    # Remove the bricks.
                    if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is not None:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y))
                        vy = - vy
                        graphics.score += 1
                        graphics.score_speed += 1
                        graphics.score_label.text = 'Score: ' + str(graphics.score)
                    if graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y) is not None:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y))
                        vy = - vy
                        graphics.score += 1
                        graphics.score_speed += 1
                        graphics.score_label.text = 'Score: ' + str(graphics.score)
                    if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height) is not None:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height))
                        vy = - vy
                        graphics.score += 1
                        graphics.score_speed += 1
                        graphics.score_label.text = 'Score: ' + str(graphics.score)
                    if graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height) is not None:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height))
                        vy = - vy
                        graphics.score += 1
                        graphics.score_speed += 1
                        graphics.score_label.text = 'Score: ' + str(graphics.score)

                # To bounce back after hitting the paddle.
                elif graphics.ball.y + graphics.ball.height <= graphics.paddle.y + graphics.paddle.height and graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height) is not None:
                    vy = - vy
                elif graphics.ball.y + graphics.ball.height <= graphics.paddle.y + graphics.paddle.height and graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height) is not None:
                    vy = - vy
                # The ball under the paddle.
                elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.window.remove(graphics.ball)
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2, y=(graphics.window.height - graphics.ball.height * 2) / 2)
                    life -= 1
                    graphics.on_off = True
                    graphics.begin = False
                    graphics.life_label.text = "Life: " + str(life)
            pause(FRAME_RATE)
            if graphics.score_speed >= 5:
                vx *= 1.2
                graphics.score_speed = 0
        else:
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
