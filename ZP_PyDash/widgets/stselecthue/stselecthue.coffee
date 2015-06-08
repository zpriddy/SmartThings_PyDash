class Dashing.Stselecthue extends Dashing.ClickableWidget
  constructor: ->
    super
    @queryState()


  @accessor 'hue',
    get: -> @_hue ? "Unknown"
    set: (key, value) -> @_hue = value

  @accessor 'sat',
    get: -> @_sat ? "50"
    set: (key, value) -> @_sat = value

  @accessor 'level',
    get: -> @_level ? "50"
    set: (key, value) -> @_level = value

  @accessor 'colorhsla',
    get: -> @_colorhsla
    set: (key, value) -> @_colorhsla = value

  postState: ->
    path = '/setselectedhue/' + @get('device') + '/'
    $.post path,
      deviceType: 'color',
      deviceId: @get('device'),

  sethsla: ->
    neshsla = '(' +  @get('hue') * 360 / 100 + ',' + @get('sat') * 255 / 100 + '%,' + @get('level') + '%,1)'
    @set 'colorhsla', newhsla
    return newhsla

  queryState: ->
    path = '/color/' + @get('device')
    $.get path,
      (data) =>
        json = JSON.parse(data)
        @set 'hue', json.hue
        @set 'sat', json.sat
        @set 'colorhsla', '(' +  @get('hue') * 360 / 100 + ',' + @get('sat') * 255 / 100 + '%,' + @get('level') + '%,1)'
   

  ready: ->

  onData: (data) ->
    @queryState()
    

  onClick: (node, event) ->
    @postState()
    Dashing.cycleDashboardsNow(
      boardnumber: @get('page'),
      stagger: @get('stagger'),
      fastTransition: @get('fasttransition'),
      transitiontype: @get('transitiontype'))