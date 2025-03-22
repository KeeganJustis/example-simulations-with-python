#%% 
from modsim import *
import numpy as np
import pandas as pd
import pint
from numpy import linspace




bikeshare1 = State(olin=10, wellesley=2,wellesley_empty=0)
bikeshare2 = State(olin=2, wellesley=10,wellesley_empty=0)
def bike_to_wellesley(state):
    """Move one bike from Qwllway to Olin
    state: bikeshare state object
    """
    # print("Moving a bike to Wellesley")
    if state.olin > 0:
        state.olin -= 1
        state.wellesley += 1
    else:
        state.olin_empty += 1
        # print("No bikes to move from Olin")
    return state



def bike_to_olin(state):
    """Update the state of the system."""
    # print("Moving a bike to Olin")
    if state.wellesley > 0:
         state.olin += 1
         state.wellesley -= 1
    else:
        state.wellesley_empty += 1
        # print("No bikes to move from wellesley")
    return state
   

def flip(p=0.5):
    """Flips a coin with the given probability.

    p: float 0-1

    returns: boolean (True or False)
    """
    return np.random.random() < p

def step(p1,p2,state):
    """Update the state of the system."""
    if flip(p1):
        bike_to_wellesley(state)
    if flip(p2):
        bike_to_olin(state)
        

def make_state(olin,wellesley):
    return State(olin=olin,wellesley=wellesley,wellesley_empty=0,olin_empty=0)

def run_simulation(p1, p2, num_steps):
    """Run the simulation."""
    state = make_state(olin=10, wellesley=2)
    results = TimeSeries()
    results[0] = state.olin  # Store initial number of bikes at Olin
    # print("bikes in olin: ", state.olin)
    # print("bikes in wellesley: ", state.wellesley)
    for steps in range(num_steps):
        step(p1, p2, state)
        results[steps+1] = state.olin
    return state, results
    
p1_array = linspace(0,1,101)
p2_array = linspace(0,1,101)

def sweep_p1(p1_array,p2=0.2,num_steps=60):
    sweep = SweepSeries()
    for p1 in p1_array:
        final_state = run_simulation(p1,p2,num_steps)
        sweep[p1]= final_state.olin_empty
    return sweep

def sweep_p2(p2_array):
    sweep = SweepSeries()
    p1 = 0.5
    num_steps = 60
    for p2 in p2_array:
        final_state = run_simulation(p1,p2,num_steps)
        sweep[p2]= final_state.olin_empty
    return sweep

sweep_1 = sweep_p1(p1_array)

sweep_1.plot()
decorate(title='Olin-Wellesley Bikeshare',xlabel='Customer rate at olin, customer per minute',ylabel='Number of unhappy customers at olin')
# %%
sweep_2 = sweep_p2(p2_array)

sweep_2.plot()
decorate(title='Olin-Wellesley Bikeshare',xlabel='Customer rate at olin, customer per minute',ylabel='Number of unhappy customers at olin')

# %%
# def run_multiple_simulations(p1, p2, num_steps, num_runs):
#     """Run multiple simulations and return the average results.
    
#     p1: probability of bike moving to Wellesley
#     p2: probability of bike moving to Olin
#     num_steps: number of steps per simulation
#     num_runs: number of simulations to run
#     """
#     # Initialize array to store results from all runs
#     all_results = np.zeros((num_runs, num_steps + 1))
    
#     for run in range(num_runs):
#         _, results = run_simulation(p1, p2, num_steps)
#         all_results[run] = np.array(list(results))
    
#     # Calculate average results across all runs
#     average_results = TimeSeries()
#     for step in range(num_steps + 1):
#         average_results[step] = np.mean(all_results[:, step])
    
#     return average_results

# %%
def run_multiple_simulations(p1_array, p2, num_steps, num_runs):
    """Run multiple simulations and return the average results.
    
    p1: probability of bike moving to Wellesley
    p2: probability of bike moving to Olin
    num_steps: number of steps per simulation
    num_runs: number of simulations to run
    """

    p2 = 0.3
    for run in range(num_runs):
        for i, p1 in enumerate(p1_array):
            if i == 0 and run == 0:
                _, all_results = run_simulation(p1, p2, num_steps)
            else: 
                _, results = run_simulation(p1, p2, num_steps)
                all_results = pd.concat([all_results,results],axis=1)
    
    
    # Calculate average results across all runs
    all_results["Mean"] = all_results.loc[:,[c for c in all_results.columns if c!= "Time"]].mean(axis=1)
    final_df = all_results[["Mean"]]
    print(final_df)
    return final_df

p1_array = linspace(0,1,101)
final_results = run_multiple_simulations(p1_array,p2=0.3,num_steps=60,num_runs=20)
show(final_results)
final_results.plot()
decorate(title='Olin-Wellesley Bikeshare',xlabel='Time step',ylabel='Number of unhappy customers at olin')

# %%
