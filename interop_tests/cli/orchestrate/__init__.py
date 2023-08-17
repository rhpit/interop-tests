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
"""Program dealing with scenario orchestration tasks."""
import click

from interop_tests.cli.orchestrate.operator_install import operator_install_cli


@click.group(name="orchestrate")
@click.pass_context
def orchestrate_cli(ctx: click.Context) -> None:
    """Collection of action to aid in Orchestration"""
    pass


orchestrate_cli.add_command(operator_install_cli)
