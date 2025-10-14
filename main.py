from manim import *
import numpy as np
import random

class BrownianMotion3D(ThreeDScene): #inheritance from manim predefined class
    def construct(self):
        # Setup
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES) #phi=vertical rotation | theta= horizontal rotation
        self.camera.background_color = DARK_GRAY

        # Create a transparent cube with white edges
        cube_size = 4
        cube = Cube(side_length=cube_size)
        cube.set_opacity(0.1)  # make faces transparent so we can see inside of cube
        cube.set_stroke(color=WHITE, width=2)
        self.add(cube) #add object to scene

        # Create red balls (particles)
        num_balls = 15
        ball_radius = 0.1
        bounds = cube_size / 2 - ball_radius  # keep balls inside cube while generating next random position
        balls = [] #list of balls which we animate

        for _ in range(num_balls):
            position = np.array([
                random.uniform(-bounds, bounds),
                random.uniform(-bounds, bounds),
                random.uniform(-bounds, bounds)
            ]) #position is defined by 3 coords:x,y,z.
            ball = Sphere(radius=ball_radius).move_to(position).set_color(RED)
            balls.append(ball)

        self.add(*balls) #add object to scene

        # Animate Brownian motion scene on screen
        self.brownian_motion(balls, bounds, steps=5, step_size=0.15, duration=10)

    def brownian_motion(self, balls, bounds, steps=200, step_size=0.1, duration=10):
        min_run_time = 1 / 15  # For 15 FPS :D QUICKER TO RUN 
        for _ in range(steps):
            animations = []
            for ball in balls:
                delta = np.random.normal(scale=step_size, size=3) #cat de mult se poate modifica in acest frame pozitia mingii
                new_pos = ball.get_center() + delta #calculezi noua pozitie
                new_pos = np.clip(new_pos, -bounds, bounds) #keeps position within cube bounds
                animations.append(ball.animate.move_to(new_pos))#store in animation list so each ball animation runs in PARALEL
            self.play(*animations, run_time=max(duration/steps, min_run_time), rate_func=linear) #actually run the animations
