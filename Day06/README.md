In our lab, we utilize drones equipped with sensors to monitor atmospheric variables, aerosol concentrations, and pollutants.
These sensors measure continuously, but the detection follows a "steps" method- The drone ascends to a specific altitude,
stays there for a few minutes to collect data, and then moves to the next step.
As a result, we only use the data collected during these constant altitude periods and discard the transitional data between steps.

The provided script processes a CSV file containing these drone measurements. It includes two main functions:
1. csv_to_df: Converts the CSV file into a pandas DataFrame.
2. drop_high_var_idxs: Removes rows where the variance of a specified column within a sliding window exceeds a threshold.
   This high variance typically indicates the drone is in a vertical transition phase, not at a constant altitude.
The main function manages command-line arguments and coordinates the script's execution.
