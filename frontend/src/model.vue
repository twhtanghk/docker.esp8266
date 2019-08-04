<script lang='coffee'>
Vue = require('vue').default
Vue.use require('vue.model/src/plugin').default
{eventBus} = require('./lib').default

Vue.component 'rest',
  extends: Vue.component 'model'
  props:
    eventBus:
      default: ->
        eventBus
  
export default
  cfg: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.API_URL}"
  ap: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.API_URL}/ap"
  sta: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.API_URL}/sta"
  syslog: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.API_URL}/log"
  ddns: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.API_URL}/ddns"
  gpio: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.API_URL}/gpio"
  pwm: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.API_URL}/pwm"
</script>
