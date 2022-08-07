from ocp.api.base import OcpBase

class v1_PackageManifest(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "packages.operators.coreos.com/v1", "PackageManifest")
    
