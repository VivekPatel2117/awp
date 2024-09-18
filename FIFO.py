# FIFO Page Replacement Algorithm in Python

# Input the number of frames
f = int(input("Enter number of frames: "))

# Input the number of pages
p = int(input("Enter number of pages: "))

# Initialize frames and pages
frame = [-1] * f  # Set all frames initially to -1 (empty)
pages = []

# Input the pages
print("Enter page numbers:")
for i in range(p):
    page = int(input())
    pages.append(page)

# Initialize variables for page hits and faults
page_hit = 0
page_fault = 0
num = 0  # Frame index

# FIFO Page Replacement Algorithm
for page in pages:
    # Check if the page is already in one of the frames
    if page in frame:
        page_hit += 1  # Page hit, no need for replacement
    else:
        frame[num] = page  # Replace the page using FIFO
        num = (num + 1) % f  # Move to the next frame in a circular manner
        page_fault += 1

    # Display the current frame status
    print("Frame:", frame)

# Output the number of page hits and page faults
print("Number of page hits:", page_hit)
print("Number of page faults:", page_fault)
