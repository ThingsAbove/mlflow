from subprocess import Popen

registered_model_name = "credit_defaults_model"
inputs={
    'data':"https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls",
    'test_train_ratio':"0.2",
    'learning_rate':"0.25",
    'registered_model_name':"registered_model_name"
    }

print(f"--data \"{inputs['data']}\" --test_train_ratio {inputs['test_train_ratio']} --learning_rate {inputs['learning_rate']} --registered_model_name \"{inputs['registered_model_name']}\"")

process = Popen(f"python3 main.py --data \"{inputs['data']}\" --test_train_ratio {inputs['test_train_ratio']} --learning_rate {inputs['learning_rate']} --registered_model_name \"{inputs['registered_model_name']}\"", shell=True)
