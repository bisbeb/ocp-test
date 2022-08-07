from ocp.api.base import OcpBase

class v1_ConsoleNotification(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "console.openshift.io/v1", "ConsoleNotification")
    
