import httplib
import json
from urllib import quote

class GoldWrap:
  
  _headers = { 'Accept': 'application/json' }

  def __init__(self, protocol, host, port, basepath, timeout):
    self._protocol = protocol
    self._host = host
    self._port = port
    self._basepath = basepath
    self._timeout = timeout
    
  def get_project_by_title(self, project_title):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects' % self._basepath)
    conn.request('GET', path, headers=self._headers)
    resp = conn.getresponse()
    body = resp.read()
    try:
      projects = json.loads(body)
    except ValueError:
      conn.close()
      raise Exception('Error parsing response \'' + body + '\'')
    conn.close()
    for project in projects:
      if project['projectTitle'] == project_title:
        return project
    raise Exception('Project with title \'%s\' not found' % project_title)

  def delete_project_by_title(self, project_title):
    project = self.get_project_by_title(project_title)
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects/%s' % (self._basepath, project['projectId']))
    conn.request('DELETE', path, headers=self._headers)
    conn.close()
    
