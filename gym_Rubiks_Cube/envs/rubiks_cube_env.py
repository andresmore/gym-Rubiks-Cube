import gym as gym
from gym import spaces
import numpy as np
import random
from gym_Rubiks_Cube.envs import cube

actionList = [
    'f', 'r', 'l', 'u', 'd', 'b',
    '.f', '.r', '.l', '.u', '.d', '.b']

tileDict = {
    'R': 0,
    'O': 1,
    'Y': 2,
    'G': 3,
    'B': 4,
    'W': 5,
}


class RubiksCubeEnv(gym.Env):
    MAX_STEPS = 100
    metadata = {
        'render_modes': ['rgb_array', 'human', 'ansi'],
        'render_fps': 4
    }

    def __init__(self, render_mode='rgb_array', order_num=3):
        # the action is 6 move x 2 direction = 12
        self.doScramble = None
        self.render_mode = render_mode
        self.action_space = spaces.Discrete(12)
        # input is 9x6 = 54 array
        self.orderNum = order_num
        low = np.array([0 for i in range(self.orderNum * self.orderNum * 6)])
        high = np.array([5 for i in range(self.orderNum * self.orderNum * 6)])
        self.observation_space = spaces.Box(low, high, dtype=np.uint8)  # flattened
        self.step_count = 0

        self.scramble_low = 1
        self.scramble_high = 10

        self.obs = None
        self.scramble_log = None
        self.action_log = None
        self.ncube = None

    def step(self, action):
        self.action_log.append(action)
        self.ncube.minimalInterpreter(actionList[action])
        self.obs = self._get_obs()
        self.step_count = self.step_count + 1
        others = {}
        reward, done = self.calculateReward()

        terminated = done
        truncated = self.step_count > self.MAX_STEPS

        return self.obs, reward, terminated or truncated, others

    def calculateReward(self):
        reward = 0
        done = False
        if self.ncube.isSolved():
            reward = 1.0
            done = True
        return reward, done

    def reset(self, return_info=None, seed=None, options=None, scramble="auto"):
        super().reset(seed=seed)
        self.ncube = cube.Cube(order=self.orderNum)
        self.step_count = 0
        self.action_log = []
        self.scramble_log = []

        if scramble == "auto":
            self.scramble()
        elif scramble:
            for i in scramble:
                action_num = actionList.index(i)
                self.scramble_log.append(action_num)
                self.ncube.minimalInterpreter(actionList[action_num])

        ob = self._get_obs()

        return ob


    def _get_obs(self):
        return np.array([tileDict[i] for i in self.ncube.constructVectorState()], dtype=np.uint8)

    def render(self, mode='rgb_array', **kwargs):
        return self.ncube.display(self.render_mode)

    def set_scramble(self, low, high, do_scramble=True):
        self.scramble_low = low
        self.scramble_high = high
        self.doScramble = do_scramble

    def scramble(self):
        # set the scramber number
        scramble_num = random.randint(self.scramble_low, self.scramble_high)

        # check if scramble
        while self.ncube.isSolved():
            self.scramble_log = []
            for i in range(scramble_num):
                action = random.randint(0, 11)
                self.scramble_log.append(action)
                self.ncube.minimalInterpreter(actionList[action])

    def get_log(self):
        return self.scramble_log, self.action_log
