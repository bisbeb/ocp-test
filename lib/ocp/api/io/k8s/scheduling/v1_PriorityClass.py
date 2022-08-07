from ocp.api.base import OcpBase

class v1_PriorityClass(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "scheduling.k8s.io/v1", "PriorityClass")
    
