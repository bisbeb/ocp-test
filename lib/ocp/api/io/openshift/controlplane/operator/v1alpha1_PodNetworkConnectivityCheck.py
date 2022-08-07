from ocp.api.base import OcpBase

class v1alpha1_PodNetworkConnectivityCheck(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "controlplane.operator.openshift.io/v1alpha1", "PodNetworkConnectivityCheck")
    
