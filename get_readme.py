import requests

# Possible valid url prefixes
all_prefix  = [
    "https://github.com",
    "https://www.github.com",
    "http://github.com",
    "http://www.github.com",
    "github.com",
    "www.github.com"
]

def startswith_any(all_prefix, url):
    """Check if `url` is a valid github link"""

    for prefix in all_prefix:
        if url.startswith(prefix):
            return prefix
    
    return False

def get_rawdata_link(url):
    """Returns the README.md file link"""

    _prefix = startswith_any(all_prefix, url)

    if _prefix:
        url = url.replace(_prefix,"",1)
        paths = url.split("/")

        paths_list = []

        for x in paths:
            if x.strip():
                paths_list.append(x)

        if len(paths_list) > 1:
            username = paths_list[0]
            project_name = paths_list[1]
            raw_data_link = f"https://raw.githubusercontent.com/{username}/{project_name}/master/README.md"

            return raw_data_link

    return None

def get_readme_md(url):
    """Return README.md file raw data"""
    
    raw_data_link = get_rawdata_link(url)

    if raw_data_link:
        # prepare headers
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

        # fetching the url, raising error if operation fails
        try:
            response = requests.get(raw_data_link, headers=headers)
        except Exception as e:
            pass
        
        if response.ok and response.status_code == 200:
            return response.text
    
    return None
