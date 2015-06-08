class Dashing.Stselectcolor extends Dashing.ClickableWidget
  constructor: ->
    super


  @accessor 'color',
    get: -> @_color ? "Unknown"
    set: (key, value) -> @_color = value

  @accessor 'hue',
    get: -> @_hue ? "Unknown"
    set: (key, value) -> @_hue = value

  @accessor 'sat',
    get: -> @_sat ? "Unknown"
    set: (key, value) -> @_sat = value

  @accessor 'level',
    get: -> @_level ? "Unknown"
    set: (key, value) -> @_level = value

  @accessor 'colorhsla',
    get: -> '(' +  @get('hue') + ',' + @get('sat') + '%,' + @get('level') + '%,1)'
    set: (key, value) -> @colorhsla = value

  postState: ->
    path = '/setcolor/'
    $.post path,
      deviceType: 'color',
      color: @get('color')
      hue: @get('hue'),
      sat: @get('sat'),


  ready: ->

  onData: (data) ->

  onClick: (node, event) ->
    @postState()
    Dashing.cycleDashboardsNow(
      boardnumber: @get('page'),
      stagger: @get('stagger'),
      fastTransition: @get('fasttransition'),
      transitiontype: @get('transitiontype'))
