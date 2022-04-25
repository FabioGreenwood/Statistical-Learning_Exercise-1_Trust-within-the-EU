import pandas as pd
#import datetime
#from datetime import now 


def fg_counter(counter_value, total_iterations_qty, start_time, number_of_updates_required_for_total_run = 10, update_counter = False):
    if float(counter_value) % int(total_iterations_qty / number_of_updates_required_for_total_run) == 0:
        print("-----")
        print(datetime.now())
        PC = float(float(counter_value) / total_iterations_qty)
        print(str(counter_value) + " / " + str(total_iterations_qty))
        print(PC)
        if not start_time == None:
            print("end estimate @: " + str((datetime.now() - start_time) * (total_iterations_qty / counter_value) + datetime.now()))
        if update_counter == True:
            return PC
        
        

def transfer_columns(new_df, original_df, target_string, target_string_at_start=True):
    #this method scans every column header of original_df and if target_string is contained within a header, at column is added to new df.
    #this allows me to iterativelly add groups of columns from the original datarame to the reduced datafrom for the analysis
    #target string must be entered as a string
    columns = original_df.columns
    for string_ in target_string:
        for col in columns:
            if col.find(string_) >= 0 and target_string_at_start==False: 
                new_df = pd.concat([new_df, original_df[col]], axis=1)
            if col.find(string_) == 0 and target_string_at_start==True:
                new_df = pd.concat([new_df, original_df[col]], axis=1)
        
    return new_df