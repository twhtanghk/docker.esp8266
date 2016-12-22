Wifi.scan (res) ->
  console.log (res)

Wifi.on 'connected', (details) ->
  console.log details

Wifi.connect SSID, 
  password: PWD,
  (err) -> 
    console.log err
