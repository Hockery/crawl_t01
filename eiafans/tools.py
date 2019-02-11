from urllib.parse import urlparse, parse_qs

dowload_file_path = {}
# import urllib
def get_parameter(url): 
    query = urlparse(url).query 
    return dict([(k,v[0]) for k,v in parse_qs(query).items()])