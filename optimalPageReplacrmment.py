def predict(pages, frames, index):
    """Helper function to find the optimal page to replace."""
    res = -1
    farthest = index

    for i in range(len(frames)):
        j = index
        while j < len(pages):
            if frames[i] == pages[j]:
                if j > farthest:
                    farthest = j
                    res = i
                break
            j += 1

        # If a page is never used again, return that page's index
        if j == len(pages):
            return i

    # If no page is found that won't be used in the future, return the farthest one
    return 0 if res == -1 else res


# Input for number of frames
capacity = int(input("Enter number of frames: "))

# Input for number of pages
p = int(input("Enter number of pages: "))

# Input for pages
pages = []
print("Enter page numbers:")
for _ in range(p):
    page = int(input())
    pages.append(page)

# To represent the set of current pages, we use a list
frames = []
page_faults = 0

# Loop through each page reference
for i in range(len(pages)):
    # If the page is not already in the frames
    if pages[i] not in frames:
        # If there is space in the frames
        if len(frames) < capacity:
            frames.append(pages[i])
        else:
            # Find the optimal page to replace
            j = predict(pages, frames, i + 1)
            frames[j] = pages[i]  # Replace the page

        # Page fault occurred
        page_faults += 1

    # Display current frame status after each iteration
    print("Frames:", frames)

# Output the number of page faults
print("Total number of page faults:", page_faults)
