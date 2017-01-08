class SysCtrl
  info: (req, res) ->
    switch req.id
      when 'info'
        res.end JSON.stringify 
          name: wifi.getHostname()
      else
        res.notFound()

module.exports =
  SysCtrl: new SysCtrl()
