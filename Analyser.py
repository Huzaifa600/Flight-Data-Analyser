import matplotlib.pyplot as plt

# Open the text file and read all lines
with open("flight_data.txt", "r") as file:
    lines = file.readlines()

# The first line is the header (column names)
header = lines[0].strip().split()

# The rest are data lines
lines = lines[1:]

# Create empty lists to store the data
time = []
altitude = []
speed = []
temperature = []

# Loop through each line in the file, remove spaces and split the numbers
for line in lines:
    parts = line.strip().split()
    # Convert each value from text to float (decimal number)
    t = float(parts[0])   # time
    a = float(parts[1])   # altitude
    s = float(parts[2])   # speed
    temp = float(parts[3])  # temperature
    
    # Add values to their corresponding lists
    time.append(t)
    altitude.append(a)
    speed.append(s)
    temperature.append(temp)

# Calculate averages
avg_speed = sum(speed) / len(speed)
avg_altitude = sum(altitude) / len(altitude)

# Find maximum and minimum values
max_speed = max(speed)
min_speed = min(speed)

max_altitude = max(altitude)
min_altitude = min(altitude)

# Print out all results
print("=== Flight Summary ===")
print(f"Average Speed: {avg_speed:.1f} km/h")
print(f"Max Speed: {max_speed} km/h")
print(f"Min Speed: {min_speed} km/h\n")

print(f"Average Altitude: {avg_altitude:.1f} m")
print(f"Max Altitude: {max_altitude} m")
print(f"Min Altitude: {min_altitude} m\n")

# If speed is 15% above the averageit will be called an anomaly
threshold = avg_speed * 1.15

anomalies = []

# Loop through all speeds and check if they are above threshold
for i in range(len(speed)):
    if speed[i] > threshold:
        anomalies.append((time[i], speed[i]))

# Print anomalies if found
if len(anomalies) > 0:
    print("=== Speed Anomalies Detected ===")
    for t, s in anomalies:
        print(f"Time {t} min — Speed {s} km/h")
else:
    print("No anomalies detected.")

# Plot altitude and speed graphs

plt.figure(figsize=(10, 6))  # make the window bigger

# Altitude Plot
plt.subplot(2, 1, 1)  # 2 rows, 1 column, first plot
plt.plot(time, altitude, marker='o', color='blue', linewidth=2)
plt.title("Altitude Over Time")
plt.xlabel("Time (min)")
plt.ylabel("Altitude (m)")
plt.grid(True)  # adds background grid lines

# Speed Plot
plt.subplot(2, 1, 2)  # second plot
plt.plot(time, speed, marker='o', color='red', linewidth=2)
plt.title("Speed Over Time")
plt.xlabel("Time (min)")
plt.ylabel("Speed (km/h)")
plt.grid(True)

# Highlight anomalies on the speed plot with arrows
for t, s in anomalies:
    plt.annotate("Anomaly", xy=(t, s), xytext=(t, s + 10),
                 arrowprops=dict(facecolor="black", arrowstyle="->"),
                 fontsize=9)

# Adjust spacing so titles don't overlap
plt.tight_layout()

plt.show()
