from numpy import True_
import yaml
import os
import json


#send config file and it ll return as dictionary

#loads the yaml file

def read_yaml(path_to_yaml: str)-> dict:  #gets an input as str and return dict
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)


    return content  

#creating a function for (Creating a dir)

def create_directory(dirs:list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)
        print(f"dir is placed at {dir_path}")


#method to save df locally
def save_local_df(data,data_path,index =False):
    data.to_csv(data_path,index= index)  
    print(f"data is saved at {data_path}")    

#saving model metrics in json
def save_reports(report : dict ,report_path : str): #acceptig reports as dict amd report_path as str
    with open(report_path,"w") as f:
        json.dump(report,f,indent =4)
    print(f"Reports are saved at {report_path}")    
      





