import pathlib


def build_url(html_filename):
    """Build the URL to a HTML test file.

    Parameters
    ----------
    html_filename : str
        The name of a HTML file.

    Returns
    -------
    url : str
        The URL for the HTML file.

    """
    base_directory = pathlib.Path(__file__).resolve().parent.parent

    return "file://{}/tests/html/{}".format(base_directory, html_filename)
