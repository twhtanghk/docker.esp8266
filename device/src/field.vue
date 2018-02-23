<template>
  <b-form-group :label='name'>
     <slot/>
  </b-form-group>
</template>

<script lang='coffee'>
module.exports =
  props: [
    'name'
  ]
</script>
