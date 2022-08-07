import time

class OcpBase:
  """
  Base class for all k8s/ocp resources, it implements basic method for object:
  - get (by name or label selector)
  - create
  - delete
  """

  def __init__(self,dyn_client, api_version, kind):
    self.dyn_client = dyn_client
    self.api_version = api_version
    self.kind = kind

  def __wait(self, resource, count):
    c = 60
    while True:
      time.sleep(0.5)
      if len(resource.get(namespace=namespace, name=name).items) == count or c == 0:
        break
      c = c - 1

  def __get_resource(self):
    return self.dyn_client.resources.get(api_version=self.api_version, kind=self.kind)

  def get(self, name=None, label=None, value=None, namespace=None):
    f_args = {}
    ret = []
    resource = self.__get_resource()
    if namespace:
      f_args["namespace"] = namespace
    if name:
      f_args["field_selector"] = "metadata.name=%s" % (name)
    elif label and value:
      f_args["label_selector"] = "%s=%s" % (label, value)
    resource_list = resource.get(**f_args).items
    for item in resource_list:
      ret.append(item)
    return ret

  def create(self, body, namespace=None, wait=True):
    f_args = {}
    resource = self.__get_resource()
    f_args["body"] = body
    if namespace:
      f_args["namespace"] = namespace
    resource.create(**f_args)
    if wait:
      self.__wait(resource, 1)

  def delete(self, name, namespace=None, wait=True):
    f_args = {}
    resource = self.__get_resource()
    f_args["name"] = name
    if namepsace:
      f_args["namespace"] = namespace
    resource.delete(**f_args)
    if wait:
      self.__wait(resource, 0)

# =================================================================
# implentation for basic objects
# =================================================================

