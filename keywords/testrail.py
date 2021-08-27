#
# TestRail API binding for Python 2.x (API v2, available since 
# TestRail 3.0)
#
# Learn more:
#
# http://docs.gurock.com/testrail-api2/start
# http://docs.gurock.com/testrail-api2/accessing
#
# Copyright Gurock Software GmbH. See license.md for details.
#

import urllib2, json, base64
import ssl, dotenv, os, re

api_client = None

def get_value(conf,key):
    "Return the value in conf for a given key"
    value = None
    try:
        #dotenv.load_dotenv(conf)
        #value = os.environ[key]
        value = dotenv.get_key(conf,key)
    except Exception,e:
        print 'Exception in get_value: %s' % e
        print 'file: ',conf
        print 'key: ',key

    return value


def get_testrail_client():
    global api_client
    if api_client is None:
        path_to_file = '/'.join(os.path.dirname(__file__).split('/')[:-1])
        testrail_file = os.path.join(path_to_file,'testrail.env')
        #print 'path_to_config_testrail: %s' % testrail_file
        testrail_url = get_value(testrail_file,'TESTRAIL_URL')
        api_client = APIClient(testrail_url)
        api_client.user = get_value(testrail_file,'TESTRAIL_USER')
        api_client.password = get_value(testrail_file,'TESTRAIL_PASSWORD')
    return api_client


def testrail_api(command, *args, **kwargs):
    global api_client
    api_client = get_testrail_client()
    command = command.lower()
    uri = command
    for arg in args:
        uri += '/%s' % arg
    try:
        if re.match('get', command):
            if len(kwargs) != 0:
                for key in kwargs:
                    uri += '&%s=%s' %(key, kwargs[key])
            result = api_client.send_get(uri)
        else:
            result = api_client.send_post(uri, kwargs)
    except Exception,e:
        print 'ERROR in testrail_api for command %s : %s' %(uri,e)
    return result


class APIClient:
	def __init__(self, base_url):
		self.user = ''
		self.password = ''
		if not base_url.endswith('/'):
			base_url += '/'
		self.__url = base_url + 'index.php?/api/v2/'

	#
	# Send Get
	#
	# Issues a GET request (read) against the API and returns the result
	# (as Python dict).
	#
	# Arguments:
	#
	# uri                 The API method to call including parameters
	#                     (e.g. get_case/1)
	#
	def send_get(self, uri):
		return self.__send_request('GET', uri, None)

	#
	# Send POST
	#
	# Issues a POST request (write) against the API and returns the result
	# (as Python dict).
	#
	# Arguments:
	#
	# uri                 The API method to call including parameters
	#                     (e.g. add_case/1)
	# data                The data to submit as part of the request (as
	#                     Python dict, strings must be UTF-8 encoded)
	#
	def send_post(self, uri, data):
		return self.__send_request('POST', uri, data)

	def __send_request(self, method, uri, data):
		url = self.__url + uri
		request = urllib2.Request(url)
		if (method == 'POST'):
			request.add_data(json.dumps(data))
		auth = base64.b64encode('%s:%s' % (self.user, self.password))
		request.add_header('Authorization', 'Basic %s' % auth)
		request.add_header('Content-Type', 'application/json')

		e = None
		try:
			response = urllib2.urlopen(request, context=ssl._create_unverified_context()).read()
		except urllib2.HTTPError as e:
			response = e.read()

		if response:
			result = json.loads(response)
		else:
			result = {}

		if e != None:
			if result and 'error' in result:
				error = '"' + result['error'] + '"'
			else:
				error = 'No additional error message received'
			raise APIError('TestRail API returned HTTP %s (%s)' % 
				(e.code, error))

		return result

class APIError(Exception):
	pass
