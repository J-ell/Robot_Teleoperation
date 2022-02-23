import simulation as sim
import sys
import rospy
import rospkg
import os


def tele_function():
    sim.initialize_simulation()

    def forward(duration=3):
        return sim.go_forward(10, duration)

    def left_turn(duration=3):
        return sim.spin_left(20, duration)

    def right_turn(duration=3):
        return sim.spin_right(20, duration)

    def backward(duration=3):
        return sim.go_backward(20, duration)

    my_dict = dict(w="forward_motion", a="left_turn", d="right_turn", s="backward_motion")

    while True:
        while True:
            motion_key = input("Enter a motion key:  ")
            try:
                motion_key = motion_key.lower()
                if motion_key not in my_dict:
                    raise ValueError()
            except:
                print("wrong input: key must be either 'w', 'a' ,'s', or 'd' ")
            if motion_key in my_dict:
                break

        if motion_key == "w":
            forward()
            sim.stop_moving_for()
        elif motion_key == "a":
            left_turn()
            sim.stop_moving_for()
        elif motion_key == "d":
            right_turn()
            sim.stop_moving_for()
        elif motion_key == "s":
            backward()
            sim.stop_moving_for()


if __name__ == "__main__":
    if not rospy.is_shutdown():
        tele_function()


