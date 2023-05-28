from robotics import Robot

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()
    robot.robot_steps()


def main():
    introduce_yourself()
    robot.retrieve_scientist_data()
    robot.say_goodbye()


if __name__ == "__main__":
    main()
