"""Application helpers"""


def make_json_response(data: dict, code: int = 200, mimetype="application/json"):
    import json
    from datetime import datetime
    from flask import make_response, Response

    if isinstance(data, Response):
        return data, code
    elif not isinstance(data, dict):
        data = {}

    response_datetime = datetime.now()
    data['response_datetime'] = response_datetime
    data['status_code'] = code
    data['statusCode'] = code
    response = make_response(json.dumps(data, indent=2, default=str, ensure_ascii=False).encode('utf8'))
    response.mimetype = mimetype
    return response, code