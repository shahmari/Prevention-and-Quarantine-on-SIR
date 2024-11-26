#!/usr/bin/env python
import subprocess
import time

runNum = 100
job=[]
for i in range(runNum):
	str = 'Ps-Pb{}.csv'.format(i)
	job.append(str)

for i in range(runNum):
	qsub_command = "qsub -v filename={} job.sh".format(job[i])
	print(qsub_command)
	exit_status = subprocess.call(qsub_command, shell=True)
	time.sleep(6)
