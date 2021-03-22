from maps import AbstractMap, ADEMap
from mapworld import MapWorld, MapWorldWrapper
import numpy as np
import gym
import cv2


# FIXME remove unnecessary 'outdoor' rooms from maps.py (church, street etc.)

class MapWorldGym(gym.Env):

    def __init__(self, n=4, m=4, n_rooms=10, room_types=2, room_repetitions=2):
        # the dimensions of the map
        self.n = n
        self.m = m
        # the number of rooms on the map
        self.n_rooms = n_rooms
        #
        self.room_types = room_types
        self.room_repetitions = room_repetitions

        self.done = False

        # FIXME load yolo, im2txt word_embeddings models
        self.object_detection_model = 0
        self.image_caption_model = 0
        self.word_embeddings = 0

        # the question is the caption generated from a randomly sampled room
        self.question = ''

        # print(self.n, self.m, self.n_rooms, self.room_types, self.room_repetitions)

    def reset(self):
        """
        resets the environment to its initial values
        samples a new map, generates a question from the map

        """
        # initialise a ne MapWorld object with the parameters set in the init
        ade_map = ADEMap(self.n, self.m, self.n_rooms,
                         (self.room_types, self.room_repetitions))
        # FIXME add MapWorldWrapper
        self.mw = MapWorld(ade_map.to_fsa_def(), ['instance', 'type'])

        # generate question based on the sampled map
        self.generate_question()

        #
        # FIXME get randomised initial position
        image = 0

        # FIXME rename state to something clearer
        state = self.get_state(image)

        # FIXME get available actions from Map
        available_actions = []

        # return the initial state/observation
        return [state, self.question, available_actions]

    def step(self, action):
        """

        :param action:
        :return: observations as a list, contains the state, reward,
        """

        # FIXME penalize wrong actions
        if action == 'n':
            reward = -10.0
            state = self.mw.try_transition(action)

        elif action == 'o':
            reward = -10.0
            state = self.mw.try_transition(action)

        elif action == 's':
            reward = -10.0
            state = self.mw.try_transition(action)

        elif action == 'w':
            reward = -10.0
            state = self.mw.try_transition(action)

        elif action == 'answer':

            # FIXME get current room from observations

            # FIXME use get_captions to generate caption for room

            # FIXME compare generated captions with question

            # FIXME return reward based on the comparison
            if True:
                reward = 100.0
            else:
                reward = -100.0

            # Terminate the game
            self.done = True

        return [state, reward, self.done, {}]   # no clue what the point of the dict is

    def get_captions(self, image):
        """

        :param image:
        :return:
        """
        # FIXME preprocess captions
        captions = self.image_caption_model(image)


        # FIXME apply word embeddings
        return captions

    def get_state(self, image):
        """

        :param image:
        :return:
        """
        # FIXME rename function ?
        # FIXME preprocess yolo output

        # FIXME apply word embeddings
        state = ''

        return state

    def answer_question(self, state):

        done = False

        return done

    def generate_question(self):
        """

        """
        # FIXME sample random image from self.mw

        image = cv2.imread()

        question = self.get_captions(image)

        # FIXME apply word embeddings
        self.question = question

    def render(self, mode='human'):
        # FIXME probably not really necessary
        pass


if __name__ == '__main__':

    m = MapWorldGym()

    print()

