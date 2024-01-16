# # Import required library
# import time
# import turtle
#
# # Create screen
# sc = turtle.Screen()
# sc.title("Pong game")
# sc.bgcolor("white")
# sc.setup(width=1000, height=600)
#
# time.sleep(10)
#
# # Left paddle
# left_pad = turtle.Turtle()
# left_pad.speed(0)
# left_pad.shape("square")
# left_pad.color("black")
# left_pad.shapesize(stretch_wid=6, stretch_len=2)
# left_pad.penup()
# left_pad.goto(-400, 0)
#
# time.sleep(10)
#
# # Right paddle
# right_pad = turtle.Turtle()
# right_pad.speed(0)
# right_pad.shape("square")
# right_pad.color("black")
# right_pad.shapesize(stretch_wid=6, stretch_len=2)
# right_pad.penup()
# right_pad.goto(400, 0)
#
# time.sleep(10)
#
# # Ball of circle shape
# hit_ball = turtle.Turtle()
# hit_ball.speed(40)
# hit_ball.shape("circle")
# hit_ball.color("blue")
# hit_ball.penup()
# hit_ball.goto(0, 0)
# hit_ball.dx = 5
# hit_ball.dy = -5
#
# time.sleep(10)



def longest_substring(s):
    longest_len = 0
    longest_str = ''

    for i in range(len(s)):
        current_str = ""
        for j in range(i, len(s)):
            if s[j] not in current_str:
                current_str += s[j]
                curr_len = longest_len
                longest_len = max(longest_len, len(current_str))
                if longest_len > curr_len:
                    longest_str = current_str
            else:
                break
    # print the longest substring and its length
    print(f'The longest substring: {longest_str}, length: {longest_len}')


# example to test the above longest substring program
x = 'ACDBVWGVRWFRADS'
longest_substring(x)

