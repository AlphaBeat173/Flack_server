# Flask OSC Server

A Flask web server to send OSC messages to a target (e.g. Reaper).

## Endpoints

- `/play`
- `/stop`
- `/seek?time=3.5`
- `/send_osc?address=/volume&value=0.5`

## Deploy on Render or Railway

Don't forget to set environment variables:

- `OSC_TARGET_IP` = `10.201.60.198`
- `OSC_TARGET_PORT` = `8000`
