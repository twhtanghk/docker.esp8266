React = require 'react'
E = require 'react-script'
AppBar = require('material-ui/AppBar').default
Drawer = require('material-ui/Drawer').default
MenuItem = require('material-ui/MenuItem').default

class _AppBar extends React.Component
  state:
    open: false

  menu: =>
    @setState (state) ->
      state.open = not state.open
      true

  render: ->
    E AppBar,
      title: @state.name
      onLeftIconButtonClick: @menu,
      E Drawer,
        open: @state.open
        docked: false
        E MenuItem,
          onClick: @menu,
          'wlan'
   
module.exports =
  component: _AppBar
