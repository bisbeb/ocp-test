from ocp.api.base import OcpBase

class v1_MachineConfig(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "machineconfiguration.openshift.io/v1", "MachineConfig")
    
