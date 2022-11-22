import pygame

import enginey.engine.play as pl
import enginey.engine.actor as ac
import enginey.engine.utility as utl
import enginey.engine.physics as phys
import random as rand

###
### random funcs
###

def random_pos(nx, ny):
    return (rand.randint(10, nx-10), rand.randint(10, ny-10))

def random_color():
    return (rand.randint(10,255), rand.randint(10,255), rand.randint(10,255))

###
### circles
###

def get_circles(nx, ny, nb):
    circles = []
    radius = 8
    for i in range(0,nb):
        circle_bounds = random_pos(nx, ny)
        circle_color = random_color()
        circle = ac.make_basic_circle(radius, circle_color, circle_bounds)
        circle.name = "circle_" + str(i)
        circle.insert_action(ac.make_draw_circle_action())
        circles.append(circle)
    return circles

###
### Physics
###

def get_particles(init_data):
    particles = []

    parts = phys.make_particles()
    particles.append(parts)

    for d in init_data:
        position = list(d.location)
        velocity = [(30.0*rand.random() - 1.0), (2.0*rand.random() - 1.0)]
        mass = 1.0
        parts.add_particle(position, velocity, mass)

    gravity = phys.make_gravity_force()
    gravity.gravity = [0.0,0.1]
    grav_action = phys.make_gravity_action()
    gravity.insert_action(grav_action)

    spring = phys.make_spring_force()
    spring.spring_constant = 0.01
    spring_action = phys.make_spring_action()
    spring.insert_action(spring_action)

    drag = phys.make_drag_force()
    drag.drag_constant = 0.01
    drag_action = phys.make_drag_action()
    drag.insert_action(drag_action)

    psolve = phys.make_position_solve_action()
    parts.insert_action(psolve)

    vsolve = phys.make_velocity_solve_action()
    parts.insert_action(vsolve)
    vsolve.children.append(grav_action)
    vsolve.children.append(drag_action)
    vsolve.children.append(spring_action)

    esolve = phys.make_euler_solve_action()
    esolve.dt = 0.1
    parts.insert_action(esolve)
    esolve.children.append(psolve)
    esolve.children.append(vsolve)
    esolve.types.append("loop")

    for i in range(0, len(init_data)):
        pick = phys.make_pick_position_action(i)
        put = phys.make_put_position_action(0)

        parts.insert_action(pick)
        init_data[i].insert_action(put)
        pick.children.append(put)

        esolve.children.append(pick)

    window_frame_collider = phys.make_rectangle_collider([0,0], [1280,720])
    collisions = phys.make_inside_rectangle_collision()
    window_frame_collider.insert_action(collisions)
    psolve.children.append(collisions)

    spring_zone_collider = phys.make_rectangle_collider([0,0], [821,720])
    spring_zone_collision = phys.make_flip2_rectangle_collision()
    spring_zone_collider.insert_action(spring_zone_collision)
    psolve.children.append(spring_zone_collision)

    gravity_zone_collider = phys.make_rectangle_collider([822,0], [1280,720])
    gravity_zone_collision = phys.make_flip1_rectangle_collision()
    gravity_zone_collider.insert_action(gravity_zone_collision)
    psolve.children.append(gravity_zone_collision)

    wall_part_1_collider = phys.make_rectangle_collider([786,0], [856,200])
    wall_part_1_collision = phys.make_outside_rectangle_collision()
    wall_part_1_collider.insert_action(wall_part_1_collision)
    psolve.children.append(wall_part_1_collision)

    wall_part_2_collider = phys.make_rectangle_collider([786,200], [856,275])
    wall_part_2_collider.name = "special_rect"
    wall_part_2_collider.active = False
    timer.alarmChild.append(wall_part_2_collider)
    wall_part_2_collision = phys.make_outside_rectangle_collision()
    wall_part_2_collider.insert_action(wall_part_2_collision)
    psolve.children.append(wall_part_2_collision)

    wall_part_3_collider = phys.make_rectangle_collider([786,275], [856,720])
    wall_part_3_collision = phys.make_outside_rectangle_collision()
    wall_part_3_collider.insert_action(wall_part_3_collision)
    psolve.children.append(wall_part_3_collision)

    platform_1_collider = phys.make_rectangle_collider([1082,550], [1182,570])
    platform_1_collision = phys.make_outside_rectangle_collision()
    platform_1_collider.insert_action(platform_1_collision)
    psolve.children.append(platform_1_collision)

    platform_2_collider = phys.make_rectangle_collider([900,670], [1000,690])
    platform_2_collision = phys.make_outside_rectangle_collision()
    platform_2_collider.insert_action(platform_2_collision)
    psolve.children.append(platform_2_collision)

    return particles

pygame.init()

################## Viewer ############################################# 

screen = pygame.display.set_mode([1280, 720])
viewer = pl.make_frame_viewer(screen)
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [ viewer ]

################## game setup ###########################################

###
### Game Timer
###

timer = utl.make_timer()
timer.insert_action(utl.make_start())
timer.insert_action(utl.make_alarm(9000))
timer.insert_action(utl.make_update())

game_content.append(timer)

###
### Play Area
###

wall_part_1_bounds = (786,0,70,200)
wall_part_2_bounds = (786,200,70,75)
wall_part_3_bounds = (786,275,70,445)

platform_1_bounds = (1082, 550, 100, 20)
platform_2_bounds = (900, 670, 100, 20)

wall_color = (255, 255, 255)

#make rectangles

wall_part_1 = ac.make_basic_rectangle(wall_part_1_bounds, wall_color)
wall_part_2 = ac.make_basic_rectangle(wall_part_2_bounds, wall_color)
wall_part_2.name = "special_rect"
wall_part_2.active = False
timer.alarmChild.append(wall_part_2)
wall_part_3 = ac.make_basic_rectangle(wall_part_3_bounds, wall_color)

platform_1 = ac.make_basic_rectangle(platform_1_bounds, wall_color)
platform_2 = ac.make_basic_rectangle(platform_2_bounds, wall_color)

#draw action inserts
wall_part_1.insert_action(ac.make_draw_rectangle_action())
wall_part_2.insert_action(ac.make_draw_rectangle_action())
wall_part_3.insert_action(ac.make_draw_rectangle_action())

platform_1.insert_action(ac.make_draw_rectangle_action())
platform_2.insert_action(ac.make_draw_rectangle_action())

display.insert_entity(wall_part_1)
display.insert_entity(wall_part_2)
display.insert_entity(wall_part_3)
display.insert_entity(platform_1)
display.insert_entity(platform_2)

#add to game_content
game_content.append(wall_part_1)
game_content.append(wall_part_2)
game_content.append(wall_part_3)
game_content.append(platform_1)
game_content.append(platform_2)

###
### circles
###

circs = get_circles(786, 720, 100)
particles = get_particles(circs)

game_content = game_content + circs + particles

for b in circs:
    display.insert_entity(b)

################## Looper #############################################

game_looper = pl.make_game_loop(game_content)
game_looper.loop()