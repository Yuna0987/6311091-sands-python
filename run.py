from signals import generate_sine_wave,generate_unit_step
imfrequency = 5      
duration = 2       
sample_rate = 100 port matlplot .pyplot as plt
wave = generate_sine_wave(frequency, duration, sample_rate)
t,y = generate_sine_wave(5,2,100)
plt.plot(t,y,label="Original sine wave")

t_shifted = t+0.5
plt.plot(t_shifted, y, label="Time shifted (+0.5s)")
t_scaled=t*0.5
plt.plot(t_scaled, y, label="Time scaled (0.5x)"
         
t2,u= generate_unit_step(2,100, step_time=1)
plt.plot(t2, u, label="Unit step (at t=1s)")
         y_sum=y+u
         plt.plot(t,y_sum, label ="sine + unit step")
         plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.titel ("Signal transformations")
plt.legend()
plt.grid(True)
plt.show()
       


 





print("First 10 samples:", wave[:10])
