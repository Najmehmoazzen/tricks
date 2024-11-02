```
import time

# Start the timer
start_time = time.time()
###
###
###
# End the timer
end_time = time.time()

# Calculate runtime
runtime = end_time - start_time

# Print runtime
print(f"Runtime: {runtime:.2f} seconds")

# Write the runtime to a text file
with open("runtime.txt", "w") as file:
    file.write(f"Runtime: {runtime:.2f} seconds")

```
