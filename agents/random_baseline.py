import numpy as np
from tqdm import tqdm
from time import time


def run_random_baseline(mapgame, logger, episodes=20000):
    """

    Args:
        mapgame:
        logger:
        episodes:
    Returns:

    """
    model_return = []
    model_steps = []
    hits = []
    for _ in tqdm(range(episodes)):

        t_r = time()
        _ = mapgame.reset()
        logger.debug(f'Time for env reset {time() - t_r}')
        available_actions = mapgame.total_available_actions
        done = False
        while not done:
            t_s = time()
            action = np.random.randint(0, len(available_actions))
            _, _, done, room_found = mapgame.step(action)

            logger.debug(f'Time for env step {time()-t_s}')
        t_a = time()
        model_return.append(mapgame.model_return)
        model_steps.append(mapgame.model_steps)
        hits.append(room_found)
        logger.debug(f'Time for append {time()-t_a}')
        logger.debug(f'Time for an episode {time()-t_r} \n')

    return model_return, model_steps, hits
