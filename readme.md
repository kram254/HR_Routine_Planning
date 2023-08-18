# Workforce Scheduling Project

## Table of Contents
Overview
Features
Dependencies
Usage
Code Structure
Conclusion
License
Contribution
Support

#### Overview
The Workforce Scheduling project aims to provide an optimized routine for managing employee shifts, ensuring that the minimum number of temporary workers are needed to cover the weekly workload. It incorporates a linear programming approach to model and solve the problem, taking into consideration the demand and available workforce, and constraints related to days off and shifts.

#### Features
```Demand Visualization:``` Graphical representation of workforce resources demand by day of the week.
```Optimization of Staff Scheduling:``` Minimize the number of staff required to meet the demand through linear programming.
```Shift Planning:``` Provides an optimal schedule, detailing the number of employees required for each shift, respecting constraints.
```Supply vs. Demand Analysis:``` Plots a bar graph to show the staff supply versus demand, including extra resources.
```Schedule Visualization:``` Generates an image of the optimized schedule as a colored table, clearly explaining the output.

### Dependencies
```pandas:``` Data manipulation and analysis.
```PuLP:``` Linear programming optimization.
```matplotlib:``` Visualization and plotting.


You can install these packages using the following command:

```
pip install pandas pulp 
```

### Usage
**Configuration:** Modify the n_staff variable to reflect the number of staff required for each day of the week.
**Run the script:** Execute the script in your Python environment.

**View the results:**
Graphical representations will be shown in separate windows.
The optimized schedule will be printed in the console.
An image (schedule.png) representing the optimized schedule will be saved in the working directory.
A CSV file (workers.csv) containing the staff supply vs demand data will also be saved in the working directory.

#### Code Structure
**ncycles:** A utility function to repeat the sequence elements n times.
**visualize_staff_demand:** Function to visualize staff demand using a bar chart.
**optimize_staff_scheduling:** Function that handles the linear programming to minimize staffing.
**print_schedule_image:** Function to print the optimized schedule onto an image.
**main:** The main function that calls the other functions in sequence and holds the main logic of the script.

### Conclusion
The Workforce Scheduling Project is a valuable tool for HR departments and managers who need to optimize staff scheduling. By leveraging linear programming and providing clear visualizations, it brings efficiency and clarity to the process of workforce planning.

### License
Please ensure that you understand the licensing requirements for your use case, particularly if you intend to use or modify this code in a commercial context.

### Contribution
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

### Support
For support and more information, you can contact the project team at markorlando45@email.com.
