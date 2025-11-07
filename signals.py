


import numpy as np
import matplotlib.pyplot as plt




def sinusoid(duration, fs, freq, amplitude=1.0, phase=0.0, offset=0.0):
    """
    Generate a sinusoidal signal.
    Returns time vector t and signal x.
    """
    t = np.arange(0, duration, 1/fs)
    x = amplitude * np.sin(2 * np.pi * freq * t + phase) + offset
    return t, x


def unit_step(duration, fs, t0=0.0, amplitude=1.0, offset=0.0):
    """
    Generate a unit step signal (starts at t0).
    """
    t = np.arange(0, duration, 1/fs)
    x = np.where(t >= t0, amplitude, 0.0) + offset
    return t, x


def unit_impulse(duration, fs, t0=0.0, amplitude=1.0, offset=0.0):
    """
    Generate a discrete impulse (1 sample = amplitude).
    """
    t = np.arange(0, duration, 1/fs)
    x = np.zeros_like(t)
    idx = int(np.clip(round(t0 * fs), 0, len(t) - 1))
    x[idx] = amplitude
    x += offset
    return t, x




def time_shift(t, x, tau):
    """
    Shift the signal in time by tau seconds.
    Positive tau = delay (move right).
    """
    y = np.interp(t - tau, t, x, left=0.0, right=0.0)
    return t, y


def time_scale(t, x, a):
    """
    Scale the time axis by factor a.
    a > 1 compresses; a < 1 stretches.
    """
    y = np.interp(a * t, t, x, left=0.0, right=0.0)
    return t, y



def plot_signals(t, signals, labels, title="Signals"):
    """
    Quick helper to plot multiple signals.
    """
    for x, label in zip(signals, labels):
        plt.plot(t, x, label=label)
    plt.title(title)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    fs = 1000
    duration = 1.0

  
    t, x = sinusoid(duration, fs, freq=5, amplitude=1)
    
    _, x_shifted = time_shift(t, x, tau=0.1)
    _, x_scaled = time_scale(t, x, a=2.0)

    plot_signals(t, [x, x_shifted, x_scaled],
                 ["original", "shifted", "scaled"],
                 "Sinusoid with operations")




















































































