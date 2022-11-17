# Both prepare the environment and execute tests
all:
    $(MAKE) prepare
    $(MAKE) test

# Prepare for execution by installing Python, Ansbile, and the MTA operator
prepare:
    $(MAKE) install-python
    $(MAKE) install-ansible
    $(MAKE) install-mta

# Run the tests
test:
    $(MAKE) execute-tests

# Run the mta_install playbook
install-mta: ansible-playbook ansible/mta_install.yml
# Run the mta_tests playbook
execute-tests: ansible-playbook ansible/mta_tests.yml
# Install Python
install-python: sudo yum install -y python38
#Install Ansible
install-ansible: python3 -m pip install --user ansible