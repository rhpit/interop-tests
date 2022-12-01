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
"""Helper module."""
import logging

__all__ = ["initialize_logger"]


def initialize_logger(verbose: bool) -> None:
    """Initialize logger configuration.

    :param verbose: toggles whether debug logging is enabled
    """
    log_level: int
    log_format: str

    if verbose:
        log_level = logging.DEBUG
        log_format = "%(asctime)s %(name)s.%(funcName)s:%(lineno)d : %(message)s"
    else:
        log_level = logging.INFO
        log_format = "%(asctime)s : %(message)s"

    logging.basicConfig(format=log_format, level=log_level)
