Theme Parks Queue Times
============

This project fetches real-time wait times from theme parks using the [Queue Times](https://queue-times.com/) API and generates an interactive map that displays each theme park’s location and current wait time.

---

## main.py
The core logic of the project.
- Fetches real-time wait time data from the Queue Times API.
- Matches data with theme park metadata.
- Passes the combined data to generate the map.

To run this script manually:
```
python main.py
```

---

## scheduled_runner.py
This is the automation layer.
- Uses the schedule library to call main() every hour.
- Runs continuously in the background and checks every 60 seconds.

To start automated hourly updates:
```
python scheduled_runner.py
```

---

## theme_parks.py
Contains a list of theme parks.
- Matches API data to theme park locations.
- Displays accurate locations on the map.

---

## map_builder.py
Responsible for rendering the interactive map.
- Generates theme park markers based on real coordinates.
- Saves the map as theme_parks_wait_map.html in the project folder.

---

## Dependencies

```
folium
requests
schedule
```
