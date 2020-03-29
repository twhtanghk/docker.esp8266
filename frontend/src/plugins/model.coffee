{Model} = require('model').default
  
export default
  Cfg: new Model
    baseUrl: "#{process.env.API_URL}"
  Ap: new Model
    baseUrl: "#{process.env.API_URL}/ap"
  Sta: new Model
    baseUrl: "#{process.env.API_URL}/sta"
  Syslog: new Model
    baseUrl: "#{process.env.API_URL}/log"
  Ddns: new Model
    baseUrl: "#{process.env.API_URL}/ddns"
  Gpio: new Model
    baseUrl: "#{process.env.API_URL}/gpio"
  Pwm: new Model
    baseUrl: "#{process.env.API_URL}/pwm"
  Dht: new Model
    baseUrl: "#{process.env.API_URL}/dht"
  Liquid: new Model
    baseUrl: "#{process.env.API_URL}/liquid"
  Gpio: new Model
    baseUrl: "#{process.env.API_URL}/gpio"
