FROM python:3.10.7

# Clone interop-tests repo
RUN git clone -b operator_install https://github.com/ascerra/interop-tests.git

# Upgrade pip and install required packages
RUN pip install --upgrade pip
RUN pip install openshift-python-wrapper

# RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# RUN install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# RUN apt update
# RUN apt install vim

CMD ["/bin/bash"]