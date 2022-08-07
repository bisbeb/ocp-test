from ocp.api.base import OcpBase

class v1_NetNamespace(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "network.openshift.io/v1", "NetNamespace")
    
