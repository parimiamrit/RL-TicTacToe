import sys
import numpy as np
import random
from agents import *
import dill as pickle
from environment.ttt_env import TicTacToe

def play_1_game(env, agent1, agent2, start, train):
    round = 1
    while(env.end == False):
        if (round+start)%2:
            agent = agent1
        else:
            agent = agent2
        prev_state = env.state().copy()
        action = agent.action(prev_state, train).copy()
        env.act(action, agent.playerid)
        state = env.state().copy()
        if train:
            agent.learn(env.reward, prev_state, state)
        round += 1
    return env.winner

def play(env, agent1, agent2, iterations=10000, train=True):
    res = {'X':0,'O':0,'D':0}
    for iteration in range(iterations):
        env.reset()
        p = random.random()
        if p>0.5:
            start = 1
        else:
            start = 2
        winner = play_1_game(env, agent1, agent2, start, train)
        res[winner] += 1
        # print(iteration, winner)
        if (iteration+1)%1000==0 and train:
            print(res)
            res = {'X':0,'O':0,'D':0}
    print('res',res)
    print(env.reward)
    print(len(agent1.q))
    return res

if __name__ == '__main__':
    if len(sys.argv) == 1:
        agent1 = q_agent.qagent('X')
        # agent2 = safe_agent.safeagent('O')
        agent2 = random_agent.randomagent('O')
    env = TicTacToe()
    play(env, agent1, agent2, iterations=10000)
    play(env, agent1, agent2, iterations=1000, train=False)
    with open('ql.pkl', 'wb') as f:
        pickle.dump(agent1.q, f)