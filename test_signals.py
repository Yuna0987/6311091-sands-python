"""
test_signals.py — basic tests for signals.py
"""

from signals import sinusoid, unit_step, time_shift, time_scale
import numpy as np

def test_sinusoid_shape():
    t, x = sinusoid(duration=1.0, fs=1000, freq=5)
    assert len(t) == len(x), "Time and signal lengths should match"
    assert np.isclose(np.max(x), 1.0, atol=0.1), "Amplitude should be ~1"

def test_unit_step_behavior():
    t, x = unit_step(duration=1.0, fs=1000, t0=0.5)
    assert np.all(x[t < 0.5] == 0.0), "Before step: should be 0"
    assert np.all(x[t >= 0.5] == 1.0), "After step: should be 1"

def test_time_shift_delays_signal():
    t, x = sinusoid(duration=1.0, fs=1000, freq=5)
    _, y = time_shift(t, x, tau=0.1)
    assert not np.allclose(x, y), "Shifted signal must differ from original"

def test_time_scale_changes_speed():
    t, x = sinusoid(duration=1.0, fs=1000, freq=5)
    _, y = time_scale(t, x, a=2.0)
    # scaled signal should have more cycles in same duration
    zero_cross_x = np.where(np.diff(np.sign(x)))[0]
    zero_cross_y = np.where(np.diff(np.sign(y)))[0]
    assert len(zero_cross_y) > len(zero_cross_x), "Scaled signal should oscillate faster"
