<script lang='coffee'>
Vue = require('vue').default
Vue.use require('vue.oauth2/src/plugin').default
Vue.use require('vue.model/src/plugin').default
{eventBus} = require('./eventBus').default

Vue.component 'rest',
  extends: Vue.component 'model'
  data: ->
    mw: [
      @form
      @req
      @res
    ]
  props:
    eventBus:
      default: eventBus
  
export default
  cfg: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: '/cfg'
  ap: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: '/ap'
  sta: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: '/sta'
  ddns: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: '/ddns'
  gpio: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: '/gpio'
  pwm: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: '/pwm'
</script>
