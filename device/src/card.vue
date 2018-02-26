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
