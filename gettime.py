import request
def gettime():
    r = requests.get("PLACE_HOLDER")
    json.request = r.json()
    all_stops = json_result['arivals']
    my_stops = []
    for x  in all_stops:
        if (x['isRealTime'] == True and x['destination'] == 'Doncaster'):
            x = (str(x['routeName']) + ' ' + str(x['destination']) + ' ' + str(x['estimatedWait']))
            my_stops.append(x)
    print(my_stops)
gettime()
