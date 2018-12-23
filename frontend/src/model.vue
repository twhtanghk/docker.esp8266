<script lang='coffee'>
Vue = require('vue').default
Vue.use require('vue.model/src/plugin').default
{eventBus} = require('./lib').default

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
      default: ->
        eventBus
  
export default
  cfg: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.VUE_APP_BASE_URL}/cfg"
  ap: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.VUE_APP_BASE_URL}/ap"
  sta: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.VUE_APP_BASE_URL}/sta"
  ddns: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.VUE_APP_BASE_URL}/ddns"
  gpio: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.VUE_APP_BASE_URL}/gpio"
  pwm: new Vue
    extends: Vue.component 'rest'
    props:
      baseUrl:
        default: "#{process.env.VUE_APP_BASE_URL}/pwm"
</script>
