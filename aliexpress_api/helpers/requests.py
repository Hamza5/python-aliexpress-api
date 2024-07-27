from types import SimpleNamespace
import json

from ..errors import ApiRequestException, ApiRequestResponseException


def api_request(request, response_name):
    try:
        response = request.getResponse()
    except Exception as error:
        if hasattr(error, 'message'):
            raise ApiRequestException(error.message) from error
        raise ApiRequestException(error) from error

    try:
        response = response[response_name]
        resp_code = response.get('rsp_code')
        resp_msg = response.get('rsp_msg')
        response = response.get('resp_result', response)
        response = json.dumps(response)
        response = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
    except Exception as error:
        raise ApiRequestResponseException(error) from error

    resp_code = getattr(response, 'resp_code', resp_code)
    resp_msg = getattr(response, 'resp_msg', resp_msg)

    if resp_code == 200:
        return response.result
    else:
        raise ApiRequestResponseException(f'Response code {resp_code} - {resp_msg}')
