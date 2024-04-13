times = [0]

for i in range(3000):
    times.append(times[i-1] + 0.07)
    
total = sum(times)

print(f"{total} seconds")

print(f"{total/60} minutes")

print(f"{total/(60*60)} hours")
print(f"{total/(60*60*24)} days")