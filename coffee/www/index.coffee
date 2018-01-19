require './index.scss'
React = require 'react'
E = require 'react-script'
ReactDOM = require 'react-dom'
MuiThemeProvider = require('material-ui/styles/MuiThemeProvider').default
AppBar = require('./appbar.coffee').component
{compose, createStore, combineReducers, applyMiddleware} = require 'redux'
{Provider, connect} = require 'react-redux'
Toastr = require 'react-redux-toastr'

reducer = combineReducers
  toastr: Toastr.reducer

composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose
store = createStore reducer, {}, composeEnhancers()

elem =
  E Provider, store: store,
    E MuiThemeProvider,
      E 'div',
        E Toastr.default
        E AppBar

ReactDOM.render elem, document.getElementById 'root'
