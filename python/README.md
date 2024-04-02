## 🕹 Running the Python Scripts

First,
- Make sure you have the *.py files downloaded;
- Make sure you have the odom.txt file downloaded, or your own [Odom](https://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html) data file;
- Name the input file correctly.

To run the time-evaluation script, running transactions with the ROS data, use:

```bash
$python3 time-evaluation.py
```

An output file should be created and named out_times.txt.

To plot a box-plot and also get data metrics, run:

```bash
$python3 plot-time-evaluation.py
```

A box-plot named odom-box-plot.png and an output file out_time_data.txt will be created. 
