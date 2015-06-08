class Dashing.Stweather extends Dashing.Widget
  constructor: ->
    super
    @queryWeather()
    @_icons =
      chanceflurries: '&#xe036',
      chancerain: '&#xe009',
      chancesleet: '&#xe003',
      chancesnow: '&#xe036',
      chancetstorms: '&#xe025',
      clear: '&#xe028',
      cloudy: '&#xe000',
      flurries: '&#xe036',
      fog: '&#xe01b',
      hazy: '&#xe01b',
      mostlycloudy: '&#xe001',
      mostlysunny: '&#xe001',
      partlycloudy: '&#xe001',
      partlysunny: '&#xe001',
      sleet: '&#xe003',
      rain: '&#xe009',
      snow: '&#xe036',
      sunny: '&#xe028',
      tstorms: '&#xe025'



  @accessor 'todayicon', ->
    get: -> @_todayicon ? "??"
    set: (key, value) -> @_todayicon = value

  @accessor 'tomorrowicon', ->
    get: -> @_tomorrowicon ? "??"
    set: (key, value) -> @_tomorrowicon = value


  @accessor 'now_temp', ->
    get: -> @_now_temp ? "??"
    set: (key, value) -> @_now_temp = value

  @accessor 'wicon', ->
    get: -> @_wicon ? "??"
    set: (key, value) -> @_wicon = value

  @accessor 'now_temp',
    get: -> if @_temp then Math.floor(@_temp) else 0
    set: (key, value) -> @_temp = value

  @accessor 'precip',
    get: -> if @_precip then Math.floor(@_precip) else 0
    set: (key, value) -> @_precip = value

  @accessor 'tomorrow_precip',
    get: -> if @_tomorrow_precip then Math.floor(@_tomorrow_precip) else 0
    set: (key, value) -> @_tomorrow_precip = value

  @accessor 'temp_high',
    get: -> if @_temp_high then Math.floor(@_temp_high) else 0
    set: (key, value) -> @_temp_high = value

  @accessor 'temp_low',
    get: -> if @_temp_low then Math.floor(@_temp_low) else 0
    set: (key, value) -> @_temp_low = value

  @accessor 'tomorrow_temp_high',
    get: -> if @_tomorrow_temp_high then Math.floor(@_tomorrow_temp_high) else 0
    set: (key, value) -> @_tomorrow_temp_high = value

  @accessor 'tomorrow_temp_low',
    get: -> if @_tomorrow_temp_low then Math.floor(@_tomorrow_temp_low) else 0
    set: (key, value) -> @_tomorrow_temp_low = value

  

  queryWeather: ->
    $.get '/weather/',
      deviceType: 'mode'
      (data) =>
        json = JSON.parse data
        @set 'tomorrow_precip',json.tomorrow_precip
        @set 'precip', json.precip
        @set 'now_temp', json.temperature
        @set 'tomorrow_temp_high',json.tomorrow_temp_high
        @set 'tomorrow_temp_low', json.tomorrow_temp_low
        @set 'temp_high', json.high
        @set 'temp_low', json.low
        @set 'today_icon', json.icon
        @set 'tomorrow_icon', json.tomorrow_icon
        
        
        

  ready: ->

  onData: (data) ->
    @queryWeather()
