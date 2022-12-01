import kubernetes
import logging
import sys

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from openshift.dynamic import DynamicClient
from ocp_resources.namespace import Namespace
from ocp_resources.subscription import Subscription
from ocp_resources.package_manifest import PackageManifest
from ocp_resources.operator_group import OperatorGroup
from ocp_resources.operator_hub import OperatorHub
from ocp_resources.custom_resource_definition import CustomResourceDefinition

logger = logging.getLogger(__name__)


class OrchestrateOperatorInstall:
    """Class representing..."""

    def __init__(self):
        """Constructs dynamic client object.

        """
        self.client = DynamicClient(client=kubernetes.config.new_client_from_config())

    def check_package_manifest(self):
        """Checks to make sure the operator can be found in PM
        """
        package = PackageManifest(name=any, namespace=any)

        list = []
        for i in package.get():
            list.append(i.name)
        try:
            assert operator_name in list, 'Operator not in Package Manifest'
        except AssertionError as msg:
            logger.error(msg)

    def create_namespace(self, namespace):
        """Creates namespace
        """

        try:
            ns = Namespace(name=namespace)
            ns.create()
        except Exception as e:
            LOGGER.info("namespace exists")

    def create_operator_group(self):
        """Creates operator group
        """

        try:
            og = OperatorGroup(
                name=f"{namespace}-og",
                namespace=namespace,
                target_namespaces=[f"{namespace}"])
            og.create()
        except Exception as e:
            logger.info("operatorgroup exists")

    def create_subscroption(self):
        """Creates namespace
        """
        try:
            sub = Subscription(
                name=operator_name,
                namespace=namespace,
                source_namespace=source_namespace,
                source=source,
                channel=channel)
            sub.create()
        except:
            logger.info("subscription exists")