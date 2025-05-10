from gym.envs.registration import register

register(
    id='RubiksCube-v0',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
    new_step_api=True

)

register(
    id='RubiksCube2x2-v0',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
    kwargs={'order_num' : 2},
    new_step_api=True
)
