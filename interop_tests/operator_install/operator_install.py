import kubernetes
import logging
import sys

from typing import List
from typing import TypedDict

from openshift.dynamic import DynamicClient
from ocp_resources.namespace import Namespace
from ocp_resources.subscription import Subscription
from ocp_resources.package_manifest import PackageManifest
from ocp_resources.operator_group import OperatorGroup
from ocp_resources.operator_hub import OperatorHub
from ocp_resources.custom_resource_definition import CustomResourceDefinition

LOGGER = logging.getLogger(__name__)

operator_name = sys.argv[1]
namespace = sys.argv[2]
channel = sys.argv[3]
source = sys.argv[4]
source_namespace = sys.argv[5]

client = DynamicClient(client=kubernetes.config.new_client_from_config())

package = PackageManifest(name=any, namespace=any)

list = []
for i in package.get():
    list.append(i.name)
try:
    assert operator_name in list, 'Operator not in Package Manifest'
except AssertionError as msg:
    LOGGER.error(msg)

try:
    ns = Namespace(name="open-cluster-management")
    ns.create()
except Exception as e:
    LOGGER.info("namespace exists")

try:
    og = OperatorGroup(
        name=f"{namespace}-og",
        namespace=namespace,
        target_namespaces=[f"{namespace}"])
    og.create()
except Exception as e:
    LOGGER.info("operatorgroup exists")

try:
    sub = Subscription(
        name=operator_name,
        namespace=namespace,
        source_namespace=source_namespace,
        source=source,
        channel=channel)
    sub.create()
except:
    LOGGER.info("subscription exists")