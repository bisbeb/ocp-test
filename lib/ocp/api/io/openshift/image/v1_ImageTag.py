from ocp.api.base import OcpBase

class v1_ImageTag(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "image.openshift.io/v1", "ImageTag")
    
