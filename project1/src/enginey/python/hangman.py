import random
import pygame
from english_words import english_words_lower_alpha_set as words

import enginey.engine.actor as ac
import enginey.engine.play as pl

pygame.init()

################## Viewer ############################################# 

screen = pygame.display.set_mode([1280, 720])
viewer = pl.make_frame_viewer(screen)
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [ viewer ]

################## game setup ###########################################

###
###  Gallow render
###
#                        L  T   W   H
gallow_piece_1_bounds = (10,550,400,20)
gallow_piece_2_bounds = (200,50,20,500)
gallow_piece_3_bounds = (200,40,200,20)
gallow_piece_4_bounds = (400,40,20,100)
gallow_color = (255, 0, 0)

gallow_piece_1 = ac.make_basic_rectangle(gallow_piece_1_bounds, gallow_color)
gallow_piece_2 = ac.make_basic_rectangle(gallow_piece_2_bounds, gallow_color)
gallow_piece_3 = ac.make_basic_rectangle(gallow_piece_3_bounds, gallow_color)
gallow_piece_4 = ac.make_basic_rectangle(gallow_piece_4_bounds, gallow_color)

gallow_piece_1.insert_action(ac.make_draw_rectangle_action())
gallow_piece_2.insert_action(ac.make_draw_rectangle_action())
gallow_piece_3.insert_action(ac.make_draw_rectangle_action())
gallow_piece_4.insert_action(ac.make_draw_rectangle_action())

display.insert_entity(gallow_piece_1)
display.insert_entity(gallow_piece_2)
display.insert_entity(gallow_piece_3)
display.insert_entity(gallow_piece_4)

###
###  empty letter slots
###

word_list = list(words)

word = word_list[random.randint(0, len(words) - 1)]
while len(word) > 8 or len(word) < 5:
    word = word_list[random.randint(0, len(words) - 1)]

letter_slot_color = (0, 255, 0)
for i in range(len(word)):
    letter_slot_bounds = (10 + (100 * i) + (10 * i),680,100,20)

    letter_slot = ac.make_basic_rectangle(letter_slot_bounds, letter_slot_color)
    letter_slot.insert_action(ac.make_draw_rectangle_action())
    display.insert_entity(letter_slot)

###
###  hangman guy parts
###

head_radius = 50
head_pos = (410, 140)
body_bounds = (405, 180, 10, 220)
left_arm_bounds = (305, 250, 100, 10)
right_arm_bounds = (415, 250, 100, 10)
upper_leg_bounds = (305, 400, 200, 10)
left_leg_bounds = (305, 400, 10, 100)
right_leg_bounds = (495, 400, 10, 100)
hangman_color = (0, 0, 255)

head = ac.make_basic_circle(head_radius, hangman_color, head_pos)
body = ac.make_basic_rectangle(body_bounds, hangman_color)
left_arm = ac.make_basic_rectangle(left_arm_bounds, hangman_color)
right_arm = ac.make_basic_rectangle(right_arm_bounds, hangman_color)
upper_leg = ac.make_basic_rectangle(upper_leg_bounds, hangman_color)
left_leg = ac.make_basic_rectangle(left_leg_bounds, hangman_color)
right_leg = ac.make_basic_rectangle(right_leg_bounds, hangman_color)

head.insert_action(ac.make_draw_circle_action())
body.insert_action(ac.make_draw_rectangle_action())
left_arm.insert_action(ac.make_draw_rectangle_action())
right_arm.insert_action(ac.make_draw_rectangle_action())
upper_leg.insert_action(ac.make_draw_rectangle_action())
left_leg.insert_action(ac.make_draw_rectangle_action())
right_leg.insert_action(ac.make_draw_rectangle_action())

display.insert_entity(head)
display.insert_entity(body)
display.insert_entity(left_arm)
display.insert_entity(right_arm)
display.insert_entity(upper_leg)
display.insert_entity(left_leg)
display.insert_entity(right_leg)

game_content.append(head)
game_content.append(body)
game_content.append(left_arm)
game_content.append(right_arm)
game_content.append(upper_leg)
game_content.append(left_leg)
game_content.append(right_leg)

game_content.append(word)

################## Looper #############################################

game_looper = pl.make_game_loop(game_content)
game_looper.loop()