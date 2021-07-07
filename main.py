from agents import run_random_baseline, reinforce
from MapWorld import MapWorldGym
from utils import save_parameters_and_results
import numpy as np
import time
import json
import os
import plotly.express as px
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("model", choices=['random', 'rl'], help="")
    parser.add_argument("--save", help="True")
    args = parser.parse_args()

    with open('results/all_parameters.json', 'r') as fp:
        parameters = json.load(fp)

    #
    mw_params = parameters['MapWorld']

    mwg = MapWorldGym(n=mw_params['n'], m=mw_params['m'], n_rooms=mw_params['n_rooms'],
                      room_types=mw_params['room_types'], room_repetitions=mw_params['room_repetitions'],
                      ade_path=mw_params['ade_path'],
                      caption_checkpoints=mw_params['caption_checkpoints'],
                      caption_vocab=mw_params['caption_vocab'],
                      image_resolution=(mw_params['image_width'], mw_params['image_height']))
    # # ade_path='../../data/ADE20K_2021_17_01/images/ADE/training')

    if args.model == 'random':
        model_return, model_steps, hits = run_random_baseline(mwg,
                                                              episodes=parameters['training']['num_episodes'])
    elif args.model == 'rl':
        model_return, model_steps, model_hits = reinforce(mwg, parameters['rl_baseline'], parameters['training'])

    model_return = [-400.0, -500.0, -600.0, -300.0, -600.0]
    model_steps = [4, 9, 15, 23, 29]
    model_hits = [0, 1, 0, 1, 1]

    # save_parameters_and_results(parameters, model_return, model_steps, model_hits)

    # model_steps = np.cumsum(model_steps)
    print('\n-------------------')
    # print('Return per model run: ', model_return)
    print('Mean return: ', np.mean(model_return))
    print('-------------------')
    # print('Total steps per model run', model_steps)
    print('Cumulative steps', np.cumsum(model_steps))
    print('Mean steps: ', np.mean(model_steps))
    print('-------------------')
    # print('model_hits', model_hits)
    print('accurracy', np.sum(model_hits)/len(model_hits))

    # def create_figure():
    #     title = 'Return over 5 episodes'
    #     x_axis = 'Steps'
    #     y_axis = 'Return'
    #     fig = px.line(x=np.cumsum(model_steps),
    #                   y=model_return,
    #                   title=title,
    #                   )
    #     fig.update_xaxes(title_text='Steps')
    #     fig.update_yaxes(title_text='Return')
    #     fig.show()
