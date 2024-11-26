import time
jobNumber=10
for i in range(jobNumber):
    qsub_command = "qsub job.sh"
    print(qsub_command)
    exit_status = subprocess.call(qsub_command, shell=True)
    time.sleep(6)