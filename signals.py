import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    """
    Generate a sine wave signal.

    Parameters:
        frequency (float): frequency of the sine wave in Hz
        duration (float): duration of the signal in seconds
        sample_rate (int): samples per second

    Returns:
        numpy.ndarray: array of sine wave samples
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = np.sin(2 * np.pi * frequency * t)
    return y


