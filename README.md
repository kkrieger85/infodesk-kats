# infodesk-kats



## Parts:

Should be available as docker compose setup

Frontend 
- Devices: TV + Mobile
- JS Framework like Vue, React, Svelte with PWA possibilities

- View:
  - Maps with POI
  - Legenda for Map
  - Newsfeed (order by prio), maybe autoscroll
  - TV Only: QR Code for Wifi
  - Accesibility

BFF
- Device: Laptop + Tablet
- CMS functionality
- Map as central information 

BE
- Offline-compatible webserver

OSM-Server
- Germany only
- Better per federal state

## Hardware:

Raspberry Pi 
TV / Monitor (should be waterproof)
Accesspoint / Network 
- should be able to handle 200 users
- should redirect all requests to the own webserver
Powerstation + Solarpanel
