import folium


def build_map(parks_list, data_utils):
    fmap = folium.Map(location=[20, 0], zoom_start=2, control_scale=True)

    for group in parks_list:
        for park in group.get('parks', []):
            lat = float(park['latitude'])
            lon = float(park['longitude'])
            name = park['name']

            wait_json = data_utils.fetch_park_wait_times(park['id'])
            average_wait_time = data_utils.compute_average_wait(wait_json)

            if average_wait_time is None:
                continue

            tooltip = f"{name} — Average Wait Time: {average_wait_time} min"

            folium.Marker(
                [lat, lon],
                tooltip=tooltip,
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(fmap)

    folium.TileLayer(
        tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
        attr='&copy; <a href="https://carto.com/">CARTO</a>',
        name='Modern',
        control=False
    ).add_to(fmap)

    return fmap
