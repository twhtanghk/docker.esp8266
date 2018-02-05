<template>
  <b-tabs>
    <b-tab title='net' active>
      <net/>
    </b-tab>
    <b-tab title='pwm'>
      <pwm/>     
    </b-tab>
  </b-tabs>
</template>

<script lang='coffee'>
pwm = require('./pwm').default
net = require('./net').default

module.exports =
  components:
    net: net
    pwm: pwm
</script>

<style lang='scss'>
@import '~bootstrap/scss/bootstrap.scss';
</style>
