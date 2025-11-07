# AESB2122 — Signals and Systems Python Project  
**Student Number:** 6311091  
**Name:** XUNYUN KANG 
**Course:** Applied Earth Sciences — Signals And Systems Python Assignment  

---

###  Theory Behind the Code

This project demonstrates basic continuous-time signal generation and transformations, implemented in Python and visualized using Matplotlib.

### Signal Generation
A continuous-time signal is represented in discrete form using a sampling frequency `fs`:

\[
x[n] = x(nT_s) \quad \text{where} \quad T_s = \frac{1}{f_s}
\]

Implemented signals:
- **Sinusoidal signal**:  
  \[
  x(t) = A \sin(2\pi f t + \phi)
  \]
- **Unit step**:  
  \[
  u(t-t_0) =
  \begin{cases}
  0, & t < t_0 \\\\
  1, & t \ge t_0
  \end{cases}
  \]
- **Unit impulse** (discrete): one sample with amplitude 1 at a chosen time index.

### Signal Operations
- **Time shifting:** moves the signal along the time axis  
  \[
  y(t) = x(t - \tau)
  \]
  Positive τ = delay; negative τ = advance.
- **Time scaling:** stretches or compresses the signal  
  \[
  y(t) = x(a t)
  \]
  If `a > 1`, the signal compresses (faster); if `a < 1`, it stretches (slower).

Additional operations such as **addition** and **multiplication** are demonstrated in `script.py`.

---

### Implementation Details

### Files
| File | Description |
|------|--------------|
| `signals.py` | Contains functions to generate and transform signals. |
| `script.py` | Imports these functions, executes them with parameters, and plots/saves the results. |
| `test_signals.py` | Contains automated tests to verify correctness. |
| `pyproject.toml` | Project metadata and dependencies. |
| `README.md` | Documentation (this file). |

### Functions in `signals.py`
- `sinusoid(duration, fs, freq, amplitude, phase, offset)`  
- `unit_step(duration, fs, t0, amplitude, offset)`  
- `unit_impulse(duration, fs, t0, amplitude, offset)`  
- `time_shift(t, x, tau)`  
- `time_scale(t, x, a)`

Each function returns a **time vector (`t`)** and **signal array (`x`)**.

### Plotting
Plots are generated using `matplotlib.pyplot`.  
The final plot shows:
- Original sinusoid  
- Time-shifted and time-scaled versions  
- Unit step  
- Combined signal (sinusoid + step)  

All figures are saved automatically in the `outputs/` folder as `.png` files.

---

### Testing

Testing ensures that signal functions behave as expected.

Tests are located in `test_signals.py`.  
They verify:
- Correct signal shape and amplitude (`test_sinusoid_shape`)
- Proper step behavior (`test_unit_step_behavior`)
- Time-shift and time-scale transformations

Run all tests with:
```bash
pytest test_signals.py
