import numpy as np

def generate_sine_wave(frequency, duration, sample_rate, amplitude=1.0,phase=0):
    ```
  Generate a sine wave signal.

    Parameters:
        frequency (float): frequency of the sine wave in Hz
        duration (float): duration of the signal in seconds
        sample_rate (int): samples per second
        amplitude(float): Amplitude of the sine wave. Default is 1.0
        phase (float):Phase shift in radinas. Default is 0.
        Returns:
         numpy.ndarray: array of sine wave samples
        t=Time values 
        y=Signal values 
     ```
    
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = np.sin(2 * np.pi * frequency * t+ phase)
    return t,y
def generate_unit_step(duration, sample_rate,step_time=0):
    Generate a unit stp signal 
    Parameters
    duration(float):Duration of the signal in seconds. 
        sample_rate: Sampling rate in HZ.
            step_time(float): Time at which step occurs. Default is 0
                return:
 t= Time values
 y= Signal values.
    ````
    t=np.linspace (0, duration, int(sample_rate * duration), endpoint = False)
    y=[]
    for ti in t
    if ti>= step_time:
        y.append(1.0)
        else:
        y.append(0.0)
        y=np.array(y)
        return t,y
