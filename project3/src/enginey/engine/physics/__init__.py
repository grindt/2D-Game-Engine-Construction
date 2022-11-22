###
### Entities
###

def make_particles():
    import enginey.engine.physics.entity.particle as prt
    return prt.Particle()

def make_gravity_force():
    import enginey.engine.physics.entity.force as frc
    return frc.GravityForce()

def make_spring_force():
    import enginey.engine.physics.entity.force as frc
    return frc.SpringForce()

def make_rectangle_collider(ulc, lrc):
    import enginey.engine.physics.entity.colliders as col
    return col.RectangleCollider(ulc, lrc)

def make_drag_force():
    import enginey.engine.physics.entity.force as frc
    return frc.DragForce()

###
### Actions
###

def make_gravity_action():
    import enginey.engine.physics.action.force_action as frcA
    return frcA.GravityForceAction()

def make_spring_action():
    import enginey.engine.physics.action.force_action as frcA
    return frcA.SpringForceAction()

def make_drag_action():
    import enginey.engine.physics.action.force_action as frcA
    return frcA.DragForceAction()

def make_position_solve_action():
    import enginey.engine.physics.action.solvers as slv
    return slv.positionSolveAction()

def make_velocity_solve_action():
    import enginey.engine.physics.action.solvers as slv
    return slv.velocitySolveAction()

def make_euler_solve_action():
    import enginey.engine.physics.action.solvers as slv
    return slv.EulerSolveAction()

def make_leap_frog_solve_action():
    import enginey.engine.physics.action.solvers as slv
    return slv.LeapFrogSolveAction()

def make_pick_position_action(i):
    import enginey.engine.physics.action.data_access as dataA
    return dataA.PickPositionAction(i)

def make_put_position_action(i):
    import enginey.engine.physics.action.data_access as dataA
    return dataA.PutPositionAction(i)

def make_inside_rectangle_collision():
    import enginey.engine.physics.action.collisions as cols
    return cols.InsideRectangleCollisionAction()

def make_outside_rectangle_collision():
    import enginey.engine.physics.action.collisions as cols
    return cols.OutsideRectangleCollisionAction()

def make_flip1_rectangle_collision():
    import enginey.engine.physics.action.collisions as cols
    return cols.Flip1RectangleCollisionAction()

def make_flip2_rectangle_collision():
    import enginey.engine.physics.action.collisions as cols
    return cols.Flip2RectangleCollisionAction()