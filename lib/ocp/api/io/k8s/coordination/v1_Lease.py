from ocp.api.base import OcpBase

class v1_Lease(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "coordination.k8s.io/v1", "Lease")
    
