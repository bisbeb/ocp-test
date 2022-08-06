import time

class OcpBase:
  """
  Base class for all k8s/ocp resources, it implements basic method for object:
  - get (by name or label selector)
  - create
  - delete
  """

  def __init__(self,dyn_client, api_version, kind):
    self.dyn_client = dyn_client
    self.api_version = api_version
    self.kind = kind

  def __wait(self, resource, count):
    c = 60
    while True:
      time.sleep(0.5)
      if len(resource.get(namespace=namespace, name=name).items) == count or c == 0:
        break
      c = c - 1

  def __get_resource(self):
    return self.dyn_client.resources.get(api_version=self.api_version, kind=self.kind)

  def get(self, name=None, label=None, value=None, namespace=None):
    f_args = {}
    ret = []
    resource = self.__get_resource()
    if namespace:
      f_args["namespace"] = namespace
    if name:
      f_args["field_selector"] = "metadata.name=%s" % (name)
    elif label and value:
      f_args["label_selector"] = "%s=%s" % (label, value)
    resource_list = resource.get(**f_args).items
    for item in resource_list:
      ret.append(item)
    return ret

  def create(self, body, namespace=None, wait=True):
    f_args = {}
    resource = self.__get_resource()
    f_args["body"] = body
    if namespace:
      f_args["namespace"] = namespace
    resource.create(**f_args)
    if wait:
      self.__wait(resource, 1)

  def delete(self, name, namespace=None, wait=True):
    f_args = {}
    resource = self.__get_resource()
    f_args["name"] = name
    if namepsace:
      f_args["namespace"] = namespace
    resource.delete(**f_args)
    if wait:
      self.__wait(resource, 0)

# =================================================================
# implentation for basic objects
# =================================================================
class v1ConfigMap(OcpBase):
  def __init__(self, dyn_client):
    super().__init__(dyn_client, "v1", "ConfigMap")

class v1Secret(OcpBase):
  def __init__(self, dyn_client):
    super().__init__(dyn_client, "v1", "Secret")

class v1Node(OcpBase):
  def __init__(self, dyn_client):
    super().__init__(dyn_client, "v1", "Node")

class v1Namespace(OcpBase):
  def __init__(self, dyn_client):
    super().__init__(dyn_client, "v1", "Namespace")

class apps_v1Deployment(OcpBase):
  def __init__(self, dyn_client):
    super().__init__(dyn_client, "apps/v1", "Deployment")

