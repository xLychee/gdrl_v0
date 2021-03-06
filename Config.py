# Copyright (c) 2016, NVIDIA CORPORATION. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import os
import gym
from itertools import product

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


class Config:
    #########################################################################
    # Game configuration

    # Name of the game, with version (e.g. PongDeterministic-v0)


    # ATARI_GAME = 'PongDeterministic-v0'
    ATARI_GAME = 'QbertDeterministic-v0'
    # ATARI_GAME = 'BreakoutDeterministic-v0'

    # Device
    DEVICE = 'gpu:0'

    # Load old models. Throws if the model doesn't exist
    LOAD_CHECKPOINT = False
    # If 0, the latest checkpoint is loaded
    LOAD_EPISODE = 0

    # Results filename
    RESULTS_FILENAME = 'qbert_dep_a2.txt'

    #########################################################################
    # Enable to see the trained agent in action
    PLAY_MODE = False
    # Enable to train
    TRAIN_MODELS = True

    #########################################################################
    # Number of agents, predictors, trainers and other system settings

    # If the dynamic configuration is on, these are the initial values.
    # Number of Agents
    AGENTS = 32
    # Number of Predictors
    PREDICTORS = 2
    # Number of Trainers
    TRAINERS = 2

    # Enable the dynamic adjustment (+ waiting time to start it)
    DYNAMIC_SETTINGS = True
    DYNAMIC_SETTINGS_STEP_WAIT = 20
    DYNAMIC_SETTINGS_INITIAL_WAIT = 10

    #########################################################################
    # Algorithm parameters

    # Discount factor
    DISCOUNT = 0.99

    # Tmax
    TIME_MAX = 5

    # Reward Clipping
    REWARD_MIN = -1
    REWARD_MAX = 1

    # Max size of the queue
    MAX_QUEUE_SIZE = 100
    PREDICTION_BATCH_SIZE = 128

    # Input of the DNN
    STACKED_FRAMES = 4
    IMAGE_WIDTH = 84
    IMAGE_HEIGHT = 84

    # Total number of episodes and annealing frequency
    EPISODES = 400000
    ANNEALING_EPISODE_COUNT = 400000

    # Entropy regualrization hyper-parameter
    BETA_START = 0.01
    BETA_END = 0.01

    # Learning rate
    LEARNING_RATE_START = 0.0003
    LEARNING_RATE_END = 0.0003

    # RMSProp parameters
    RMSPROP_DECAY = 0.99
    RMSPROP_MOMENTUM = 0.0
    RMSPROP_EPSILON = 0.1

    # Dual RMSProp - we found that using a single RMSProp for the two cost function works better and faster
    DUAL_RMSPROP = False

    # Gradient clipping
    USE_GRAD_CLIP = False
    GRAD_CLIP_NORM = 40.0
    # Epsilon (regularize policy lag in GA3C)
    LOG_EPSILON = 1e-6
    # Training min batch size - increasing the batch size increases the stability of the algorithm, but make learning slower
    TRAINING_MIN_BATCH_SIZE = 30

    #########################################################################
    # Log and save

    # Enable TensorBoard
    TENSORBOARD = False
    # Update TensorBoard every X training steps
    TENSORBOARD_UPDATE_FREQUENCY = 1000

    # Enable to save models every SAVE_FREQUENCY episodes
    SAVE_MODELS = True
    # Save every SAVE_FREQUENCY episodes
    SAVE_FREQUENCY = 1000

    # Print stats every PRINT_STATS_FREQUENCY episodes
    PRINT_STATS_FREQUENCY = 1
    # The window to average stats
    STAT_ROLLING_MEAN_WINDOW = 1000

    # Network checkpoint name
    NETWORK_NAME = 'network'

    #########################################################################
    # More experimental parameters here

    # Minimum policy
    MIN_POLICY = 0.0
    # Use log_softmax() instead of log(softmax())
    USE_LOG_SOFTMAX = False

    #########################################################################
    '''
    BASIC_ACTION_SET = [0, 1, 2, 3, 4, 5]  # (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    ENLARGED_ACTION_SET = [(0,), (1,), (2,), (3,), (4,), (5,),
                           (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                           (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                           (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
                           (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
                           (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
                           (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
    
    BASIC_ACTION_SET = [0, 1, 2, 3]  # (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    ENLARGED_ACTION_SET = [(0,), (1,), (2,), (3,),
                           (0, 0), (0, 1), (0, 2), (0, 3),
                           (1, 0), (1, 1), (1, 2), (1, 3),
                           (2, 0), (2, 1), (2, 2), (2, 3),
                           (3, 0), (3, 1), (3, 2), (3, 3)]
    '''
    env_temp = gym.make(ATARI_GAME)
    BASIC_ACTION_SET = list(range(env_temp.action_space.n))
    ENLARGED_ACTION_SET = [(itm,) for itm in BASIC_ACTION_SET] + list(product(BASIC_ACTION_SET, BASIC_ACTION_SET))

    def build_action_index_map(action_set):
        index = 0
        result = {}
        for a in action_set:
            result[a] = index
            result[index] = a
            index += 1
        return result

    NUM_ENLARGED_ACTIONS = len(ENLARGED_ACTION_SET)
    ACTION_INDEX_MAP = build_action_index_map(ENLARGED_ACTION_SET)

    LOOK_AHEAD_STEPS = 4
