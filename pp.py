# Priority scheduling
# Jo user priority dega viasa he execute hoga process
n = int(input("Enter number of processes: "))
processes = []

# Taking burst times and priorities as input
for i in range(n):
    burst = int(input(f"Enter burst time for process {i + 1}: "))
    priority = int(input(f"Enter priority for process {i + 1}: "))
    # appending a tuple in processes list
    processes.append((burst, priority))

# Sort processes by priority (lower number has higher priority)
processes.sort(key=lambda x: x[1])  # Sort by priority

# Initialize times
wait_time = 0
total_wait = 0
total_turnaround = 0

# Display header
print("\nProcess\tBurst Time\tWait Time\tTurnaround Time")

# Calculate wait and turnaround times
for i in range(n):
    burst = processes[i][0]
    print(f"{i + 1}\t{burst}\t\t{wait_time}\t\t{wait_time + burst}")
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