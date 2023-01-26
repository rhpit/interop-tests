FROM registry.access.redhat.com/ubi8/ubi

RUN yum install -y --nodocs jq python3-virtualenv python3-pip make git golang bc

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN ln -s /cli/oc /usr/bin/kubectl

RUN curl -Lk -o /usr/bin/yq https://github.com/mikefarah/yq/releases/download/v4.18.1/yq_linux_amd64 && chmod +x /usr/bin/yq

RUN pip3 install yamllint

CMD ["/bin/bash"]
