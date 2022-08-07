from ocp.api.base import OcpBase

class v1_CSINode(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "storage.k8s.io/v1", "CSINode")
    
