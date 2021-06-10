# exoedu-robot

## simulation

Build urdf model using stl files and load in the pybullet simulation.
```
python test_robot.py
```

<!-- ![](./urdf/robot.PNG)  -->
<img src="./urdf/robot.PNG" width="300" height="180">

## connect through ROS

1. launch aduino
    using arduino IDE to upload the [code](./arduino/ros_test.ino) to the arduino/ Once the compilation is completed, you will receive a message about program storage space and dynamic memory usage, similar to this:
    ```
    Sketch uses 9,392 bytes (29%) of program storage space. Maximum is 32,256 bytes. Global variables use 1,356 bytes (66%) of dynamic memory, leaving 692 bytes for local variables. Maximum is 2,048 byte
    ```

2. launch launch roscore and roserial to create publish and subscriber
    ```
    roscore
    rosrun rosserial_arduino serial_node.py /dev/ttyACM0 _baud:=57600
    python main.py
    ```
    ![](./urdf/sim_real_0.gif) 
