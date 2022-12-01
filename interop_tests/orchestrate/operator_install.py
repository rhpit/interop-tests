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
import kubernetes
import logging
import sys

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from openshift.dynamic import DynamicClient
from openshift.dynamic.exceptions import NotFoundError
from ocp_resources.namespace import Namespace
from ocp_resources.subscription import Subscription
from ocp_resources.package_manifest import PackageManifest
from ocp_resources.operator_group import OperatorGroup
from ocp_resources.subscription import Subscription

logger = logging.getLogger(__name__)


class OrchestrateOperatorInstall:
    """Class representing..."""

    def __init__(self, operator_name, namespace, source_namespace, source, channel):
        """Constructs dynamic client object.

        """
        self.client = DynamicClient(client=kubernetes.config.new_client_from_config())
        self.operator_name = operator_name
        self.namespace = namespace
        self.source_namespace = source_namespace
        self.source = source
        self.channel = channel

    def check_package_manifest(self):
        """Checks to make sure the operator can be found in PM
        """
        try:
            package = PackageManifest(name=any, namespace=any)
            list = []
            for i in package.get():
                list.append(i.name)
            assert self.operator_name in list, 'Operator not in Package Manifest'
        except AssertionError as msg:
            logger.error(msg)

    def check_subscription(self):
        """Checks to make sure subscription exists
        """
        try:
            sub = Subscription.get(name=self.operator_name, namespace=self.namespace)
        except NotFoundError:
            logger.info(sub)


    def create_namespace(self):
        """Creates namespace
        """

        try:
            ns = Namespace(name=self.namespace)
            ns.create()
        except Exception as e:
            logger.info("namespace exists")

    def create_operator_group(self):
        """Creates operator group
        """

        try:
            og = OperatorGroup(
                name=f"{self.namespace}-og",
                namespace=self.namespace,
                target_namespaces=[f"{self.namespace}"])
            og.create()
        except Exception as e:
            logger.info("operatorgroup exists")

    def create_subscription(self):
        """Creates namespace
        """
        try:
            sub = Subscription(
                name=self.operator_name,
                namespace=self.namespace,
                source_namespace=self.source_namespace,
                source=self.source,
                channel=self.channel)
            sub.create()
        except:
            logger.info("subscription exists")