# cluster-wide resources
# ======================
class apiserver_openshift_io_v1APIRequestCount(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apiserver.openshift.io/v1", "APIRequestCount")
  
class config_openshift_io_v1APIServer(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "APIServer")
  
class apiregistration_k8s_io_v1APIService(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apiregistration.k8s.io/v1", "APIService")
  
class config_openshift_io_v1Authentication(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "Authentication")
  
class config_openshift_io_v1Build(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "Build")
  
class operator_openshift_io_v1CloudCredential(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "CloudCredential")
  
class network_openshift_io_v1ClusterNetwork(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "network.openshift.io/v1", "ClusterNetwork")
  
class config_openshift_io_v1ClusterOperator(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "ClusterOperator")
  
class authorization_openshift_io_v1ClusterRole(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "authorization.openshift.io/v1", "ClusterRole")
  
class authorization_openshift_io_v1ClusterRoleBinding(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "authorization.openshift.io/v1", "ClusterRoleBinding")
  
class rbac_authorization_k8s_io_v1ClusterRoleBinding(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "rbac.authorization.k8s.io/v1", "ClusterRoleBinding")
  
class rbac_authorization_k8s_io_v1ClusterRole(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "rbac.authorization.k8s.io/v1", "ClusterRole")
  
class config_openshift_io_v1ClusterVersion(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "ClusterVersion")
  
class imageregistry_operator_openshift_io_v1Config(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "imageregistry.operator.openshift.io/v1", "Config")
  
class console_openshift_io_v1ConsoleCLIDownload(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "console.openshift.io/v1", "ConsoleCLIDownload")
  
class config_openshift_io_v1Console(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "Console")
  
class console_openshift_io_v1ConsoleNotification(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "console.openshift.io/v1", "ConsoleNotification")
  
class machineconfiguration_openshift_io_v1ControllerConfig(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "machineconfiguration.openshift.io/v1", "ControllerConfig")
  
class storage_k8s_io_v1CSINode(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "storage.k8s.io/v1", "CSINode")
  
class operator_openshift_io_v1CSISnapshotController(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "CSISnapshotController")
  
class apiextensions_k8s_io_v1CustomResourceDefinition(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apiextensions.k8s.io/v1", "CustomResourceDefinition")
  
class config_openshift_io_v1DNS(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "DNS")
  
class operator_openshift_io_v1Etcd(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "Etcd")
  
class config_openshift_io_v1FeatureGate(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "FeatureGate")
  
class flowcontrol_apiserver_k8s_io_v1beta2FlowSchema(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "flowcontrol.apiserver.k8s.io/v1beta2", "FlowSchema")
  
class helm_openshift_io_v1beta1HelmChartRepository(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "helm.openshift.io/v1beta1", "HelmChartRepository")
  
class network_openshift_io_v1HostSubnet(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "network.openshift.io/v1", "HostSubnet")
  
class user_openshift_io_v1Identity(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "user.openshift.io/v1", "Identity")
  
class config_openshift_io_v1Image(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "Image")
  
class image_openshift_io_v1Image(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "image.openshift.io/v1", "Image")
  
class imageregistry_operator_openshift_io_v1ImagePruner(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "imageregistry.operator.openshift.io/v1", "ImagePruner")
  
class config_openshift_io_v1Infrastructure(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "Infrastructure")
  
class networking_k8s_io_v1IngressClass(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "networking.k8s.io/v1", "IngressClass")
  
class config_openshift_io_v1Ingress(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "Ingress")
  
class operator_openshift_io_v1KubeAPIServer(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "KubeAPIServer")
  
class operator_openshift_io_v1KubeControllerManager(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "KubeControllerManager")
  
class operator_openshift_io_v1KubeScheduler(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "KubeScheduler")
  
class operator_openshift_io_v1KubeStorageVersionMigrator(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "KubeStorageVersionMigrator")
  
class machineconfiguration_openshift_io_v1MachineConfig(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "machineconfiguration.openshift.io/v1", "MachineConfig")
  
class machineconfiguration_openshift_io_v1MachineConfigPool(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "machineconfiguration.openshift.io/v1", "MachineConfigPool")
  
class admissionregistration_k8s_io_v1MutatingWebhookConfiguration(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "admissionregistration.k8s.io/v1", "MutatingWebhookConfiguration")
  
class v1Namespace(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "Namespace")
  
class network_openshift_io_v1NetNamespace(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "network.openshift.io/v1", "NetNamespace")
  
class config_openshift_io_v1Network(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "Network")
  
class operator_openshift_io_v1Network(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "Network")
  
class v1Node(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "Node")
  
class oauth_openshift_io_v1OAuthAccessToken(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "oauth.openshift.io/v1", "OAuthAccessToken")
  
class oauth_openshift_io_v1OAuthClient(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "oauth.openshift.io/v1", "OAuthClient")
  
class config_openshift_io_v1OAuth(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "OAuth")
  
class operators_coreos_com_v1OLMConfig(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v1", "OLMConfig")
  
class operator_openshift_io_v1OpenShiftAPIServer(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "OpenShiftAPIServer")
  
class operator_openshift_io_v1OpenShiftControllerManager(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "OpenShiftControllerManager")
  
class config_openshift_io_v1OperatorHub(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "OperatorHub")
  
class operators_coreos_com_v1Operator(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v1", "Operator")
  
class v1PersistentVolume(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "PersistentVolume")
  
class scheduling_k8s_io_v1PriorityClass(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "scheduling.k8s.io/v1", "PriorityClass")
  
class flowcontrol_apiserver_k8s_io_v1beta2PriorityLevelConfiguration(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "flowcontrol.apiserver.k8s.io/v1beta2", "PriorityLevelConfiguration")
  
class project_openshift_io_v1Project(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "project.openshift.io/v1", "Project")
  
class config_openshift_io_v1Proxy(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "Proxy")
  
class security_internal_openshift_io_v1RangeAllocation(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "security.internal.openshift.io/v1", "RangeAllocation")
  
class config_openshift_io_v1Scheduler(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "Scheduler")
  
class security_openshift_io_v1SecurityContextConstraints(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "security.openshift.io/v1", "SecurityContextConstraints")
  
class operator_openshift_io_v1ServiceCA(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "ServiceCA")
  
class storage_k8s_io_v1StorageClass(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "storage.k8s.io/v1", "StorageClass")
  
class operator_openshift_io_v1Storage(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "Storage")
  
class migration_k8s_io_v1alpha1StorageVersionMigration(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "migration.k8s.io/v1alpha1", "StorageVersionMigration")
  
class user_openshift_io_v1User(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "user.openshift.io/v1", "User")
  
class admissionregistration_k8s_io_v1ValidatingWebhookConfiguration(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "admissionregistration.k8s.io/v1", "ValidatingWebhookConfiguration")
  
# namespaced resources
# ====================
class operators_coreos_com_v1alpha1CatalogSource(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v1alpha1", "CatalogSource")
  
class operators_coreos_com_v1alpha1ClusterServiceVersion(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v1alpha1", "ClusterServiceVersion")
  
class v1ConfigMap(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "ConfigMap")
  
class apps_v1ControllerRevision(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apps/v1", "ControllerRevision")
  
class cloudcredential_openshift_io_v1CredentialsRequest(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "cloudcredential.openshift.io/v1", "CredentialsRequest")
  
class batch_v1CronJob(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "batch/v1", "CronJob")
  
class apps_v1DaemonSet(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apps/v1", "DaemonSet")
  
class apps_v1Deployment(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apps/v1", "Deployment")
  
class discovery_k8s_io_v1EndpointSlice(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "discovery.k8s.io/v1", "EndpointSlice")
  
class v1Endpoints(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "Endpoints")
  
class v1Event(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "Event")
  
class image_openshift_io_v1ImageStream(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "image.openshift.io/v1", "ImageStream")
  
class image_openshift_io_v1ImageStreamTag(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "image.openshift.io/v1", "ImageStreamTag")
  
class image_openshift_io_v1ImageTag(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "image.openshift.io/v1", "ImageTag")
  
class operator_openshift_io_v1IngressController(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "IngressController")
  
class operators_coreos_com_v1alpha1InstallPlan(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v1alpha1", "InstallPlan")
  
class batch_v1Job(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "batch/v1", "Job")
  
class coordination_k8s_io_v1Lease(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "coordination.k8s.io/v1", "Lease")
  
class machine_openshift_io_v1beta1MachineHealthCheck(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "machine.openshift.io/v1beta1", "MachineHealthCheck")
  
class machine_openshift_io_v1beta1Machine(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "machine.openshift.io/v1beta1", "Machine")
  
class machine_openshift_io_v1beta1MachineSet(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "machine.openshift.io/v1beta1", "MachineSet")
  
class operators_coreos_com_v2OperatorCondition(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v2", "OperatorCondition")
  
class operators_coreos_com_v1OperatorGroup(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v1", "OperatorGroup")
  
class packages_operators_coreos_com_v1PackageManifest(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "packages.operators.coreos.com/v1", "PackageManifest")
  
class v1PersistentVolumeClaim(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "PersistentVolumeClaim")
  
class policy_v1PodDisruptionBudget(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "policy/v1", "PodDisruptionBudget")
  
class controlplane_operator_openshift_io_v1alpha1PodNetworkConnectivityCheck(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "controlplane.operator.openshift.io/v1alpha1", "PodNetworkConnectivityCheck")
  
class v1Pod(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "Pod")
  
class tuned_openshift_io_v1Profile(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "tuned.openshift.io/v1", "Profile")
  
class monitoring_coreos_com_v1PrometheusRule(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "monitoring.coreos.com/v1", "PrometheusRule")
  
class apps_v1ReplicaSet(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apps/v1", "ReplicaSet")
  
class v1ResourceQuota(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "ResourceQuota")
  
class authorization_openshift_io_v1Role(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "authorization.openshift.io/v1", "Role")
  
class authorization_openshift_io_v1RoleBinding(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "authorization.openshift.io/v1", "RoleBinding")
  
class rbac_authorization_k8s_io_v1RoleBinding(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "rbac.authorization.k8s.io/v1", "RoleBinding")
  
class rbac_authorization_k8s_io_v1Role(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "rbac.authorization.k8s.io/v1", "Role")
  
class route_openshift_io_v1Route(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "route.openshift.io/v1", "Route")
  
class v1Secret(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "Secret")
  
class v1ServiceAccount(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "ServiceAccount")
  
class monitoring_coreos_com_v1ServiceMonitor(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "monitoring.coreos.com/v1", "ServiceMonitor")
  
class v1Service(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "Service")
  
class operators_coreos_com_v1alpha1Subscription(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v1alpha1", "Subscription")
  
class template_openshift_io_v1Template(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "template.openshift.io/v1", "Template")
  
class tuned_openshift_io_v1Tuned(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "tuned.openshift.io/v1", "Tuned")
  
