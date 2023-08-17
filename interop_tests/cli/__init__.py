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
"""Module building interop_tests cli."""
import click

from interop_tests.cli.orchestrate import orchestrate_cli


@click.group()
@click.pass_context
def cli(ctx: click.Option) -> None:
    """CSPI tooling

    Provides programs to be used directly for interop testing.
    """
    pass


cli.add_command(orchestrate_cli)
