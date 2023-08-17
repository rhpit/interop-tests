#
# Copyright (C) 2022 Red Hat, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
This module will be used to install operators.
"""
import logging

import click

from interop_tests import helper
from interop_tests.orchestrate.operator_install import OrchestrateOperatorInstall

logger = logging.getLogger(__name__)


@click.option(
    "--operator-name",
    help="Name of operator to install",
    required=True
)
@click.option(
    "--namespace",
    help="Namespace to create & use for operator install placement",
    required=True
)
@click.option(
    "--channel",
    help="Channel name to specify version of the operator to install",
    required=True
)
@click.option(
    "--source",
    help="Specify the catalog source of the operator",
    default="redhat-operators"
)
@click.option(
    "--source-namespace",
    help="Specify the catalog source namespace of the operator",
    default="openshift-marketplace"
)
@click.command("operator-install")
@click.pass_context
def operator_install_cli(
    ctx: click.Context,
    operator_name,
    namespace,
    channel,
    source,
    source_namespace,
) -> None:
    """Install operator
    \b
    Examples
      # Install operator
      $ interop-tests orchestrate operator-install --operator_name ${OPERATOR_NAME}
    """
    helper.initialize_logger(True)
    client = OrchestrateOperatorInstall()
    client.check_package_manifest()
    client.create_namespace(namespace)
    client.create_operator_group(namespace)
    client.create_subscription(operator_name, namespace, channel, source, source_namespace)
    client.check_subscription(operator_name, namespace)

