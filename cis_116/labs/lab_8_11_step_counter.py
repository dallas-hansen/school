def feet_to_steps(ft: float):
    steps = int(ft // 2.5)
    return steps


if __name__ == '__main__':
    feet_walked = float(input())
    print(feet_to_steps(feet_walked))
