
from signals import sinusoid, unit_step, time_shift, time_scale
import matplotlib.pyplot as plt
import numpy as np
import os


fs = 1000         
duration = 2.0    
freq = 5         
shift = 0.3      
scale = 1.5       
out_dir = "outputs"


os.makedirs(out_dir, exist_ok=True)


t, x = sinusoid(duration, fs, freq, amplitude=1.0)
t, step = unit_step(duration, fs, t0=1.0)


_, x_shifted = time_shift(t, x, tau=shift)
_, x_scaled = time_scale(t, x, a=scale)
x_sum = x + step  

plt.figure(figsize=(8, 5))
plt.plot(t, x, label="Original sinusoid", linewidth=2)
plt.plot(t, x_shifted, "--", label=f"Shifted by {shift}s", alpha=0.8)
plt.plot(t, x_scaled, ":", label=f"Scaled (×{scale})", alpha=0.8)
plt.plot(t, x_sum, label="Sinusoid + Step", color="magenta", linewidth=2)
plt.plot(t, step, color="orange", label="Unit Step", linewidth=1.5)

plt.title("Signal Transformations", fontsize=12)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()


save_path = os.path.join(out_dir, "signal_transformations.png")
plt.savefig(save_path, dpi=200)
plt.show()

print(r"✅ Plot saved to: C:\Users\86150\Downloads\6311091-sands-python")
