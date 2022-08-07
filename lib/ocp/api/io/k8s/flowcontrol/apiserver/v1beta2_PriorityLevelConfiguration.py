from ocp.api.base import OcpBase

class v1beta2_PriorityLevelConfiguration(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "flowcontrol.apiserver.k8s.io/v1beta2", "PriorityLevelConfiguration")
    
