# First come first serve j process phele aayega voh phele execute hoga
n = int(input("Enter the number of processes: "))

# Initialize lists for process ID and burst time
burst_times = []

# Input process details
for i in range(n):
    bt = int(input(f"Enter the burst time of process {i + 1}: "))
    burst_times.append(bt)

# Calculate waiting time and total wait time
waiting_times = 0
total_wait_time = 0
print("\nProcess ID\tBurst Time\tWaiting Time")
for i in range(n):
    total_wait_time += waiting_times
    waiting_times += burst_times[i]
    print(f"{i + 1}\t\t{burst_times[i]}\t\t{waiting_times}")

# Calculate average waiting time
average_wait_time = total_wait_time / n
# Output total wait time and average wait time
print("\nTotal Waiting Time:", total_wait_time)
print("Average Waiting Time:", average_wait_time)
