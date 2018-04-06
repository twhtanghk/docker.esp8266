<template>
</template>

<script lang='coffee'>
module.exports =
  extends: require('vue.model/src/model').default
  data: ->
    mw: [
      @form
      @req
    ]
  methods:
    param: (data) ->
      ret = new URLSearchParams()
      for k, v of data
        ret.set k, v
      ret
    form: (opts) ->
      opts.headers ?= {}
      opts.headers['Content-Type'] = 'application/x-www-form-urlencoded'
      opts.body = @param opts.data
</script>
