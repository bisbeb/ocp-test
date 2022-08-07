from ocp.api.base import OcpBase

class v1_ImagePruner(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "imageregistry.operator.openshift.io/v1", "ImagePruner")
    
