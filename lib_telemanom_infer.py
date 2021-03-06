""" Produces anomaly scores, by regularly asking the trained Telemanom model to infer the scores.

It runs in parallel with the lib_telemanom_train.py, to make training and inference work as separate processes.
"""

import time

from helper_funcs import append_logs, infer_and_save_results, exit7, synthetic_data7
import lib_telemanom_calc

ask_model_func = lib_telemanom_calc.ask_model

useOnlyThisManyLatestOfLastN = 100
filename2write = "risk_scores/telemanom_anomaly.txt"
name4logs = "lib_telemanom_infer"
method_name = "telemanom"

if synthetic_data7():
    output_postfix = "_synthetic"
else:
    output_postfix = "_fetched"

modelpath = "pickled_models/" + method_name + output_postfix + ".pkl"

append_logs("Starting the main circle", name4logs, "always")

old_modification_ts = -1
old_meta_model_dic = None
scales_dic = None

while True:
    exit7()
    old_modification_ts, old_meta_model_dic, scales_dic = infer_and_save_results(ask_model_func, modelpath,
                                                                                 old_modification_ts,
                                                                                 old_meta_model_dic,
                                                                                 useOnlyThisManyLatestOfLastN,
                                                                                 method_name, scales_dic)
    time.sleep(1.0)
