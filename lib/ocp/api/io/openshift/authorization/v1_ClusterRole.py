from ocp.api.base import OcpBase

class v1_ClusterRole(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "authorization.openshift.io/v1", "ClusterRole")
    
