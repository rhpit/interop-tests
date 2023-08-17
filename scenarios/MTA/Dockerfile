FROM registry.access.redhat.com/ubi8/ubi:8.4

LABEL vendor="Red Hat inc."
LABEL maintainer="CSPI QE Team"
USER root

RUN set -x && \
    yum -y update && \
    INSTALL_PKGS="git gcc bind-utils iputils openssh-clients python3 python3-pip vim libselinux-python3 podman" && \
    yum install -y $INSTALL_PKGS && \
    INSTALL_PIP_PKGS="pytest kubernetes cryptography==3.3.1 pyopenssl<=22.0.0 openstacksdk>=0.36,<0.99.0" \
    /usr/bin/pip3 install $INSTALL_PIP_PKGS && \
    yum clean all -y && \
    rm -rf /var/cache/yum /var/tmp/* /tmp/*

RUN cd /tmp && curl -O https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz && \
    tar xvzf /tmp/oc.tar.gz && \
    cp /tmp/oc /usr/local/bin/ && \
    oc create namespace mta

