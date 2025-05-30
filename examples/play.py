import gym
import gym_Rubiks_Cube
# 3x3 Rubik's Cube

env = gym.make("RubiksCube-v0")

env.set_scramble(1, 10, False)
print(env.reset()) # print status
env.render()

env.set_scramble(1, 10, True)
print(env.reset()) # scramble status
env.render()
env.step(0) # action 0~11
env.step(1) # action 0~11
env.render()
scramble, action = env.get_log()
print("Scramble: ", scramble)
print("Action: ", action)


# 2x2 Rubik's Cube
env = gym.make("RubiksCube2x2-v0")

print(env.reset()) # scramble status
env.render()
env.step(0) # action 0~11
env.step(1) # action 0~11
env.render()
scramble, action = env.get_log()
print("Scramble: ", scramble)
print("Action: ", action)



