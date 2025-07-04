from statistics import mean

import requests


BASE_URL = 'https://queue-times.com'


def fetch_all_parks():
    url = f'{BASE_URL}/parks.json'
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def fetch_park_wait_times(park_id):
    url = f'{BASE_URL}/parks/{park_id}/queue_times.json'
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def compute_average_wait(wait_data):
    waits = []
    for land in wait_data.get('lands', []):
        for ride in land.get('rides', []):
            wt = ride.get('wait_time')
            if wt is not None:
                waits.append(wt)
    return round(mean(waits), 1) if waits else None
