<template>
  <div id='ddns'>
    <form-col>
      <div slot='fields'>
        <field name='url'>
          <b-form-input v-model='url' type='text' />
        </field>
        <field name='interval (sec)'>
          <b-form-input v-model='interval' type='number' />
        </field>
        <field name='hostname'>
          <b-form-input v-model='host' type='text' />
        </field>
        <field name='user'>
          <b-form-input v-model='user' type='text' />
        </field>
        <field name='password'>
          <b-form-input v-model='pass' type='password' />
        </field>
        <field name='enable'>
          <b-form-checkbox v-model='enable' :value='true' :unchecked-value='false' />
        </field>
      </div>
      <div slot='buttons' class='action'>
        <b-button variant="primary" @click='save'>Save</b-button>
      </div>

    </form-col>
  </div>
</template>

<script lang='coffee'>
{ddns} = require('./model').default

export default
  components:
    model:
      extends: require('vue.model/src/model').default
      data: ->
        mw: [
          @form
          @req
          @res
        ]
  data: ->
    url: ''
    interval: 0
    host: ''
    user: ''
    pass: ''
    enable: false
  methods:
    get: ->
      ddns.get()
        .then (res) =>
          @url = res.url
          @interval = res.interval
          @host = res.host
          @enable = res.enable
        .catch console.error
    save: ->
      ddns
        .put data: _.pick @, 'url', 'interval', 'host', 'user', 'pass', 'enable'
        .then ->
          console.info 'saved successfully'
        .catch console.error
  created: ->
    @get()
</script>
