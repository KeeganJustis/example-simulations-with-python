#%% 
import pint
from modsim import *
import numpy as np


def State(**variables):
    """Contains the values of state variables."""
    return pd.Series(variables, name='state')


bikeshare = State(olin=10, wellesley=2,downtown=0)

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

def bike_to_wellesley():
    """Update the state of the system."""
    print("Moving a bike to Wellesley")
    bikeshare.olin -= 1
    bikeshare.wellesley += 1



def bike_to_olin():
    """Update the state of the system."""
    print("Moving a bike to Olin")
    bikeshare.olin += 1
    bikeshare.wellesley -= 1

def flip(p=0.5):
    """Flips a coin with the given probability.

    p: float 0-1

    returns: boolean (True or False)
    """
    return np.random.random() < p

def step(p1,p2):
    """Update the state of the system."""
    if flip(p1):
        bike_to_wellesley()
    if flip(p2):
        bike_to_olin()
        


def run_simulation(p1,p2,num_steps):
    """Run the simulation."""
    print("bikes in olin: ",bikeshare.olin)
    print("bikes in wellesley: ",bikeshare.wellesley)
    print("bikes in downtown: ",bikeshare.downtown)
    results = TimeSeries()
    results[0] = bikeshare.olin
    for steps in range(num_steps):
        step(p1,p2)
        results[steps+1] = bikeshare.olin
    results.plot()
    decorate(title='Olin-Wellesley Bikeshare',xlabel='Time step (min)',ylabel='Number of bikes')
    print(results)
    show(results)
    print("bikes in olin: ",bikeshare.olin)
    print("bikes in wellesley: ",bikeshare.wellesley)
    print("bikes in downtown: ",bikeshare.downtown)


run_simulation(0.3,0.2,60)


# %%
