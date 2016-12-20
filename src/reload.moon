return (module) ->
  package.loaded[module] = nil
  require module
