# 1. Install Required Packages

Install TurtleBot3 packages:

```bash
sudo apt update
sudo apt install ros-noetic-turtlebot3*
```

---

# 2. Clone or Download the Repository

## Option A — Clone with Git

```bash
cd ~/catkin_ws/src
git clone https://github.com/Fareed-a11y/tb3-control.git
```

## Option B — Download ZIP

1. Download ZIP from GitHub
2. Extract folder
3. Move folder into:

```bash
~/catkin_ws/src/
```

---

# 3. Build the Workspace

Open a terminal:

```bash
cd ~/catkin_ws
catkin_make
```

After building:

```bash
source devel/setup.bash
```

---

# 4. Running TurtleBot3 Gazebo

You must use multiple terminals.

---

# Terminal 1 — Start ROS Master

```bash
roscore
```

Leave this terminal running.

---

# Terminal 2 — Launch Gazebo

Source ROS:

```bash
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash
```

Set TurtleBot3 model:

```bash
export TURTLEBOT3_MODEL=burger
```

Launch Gazebo:

```bash
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

Wait until Gazebo fully loads.

---

# Terminal 3 — Run Control Scripts

Open another terminal:

```bash
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash
```

---

# 5. Running the Scripts

## Keyboard Controller

Run:

```bash
rosrun tb3_control keyboard_control.py
```

Available commands:

```text
move   -> move forward
back   -> move backward
left   -> rotate left
right  -> rotate right
stop   -> stop robot
exit   -> quit program
```

Example:

```text
Enter command: move
```

---


## Move and Rotate Script

Run:

```bash
rosrun tb3_control move_rotate.py
```

This script:

* moves forward
* stops
* rotates

---

# 6. Useful ROS Commands

## View ROS topics

```bash
rostopic list
```

---

## View velocity commands

```bash
rostopic echo /cmd_vel
```

---

## Check running nodes

```bash
rosnode list
```

---

# 7. Common Errors

## "Connection refused"

Usually means:

* `roscore` is not running
* Gazebo was closed improperly

Fix:

```bash
killall -9 rosmaster roslaunch gzserver gzclient
```

Then restart from Terminal 1.

---

# 8. Package Structure

```text
tb3_control/
├── scripts/
│   ├── move_rotate.py
│   └── keyboard_control.py
├── CMakeLists.txt
├── package.xml
├── .gitignore
└── README.md
```

---

# Author

Fareed-a11y
