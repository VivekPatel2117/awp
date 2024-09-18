# Shortest job first 
# Jiska buurst time sabse kaam hoga voh phele execute hoga 
n = int(input("Enter number of processes: "))
processes = []

# Taking burst times and priorities as input
for i in range(n):
    burst = int(input(f"Enter burst time for process {i + 1}: "))
    processes.append(burst)

# Sort processes by priority (lower number has higher priority)
processes.sort()  # Sort by priority

# Initialize times
wait_time = 0
total_wait = 0
total_turnaround = 0

# Display header
print("\nProcess\tBurst Time\tWait Time\tTurnaround Time")

# Calculate wait and turnaround times
for i in range(n):
    burst = processes[i]
    print(f"{burst}\t\t{wait_time}\t\t{wait_time + burst}")
    total_wait += wait_time
    turnaround_time = wait_time + burst
    total_turnaround += turnaround_time
    wait_time += burst

# Display averages
average_wait_time = total_wait / n
average_turnaround_time = total_turnaround / n
print("Total wait",total_wait)
print(f"\nAverage Wait Time: {average_wait_time}")
print(f"Average Turnaround Time: {average_turnaround_time}")


