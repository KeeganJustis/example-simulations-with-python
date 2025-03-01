#%% 
import pint
import numpy as np
import pandas as pd
from modsim import *


def State(**variables):
    """Contains the values of state variables."""
    return pd.Series(variables, name='state')


def decorate(**options):
    """Decorate the current axes.

    Call decorate with keyword arguments like
    decorate(title='Title',
             xlabel='x',
             ylabel='y')

    The keyword arguments can be any of the axis properties
    https://matplotlib.org/api/axes_api.html
    """
    ax = plt.gca()
    ax.set(**options)

    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(handles, labels)

    plt.tight_layout()

bikeshare1 = State(olin=10, wellesley=2,wellesley_empty=0)
bikeshare2 = State(olin=2, wellesley=10,wellesley_empty=0)
def bike_to_wellesley(state):
    """Move one bike from Qwllway to Olin
    state: bikeshare state object
    """
    print("Moving a bike to Wellesley")
    if state.olin > 0:
        state.olin -= 1
        state.wellesley += 1
    else:
        state.wellesley_empty += 1
        print("No bikes to move from Olin")
    return state



def bike_to_olin(state):
    """Update the state of the system."""
    print("Moving a bike to Olin")
    print("Moving a bike to Olin")
    if state.olin > 0:
         state.olin += 1
         state.wellesley -= 1
    else:
        state.wellesley_empty += 1
        print("No bikes to move from Olin")
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
        


def run_simulation(p1,p2,num_steps,state):
    """Run the simulation."""
    print("bikes in olin: ",state.olin)
    print("bikes in wellesley: ",state.wellesley)
    results = TimeSeries()
    results[0] = state.olin
    for steps in range(num_steps):
        step(p1,p2,state)
        results[steps+1] = state.olin
    results.plot()
    decorate(title='Olin-Wellesley Bikeshare',xlabel='Time step (min)',ylabel='Number of bikes')
    print(results)
    show(results)
    print("bikes in olin: ",state.olin)
    print("bikes in wellesley: ",state.wellesley)


run_simulation(0.3,0.2,60,bikeshare1)
# %%
