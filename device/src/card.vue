<template>
  <b-card :id='id' :header='header'>
    <p>
      <slot/>
    </p>
  </b-card>
</template>

<script lang='coffee'>
module.exports =
  props: [
    'id'
    'header'
    'bgVariant'
  ]
</script>

<style lang='scss' scoped>
.card-body > p {
  margin-bottom: 0;
}
</style>
