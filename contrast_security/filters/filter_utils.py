from typing import Union


def parse_single_element_list_to_string(input_parameter: Union[str, list]) -> str:
    """
    Used to maintain backwards compatibility with parameters that used to allow a list but now only allow a string
    If the input is a list, then return the first element of the list or the empty string
    """
    if isinstance(input_parameter, list):
        return input_parameter[0] if input_parameter else ''
    else:
        return input_parameter
