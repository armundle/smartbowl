- For every x seconds:

-- getData() # Poll the sensor, get values, convert, return.

--- Is it aboveThreshold() and minTimeElapsed() # > 200g? AND >5s

--- True: sendText()

--- False: continue

--------------------------
# Policy
- Board will send weight every 5s.
- Cloud will decide what to do with this value depending on the timestamp.

