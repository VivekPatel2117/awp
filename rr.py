# Round robin
# Round Robin (RR): This algorithm allocates a fixed time slice (quantum) to each process in a cyclic order, ensuring all processes receive fair CPU time. It's effective for time-sharing systems but can lead to higher waiting times if the quantum is too small.
# matlab yeh hua ki yeh jo h iske quantum time tak he process ko execute hone dega ab samaj ki quantam time = 4 dala h toh 1st process 4sec fir 2nd processs 4sec aaisa krke small peices mein process ko execute krte h 
# Input number of processes
n = int(input("Enter the number of processes: "))
burst_times = []
for i in range(n):
    bt = int(input(f"Enter the burst time for process {i + 1}: "))
    burst_times.append(bt)

# Input quantum time
quantum_time = int(input("Enter the quantum time: "))

# Initialize remaining burst times, waiting times, turnaround times, and current time
remaining_times = burst_times[:]  # Copy of burst times
waiting_times = [0] * n
turnaround_times = [0] * n
current_time = 0

# Round Robin scheduling
while True:
    done = True
    for i in range(n):
        if remaining_times[i] > 0:  # If the process still has remaining time
            done = False
            if remaining_times[i] > quantum_time:
                current_time += quantum_time
                remaining_times[i] -= quantum_time
            else:
                current_time += remaining_times[i]
                turnaround_times[i] = current_time  # Turnaround time
                waiting_times[i] = turnaround_times[i] - burst_times[i]  # Waiting time
                remaining_times[i] = 0  # Process is completed
    if done:
        break

# Calculate averages
avg_waiting_time = sum(waiting_times) / n
avg_turnaround_time = sum(turnaround_times) / n

# Display results
print("\nProcess ID\tBurst Time\tWaiting Time\tTurnaround Time")
print("-------------------------------------------------------------")
for i in range(n):
    print(f"{i + 1}\t\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")

# Display average waiting time and turnaround time
print("Average Waiting Time:", avg_waiting_time)
print("Average Turnaround Time:", avg_turnaround_time)