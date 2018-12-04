<template>
  <div id='ap'>
    <card header='Settings'>
      <form-col>
        <div slot='fields'>
          <field name='essid'>
            <b-form-input v-model='essid' type='text' required />
          </field>
          <field name='password'>
            <b-form-input v-model='password' type='password' data-minlength='8' required />
          </field>
          <field name='authmode'>
            <b-form-input v-model='authmode' type='text' disabled />
          </field>
        </div>
        <div slot='buttons' class='action'>
          <b-button variant="primary" @click='save(essid, password)'>Save</b-button>
        </div>
      </form-col>
    </card>
    <card header='System'>
      <div class='action'>
        <b-button variant="primary" @click='reset()'>Restart</b-button>
        <b-button variant="primary" @click='factory()'>Factory Config</b-button>
      </div>
    </card>
  </div>
</template>

<script lang='coffee'>
{ap, cfg} = require('./model').default

export default
  component:
    model: require('./model').default
    card: require('./card').default
    formCol: require('./form').default
    field: require('./field').default
  data: ->
    essid: ''
    password: ''
    authmode: ''
  methods:
    getStatus: ->
      ap.get()
        .then (res) =>
          @essid = res.essid
          @authmode = res.authmode
        .catch console.error
    save: (essid, password) ->
      ap
        .put
          data:
            essid: essid
            password: password
        .then ->
          console.info 'saved successfully'
        .catch console.error
    reset: ->
      cfg
        .read 'reset'
        .then ->
          console.info 'reset in progress'
        .catch console.error
    factory: ->
      cfg
        .read 'factory'
        .then (res) =>
          @essid = res.essid
          @authmode = res.authmode
        .catch console.error
  mounted: ->
    @getStatus()
</script>
