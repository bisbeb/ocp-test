from ocp.api.base import OcpBase

class v1_PersistentVolume(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "v1", "PersistentVolume")
    
