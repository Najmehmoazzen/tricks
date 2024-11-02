To measure the runtime of your code and save it to a ```.txt``` file, you can use Python's ```time``` module to capture the start and end times. Here’s a sample way to do it:


```python
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
