import jsonschema
import json


class Schemas:
    SIGNUP_SCHEMA = {
        "type": "object",
        "properties": {
            "account_type": {"type": "number"},
            "fname": {"type": "string"},
            "sname": {"type": "string"},
            "uname": {"type": "string"},
            "gender": {"type": "string", "enum": ["male", "female"]},
            "dob": {"type": "string", "format": "date"},
            "email": {"type": "string", "format": "idn-email"},
            "phone": {"type": "string", "maxLength": 10},
            "street_apt": {"type": "string"},
            "district": {"type": "string"},
            "city": {"type": "string"},
            "state": {"type": "string"},
            "pin": {"type": "string"},
            "password": {"type": "string"}
        },
        "required": ["account_type", "fname", "sname", "email", "uname", "password"]
    }


def valid_signup(form_data):
    allowed_hosts_json = form_data
    try:
        jsonschema.validate(instance=allowed_hosts_json, schema=Schemas.SIGNUP_SCHEMA, format_checker=jsonschema.draft4_format_checker)
    except jsonschema.exceptions.ValidationError:
        return False
    return True
