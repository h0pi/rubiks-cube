import pyray as pr
import configs
from rubik import Rubik
import numpy as np
from utils import generate_random_movements

pr.init_window (
    configs.window_h,
    configs.window_w,
    "Building a Rubik's Cube"
)
rubik_cube = Rubik()

rotation_queue = generate_random_movements(120)



pr.set_target_fps(configs.fps)

while not pr.window_should_close():

    rotation_queue, _ = rubik_cube.handle_rotation(rotation_queue)

    pr.update_camera(configs.camera,
                     pr.CameraMode.CAMERA_THIRD_PERSON)
    
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)


    pr.begin_mode_3d(configs.camera)
    for i, cube in enumerate(rubik_cube.cubes):
        for cube_part in cube:
            position = pr.Vector3(cube[0].center[0], cube[0].center[1], cube[0].center[2])

            #print(cube[0].center)

            pr.draw_model(cube_part.model, position, 2, cube_part.face_color)

    pr.draw_grid(20,1.0)

    pr.end_mode_3d()
    pr.end_drawing()

pr.close_window()