from manim import *
import numpy as np
import random

class BrownianMotion3D(ThreeDScene):
    def construct(self):
        # Setup
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.camera.background_color = DARK_GRAY

        # Create a transparent cube with white edges
        cube_size = 4
        cube = Cube(side_length=cube_size)
        cube.set_opacity(0.1)  # make faces transparent
        cube.set_stroke(color=WHITE, width=2)
        self.add(cube)

        # Create red balls (particles)
        num_balls = 10
        ball_radius = 0.1
        bounds = cube_size / 2 - ball_radius  # keep balls inside cube
        balls = []

        for _ in range(num_balls):
            position = np.array([
                random.uniform(-bounds, bounds),
                random.uniform(-bounds, bounds),
                random.uniform(-bounds, bounds)
            ])
            ball = Sphere(radius=ball_radius).move_to(position).set_color(RED)
            balls.append(ball)

        self.add(*balls)

        # Animate Brownian motion
        self.brownian_motion(balls, bounds, steps=5, step_size=0.15, duration=10)

    def brownian_motion(self, balls, bounds, steps=200, step_size=0.1, duration=10):
        min_run_time = 1 / 15  # For 15 FPS
        for _ in range(steps):
            animations = []
            for ball in balls:
                delta = np.random.normal(scale=step_size, size=3)
                new_pos = ball.get_center() + delta
                new_pos = np.clip(new_pos, -bounds, bounds)
                animations.append(ball.animate.move_to(new_pos))
            self.play(*animations, run_time=max(duration/steps, min_run_time), rate_func=linear)
