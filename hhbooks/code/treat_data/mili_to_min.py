def millis_to_min_str(millis: int or float) -> str:
    """
    Function to convert and format milliseconds to minutes

    Parameters:
        millis (int or float): the number of milliseconds to be converted. If it is a float it will be converted to an int.
    Returns:
        (str): a string with the formated and converted milliseconds. mins:secs ex: 3:01
    """

    # turn milliseconds to an integer
    millis = int(millis)

    # calculate the seconds
    secs = (millis/1000) % 60
    secs = int(secs)

    # calculate the minutes
    mins = (millis/(1000*60)) % 60
    mins = int(mins)

    # format the output
    formated = f"{mins}:{secs:02}"
    return formated
