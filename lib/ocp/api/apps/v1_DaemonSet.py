from ocp.api.base import OcpBase

class v1_DaemonSet(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apps/v1", "DaemonSet")
    
