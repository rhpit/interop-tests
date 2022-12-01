FROM python:3.10.7

# Install interop-tests repo
RUN pip3 install git+https://github.com/rhpit/interop-tests.git@main

# Upgrade pip and install required packages
RUN pip install --upgrade pip
RUN pip install openshift-python-wrapper

# RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# RUN install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# RUN apt update
# RUN apt install vim

CMD ["/bin/bash"]