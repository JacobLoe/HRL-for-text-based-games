from agents import RandomBaseline
from MapWorld import MapWorldGym
# from im2txt import Captioning
import numpy as np

if __name__ == '__main__':

    mwg = MapWorldGym()
    initial_state = mwg.reset()
    # print(np.shape(initial_state))
    # print(initial_state)
    available_actions = mwg.available_actions
    num_actions = mwg.num_actions
    # print(num_actions, available_actions)
    rb = RandomBaseline()

    # while not mwg.done:
    #     action = available_actions[rb.select_action(len(available_actions))]
    #     s = mwg.step(action)
    #     available_actions = s[0][2]
    #     print(s[0][2], s[1])

    # obj = Captioning("./im2txt/checkpoints/5M_iterations/model.ckpt-5000000", './im2txt/vocab/word_counts.txt')
    #
    # cap = obj.image("./MapWorld/ADE20k_test.jpg")
    #
    # print(cap)
    # print(type(cap))
