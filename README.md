# Programansible

Simple class to manage Ansible within Python. Though Ansible only works on Python 2, this class will be usable on Python 3 when Ansible works on it.

The reason of using python instead of a regular ansible playbook is that at the time of writing this, there's a bug that makes imposible the normal use of `include_role` with loops. More information [here](https://github.com/ansible/ansible/issues/21285). To learn how to program a playbook in Python, read the source code and read [this article](https://serversforhackers.com/running-ansible-2-programmatically) and the Ansible's page dedicated to the [Python API](http://docs.ansible.com/ansible/dev_guide/developing_api.html#python-api-2-0).


# Installation

You can clone the repository and install from source (you should always use a virtualenv):

```bash
git clone https://git.paradigmadigital.com/ansible/programansible
cd programansible
python setup.py install
```

Or you can simply use pip:

```bash
pip install git+https://git.paradigmadigital.com/ansible/programansible/
```
