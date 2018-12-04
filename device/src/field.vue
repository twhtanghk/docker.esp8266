<template>
  <b-form-group :label='name'>
     <slot/>
  </b-form-group>
</template>

<script lang='coffee'>
export default
  props: [
    'name'
  ]
</script>
