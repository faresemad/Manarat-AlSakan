from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    error_messages = {
        200: "OK.",
        201: "Created.",
        202: "Accepted.",
        204: "No content.",
        400: "Bad request.",
        401: "Unauthorized.",
        402: "Payment required.",
        403: "Forbidden.",
        404: "Not found.",
        405: "Method not allowed.",
        406: "Not acceptable.",
        407: "Proxy authentication required.",
        415: "Unsupported media type.",
        500: "Internal server error.",
        501: "Not implemented.",
        502: "Bad gateway.",
    }

    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__
    if response is not None:
        response.data["status_code"] = response.status_code
        response.data["exception_class"] = exception_class
        response.data["error_message"] = error_messages.get(response.status_code, "Unknown error.")

    return response
