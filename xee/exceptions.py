#!/usr/bin/env python
# coding: utf8
"""This script contains exceptions for the SDK"""


class ParseException(Exception):
    """
        Parse exception (a ValueError when parsing)
    """

    def __init__(self, parent):
        super(ParseException, self).__init__(parent.message)


class APIException(Exception):
    """
        Basic API Exception (Http error with a specific message)
        see https://github.com/xee-lab/xee-api-docs/tree/master/api/api/v3#errors
    """

    def __init__(self, error, error_description):
        super(APIException, self).__init__(error_description)
        self.error = error
        self.error_description = error_description

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
