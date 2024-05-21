from ip2geotools.databases.noncommercial import DbIpCity

def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_geolocation(ip_address):
    try:
        response = DbIpCity.get(ip_address, api_key='free')
        return f'{response.city}, {response.region}, {response.country}'
    except:
        return 'Unknown location'