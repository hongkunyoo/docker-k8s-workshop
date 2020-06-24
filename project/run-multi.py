import os
import yaml

######################
# kubectl apply -f -
######################
def kubectl_apply(job_yaml):
    cmd = """cat << EOF | kubectl apply -f -
%s
EOF
""" % job_yaml

    os.system(cmd)


with open('experiments.yaml') as f:
    experiments = yaml.load(f)

with open('job.yaml') as f:
    JOB_TEMPLATE = f.read()

for exp in experiments:
    for idx, arg in enumerate(exp['args']):
        ########################
        # WRITE YOUR CODE HERE
        #>>>>>>>>>>>>>>>>>>>>>>>



        #<<<<<<<<<<<<<<<<<<<<<<<
        kubectl_apply(JOB_TEMPLATE)
        count += 1