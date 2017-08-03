# -*- coding: utf-8 -*-
"""
Python object to manage Ansible within Python.
"""
# Author:: Àlex Pérez-Pujol <alexperez [ EN ] paradigmadigital.com>
# Copyright:: Copyright (c) 2017, Paradigma Digital SL
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import yaml
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory import Inventory
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.utils.display import Display
from ansible.vars import VariableManager


class Options(object):
    """
    Options class to replace Ansible OptParser
    """
    def __init__(self, verbosity=None, inventory=None, listhosts=None,
                 subset=None, module_paths=None, extra_vars=None, forks=None,
                 ask_vault_pass=None, vault_password_files=None,
                 new_vault_password_file=None, output_file=None, tags=None,
                 skip_tags=None, one_line=None, tree=None, ask_sudo_pass=None,
                 ask_su_pass=None, sudo=None, sudo_user=None, become=None,
                 become_method=None, become_user=None, become_ask_pass=None,
                 ask_pass=None, private_key_file=None, remote_user=None,
                 connection=None, timeout=None, ssh_common_args=None,
                 sftp_extra_args=None, scp_extra_args=None,
                 ssh_extra_args=None, poll_interval=None, seconds=None,
                 check=None, syntax=None, diff=None, force_handlers=None,
                 flush_cache=None, listtasks=None, listtags=None,
                 module_path=None):

        self.verbosity = verbosity
        self.inventory = inventory
        self.listhosts = listhosts
        self.subset = subset
        self.module_paths = module_paths
        self.extra_vars = extra_vars
        self.forks = forks
        self.ask_vault_pass = ask_vault_pass
        self.vault_password_files = vault_password_files
        self.new_vault_password_file = new_vault_password_file
        self.output_file = output_file
        self.tags = tags
        self.skip_tags = skip_tags
        self.one_line = one_line
        self.tree = tree
        self.ask_sudo_pass = ask_sudo_pass
        self.ask_su_pass = ask_su_pass
        self.sudo = sudo
        self.sudo_user = sudo_user
        self.become = become
        self.become_method = become_method
        self.become_user = become_user
        self.become_ask_pass = become_ask_pass
        self.ask_pass = ask_pass
        self.private_key_file = private_key_file
        self.remote_user = remote_user
        self.connection = connection
        self.timeout = timeout
        self.ssh_common_args = ssh_common_args
        self.sftp_extra_args = sftp_extra_args
        self.scp_extra_args = scp_extra_args
        self.ssh_extra_args = ssh_extra_args
        self.poll_interval = poll_interval
        self.seconds = seconds
        self.check = check
        self.syntax = syntax
        self.diff = diff
        self.force_handlers = force_handlers
        self.flush_cache = flush_cache
        self.listtasks = listtasks
        self.listtags = listtags
        self.module_path = module_path


class AnsibleProgramatic:
    """Class to make easier to execute playbooks."""
    def __init__(self, options, playbook, extra_vars=None, loader=DataLoader(),
                 password=None, variable_manager=VariableManager(),
                 verbosity=1, host_list=None, callback=None):
        """Instantiate the class."""

        # Verbosity
        display = Display()
        display.verbosity = verbosity
        # El equivalente de -e en la terminal
        self.extra_vars = extra_vars
        # Ni idea, pero es necesario
        self.loader = loader
        # Contraseña del vault, de haber
        self.passwords = password
        # Añade automaticamente las variables
        self.variable_manager = variable_manager
        # Crea un falso inventario dinámico y se lo pasa al gestor de variables
        self.inventory = Inventory(
            loader=loader,
            variable_manager=variable_manager,
            host_list=host_list)
        # Añade el inventario
        self.variable_manager.set_inventory(self.inventory)
        # Añade variables a mano
        if extra_vars is not None:
            self.variable_manager.extra_vars = extra_vars
        # Definir playbook
        self.playbook = playbook
        # Define opciones
        self.options = options
        # Define la lista de hosts
        self.host_list = host_list
        # Define callback
        self.callback = callback

    def run(self):
        """Execute the playbook."""
        # Instancia el objeto del playbook
        play = Play().load(self.playbook,
                           variable_manager=self.variable_manager,
                           loader=self.loader)
        # Añade el playbook a la cola
        tqm = TaskQueueManager(inventory=self.inventory,
                               variable_manager=self.variable_manager,
                               loader=self.loader,
                               options=self.options,
                               passwords=self.passwords,
                               stdout_callback=None
                              )
        # Ejecuta el playbook
        tqm.run(play)
        # Guarda los resultados de un modo mas accesible. Probablemente
        # mala practica, dado que accede a un metodo protegido.
        tqm = tqm._variable_manager._nonpersistent_fact_cache.items()

        return tqm

def yaml2json(stream):
    """Receive yaml and convert it into json."""

    json_data = yaml.safe_load(stream)

    return json_data
