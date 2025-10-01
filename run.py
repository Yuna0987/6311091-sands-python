from signals import generate_sine_wave


frequency = 5      
duration = 2       
sample_rate = 100  


wave = generate_sine_wave(frequency, duration, sample_rate)


print("First 10 samples:", wave[:10])
