class SysCtrl
  info: (req, res) ->
    res.end cjson.encode name: wifi.sta.gethostname()

return SysCtrl()
