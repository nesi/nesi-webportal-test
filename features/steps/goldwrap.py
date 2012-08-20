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
    
  def get_project(self, project_id):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects/%s' % (self._basepath, project_id))
    conn.request('GET', path, headers=self._headers)
    resp = conn.getresponse()
    body = resp.read()
    try:
      project = json.loads(body)
    except ValueError:
      conn.close()
      raise Exception('Error parsing response \'' + body + '\'')
    conn.close()
    if not 'projectId' in project or project['projectId'] != project_id:
      raise Exception('Project with id %s not found' % project_id)
    return project

  def delete_project(self, project_id):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects/%s' % (self._basepath, project_id))
    conn.request('DELETE', path, headers=self._headers)
    resp = conn.getresponse()
    status = resp.status
    conn.close()
    if status != httplib.NO_CONTENT:
      raise Exception('Delete project: Expected status %s but got %s' % httplib.NO_CONTENT, resp.status)
    