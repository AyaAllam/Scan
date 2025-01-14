# Python program for Scan disk scheduling algorithm

disk_size = 200

def SCAN(arr, head, size, direction):

    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []
    seek_sequence.append(head)

	# Appending end values
	# which has to be visited
	# before reversing the direction
    if (direction == "left"):
        left.append(0)
    elif (direction == "right"):
        right.append(disk_size - 1)

    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])

	# Sorting left and right vectors
    left.sort()
    right.sort()

	# Run the while loop two times.
	# one by one scanning right
	# and left of the head
    run = 2
    while (run != 0):
        if (direction == "left"):
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]

				# Appending current track to
				# seek sequence
                seek_sequence.append(cur_track)

				# Calculate absolute distance
                distance = abs(cur_track - head)

				# Increase the total count
                seek_count += distance

				# Accessed track is now the new head
                head = cur_track
			
            direction = "right"
	
        elif (direction == "right"):
            for i in range(len(right)):
                cur_track = right[i]
				
				# Appending current track to seek
				# sequence
                seek_sequence.append(cur_track)

				# Calculate absolute distance
                distance = abs(cur_track - head)

				# Increase the total count
                seek_count += distance

				# Accessed track is now new head
                head = cur_track
			
            direction = "left"
		
        run -= 1

    print("Total number of seek tracks =",
		seek_count)

    print("Seek Sequence : ")

    for i in range(len(seek_sequence)):
        print(seek_sequence[i])

    # calculate the average
    average = seek_count / size;
    print("Average number of tracks travelled = ", average)

# Driver code
if __name__ == '__main__':
    
    # to get the initial head position
    head=int(input("Initial head position: "))
    
    # to get the size of the array
    size= int(input("Number of pathes: "))
    
	# request array
    print("Sequence: ")
    arr= []
    for i in range(size):
        arr.append(int(input()))
        
    # request the direction( left or right)
    direction = input("Direction : ")

    SCAN(arr, head, size, direction)

