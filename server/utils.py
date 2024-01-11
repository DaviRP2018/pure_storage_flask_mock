import datetime
import os

from settings import SESSION_LOCATION


def get_synced_response(api_responses, logger):
    """
    This function is essential for proper testing and monitoring,

    Some APIs have multiple responses to simulate a real server, and instead of
    just random choosing one of the responses we will select the response based
    on the current minute.

    We don't want random choices because this will make different SL1 register
    different graphs and collections, which will nullify our capability of comparison
    between SL1s/SL1 versions

    So this function will basically get the list length and spread its contents
    evenly over the current hour. Along 60 minutes.

    So, for example, if we have 3 items
    60 minutes:
    0 - 19 = item 1 selected
    20 - 39 = item 2 selected
    40 - 59 = item 3 selected

    If we have 7 items:
    60 / 7 ~= 9 (round up)
    0 - 9 = item 1 selected
    10 - 18 = item 2 selected
    19 - 27 = item 3 selected
    28 - 36 = item 4 selected
    37 - 45 = item 5 selected
    46 - 54 = item 6 selected
    55 - 63 = item 7 selected
    """
    section_size = round(60 / len(api_responses))
    # The initial section_limit is the section_size
    section_index = _get_section_index(section_size, section_size, logger)
    # Debug
    logger.debug("api_responses[section_index] = %s", api_responses[section_index])
    return api_responses[section_index]


def _get_section_index(section_size, section_limit, logger, index=0):
    """
    This selects the current index for the minute.
    """
    minute = datetime.datetime.now().minute
    if minute >= section_limit:
        # Go to next section
        index += 1
        section_limit += section_size
        return _get_section_index(section_size, section_limit, logger, index)
    # Debug
    logger.debug(
        "minute: %s" " - section_limit: %s" " - section_index: %s",
        datetime.datetime.now().minute,
        section_limit,
        index,
    )
    return index


def session_exists(remote_address, logger):
    file_path = f"{SESSION_LOCATION}/pure_session_{remote_address}"

    if os.path.exists(file_path):
        logger.info("The session exists for %s.", remote_address)
        return True
    else:
        logger.info("The session for %s does not exist.", remote_address)
        return False


def delete_session(remote_address):
    file_path = f"{SESSION_LOCATION}/pure_session_{remote_address}"
    os.remove(file_path)
