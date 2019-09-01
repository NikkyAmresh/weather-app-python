from auth import apikey 
def get_closest_value(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    mid = 0
    if target >= arr[n - 1]:
        return arr[n - 1]
    if target <= arr[0]:
        return arr[0]
    while left < right:
        mid = (left + right)//2
        if target < arr[mid]:
            right = mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            return arr[mid]

    if target < arr[mid]:
        return find_closest(arr[mid - 1], arr[mid], target)
    else:
        return find_closest(arr[mid], arr[mid + 1], target)



def find_closest(val1, val2, target):
    return val2 if target - val1 >= val2 - target else val1

def get_city(num,n):
    import requests, json 
    from flask import jsonify
    if n==0:
        url="https://api.openweathermap.org/data/2.5/weather/?id="+str(num)+"&appid="+apikey
    else:
        url="https://api.openweathermap.org/data/2.5/forecast/?id="+str(num)+"&appid="+apikey 
    r=requests.get(url)
    d=r.json()
    return d
   
def get_forcast(u_lat,u_lon,n):
    import requests, json
    from coordinates import lat, lon 
    from flask import jsonify     
    final_lat=get_closest_value(lat, u_lat)
    final_lon=get_closest_value(lon, u_lon)
    if n==0:
        url="https://api.openweathermap.org/data/2.5/weather/?lat="+str(final_lat)+"&lon="+str(final_lon)+"&appid="+apikey
    else:
        url="https://api.openweathermap.org/data/2.5/forecast/?lat="+str(final_lat)+"&lon="+str(final_lon)+"&appid="+apikey
    r=requests.get(url)
    d=r.json()
    return d