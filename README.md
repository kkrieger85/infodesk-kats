# infodesk-kats



## Parts:

- Should be available as docker compose setup
- Should be usable by an non-tech person

### Frontend 
- Devices: TV + Mobile
- JS Framework like Vue, React, Svelte with PWA possibilities

- View:
  - Maps with POI
    - https://leafletjs.com/ to use.
    - https://leaflet.github.io/Leaflet.draw/docs/leaflet-draw-latest.html  Add Point, Circles & Polygons
  - Legenda for Map
  - Newsfeed (order by prio), maybe autoscroll
  - TV Only: QR Code for Wifi
  - Accesibility

### BFF
- Device: Laptop + Tablet
- CMS functionality
- Map as central information 

### BE
- Offline-compatible webserver

### OSM-Server
- Germany only (e.g. https://download.geofabrik.de/europe.html aprox 4.1GB)
- Better per federal state
 - e.g. Saarland: https://download.geofabrik.de/europe/germany.html (aprox 48.5 MB)

**Solution**
https://github.com/Overv/openstreetmap-tile-server can & will be used for our purpose.
https://hub.docker.com/r/overv/openstreetmap-tile-server

## Hardware:

- Raspberry Pi 
- TV / Monitor (should be waterproof)
- Accesspoint / Network 
  - should be able to handle 200 users
  - should redirect all requests to the own webserver
- Powerstation + Solarpanel
