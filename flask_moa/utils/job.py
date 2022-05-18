import json
from tkinter import W
import pandas as pd
import numpy as np
import collections
from logics import topological_sort
SAMPLE_JOB = {
    "job_id": 3,
    "job_name": "Job3",
    "task_list":
    {
        "read": ["drop"],
        "drop": ["write"],
        "write": []
    },
    "property":
    {
        "read":
        {
            "task_name": "read",
            "filename": "a.csv",
            "sep": ","
        },
        "drop":
        {
            "task_name": "drop",
            "column_name": "date"
        },
        "write":
        {
            "task_name": "write",
            "filename": "b.csv",
            "sep": ","
        }
    }
}


class JsonCrudExcuter:
    FILE_PATH = './../data/job.json'
    def _read_all_job(self, id = None):
        with open(self.FILE_PATH,'r') as file:
            job_list = json.load(file)
            if id:
                for job in job_list:
                    if int(job['job_id']) == int(id):
                        return job
            else:
                return job_list
        if id:
            raise Exception(f'404 : there is nop id [{id}]')
    
    def _read_job(self,id):
        return self._read_all_job(id)
    
    def _write_to_json(self, job):
        with open(self.FILE_PATH, 'w') as file:
            json.dump(job, file)

    def _get_index(self, job_list, id):
        for idx, job in enumerate(job_list):
            if int(job['job_id']) == int(id):
                return idx

        raise Exception(f'404 : There is no Job id [{id}]')

    def create(self, input_job):
        job_list = self._read_all_job()
        job_list.append(input_job)

        self._write_to_json(job_list)

    def edit(self, id, input_job):
        job_list = self._read_all_job()
        job_index = self._get_index(job_list, id)
        job_list.insert(job_index, input_job)

        self._write_to_json(job_list)

    def delete(self, id):
        job_list = self._read_all_job()
        job_index = self._get_index(job_list, id)

        job_list.pop(job_index)

        self._write_to_json(job_list)
    
    def run(self, id):
        job = self._read_all_job(id)
        task_list = job['task_list']
        props = job['property']
        execurtor = CsvExecute(props,task_list)
        return execurtor.run()
    
class CsvExecute():

    def __init__(self, props, task_list):
        self.property = props
        self.task_list = topological_sort(task_list)
        self.df = pd.DataFrame()

    def _read_(self, prop):
        if self.df.empty:
            self.df = pd.read_csv(prop['filename'], sep = prop['sep'])
        else:
            new_df = pd.read_csv(prop['filename'], sep = prop['sep'])
            self.df = pd.concat([self.df,new_df],axis=1, join='outer')

    def _drop_(self, prob):
        self.df.drop([prob['column_name']],axis=1,inplace=True)

    def _write_(self,prob):
        self.df.to_csv(prob['filename'], sep=prob['sep'], mode='a')

    def run(self):
        for task in self.task_list:
            prop = self.property[task]
            if prop['task_name'] == 'read':
                res = self._read_(prop)
            if prop['task_name'] == 'drop':
                res = self._drop_(prop)
            if prop['task_name'] == 'write':
                res = self._write_(prop)
        return 
    # Job Task excute functions

