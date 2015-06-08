class Dashing.Stselectdimmer extends Dashing.ClickableWidget
  constructor: ->
    super
    @queryState()


  @accessor 'state',
    get: -> @_state ? 'off'
    set: (key, value) -> @_state = value

  @accessor 'level',
    get: -> if @get('state') != 'off' then @_level else 'Off'
    set: (key, value) -> @_level = value

  @accessor 'levellabel',
    get: -> if @get('state') != 'off' then @get('level') + '%' else 'Off'
    set: (key, value) -> @_level = value

  @accessor 'opacitylevel',
    get: -> if @get('state') == 'off' then '100 ; color:Black' else @get('level') / 50
    set: (key, value) -> @_opacitylevel = value

  postState: ->
    path = '/setselecteddimmer/' + @get('device') + '/'
    $.post path,
      deviceType: 'dimmer',
      deviceId: @get('device'),

  queryState: ->
    path = '/dimmer/' + @get('device') 
    $.get path,
      deviceType: 'dimmer',
      deviceId: @get('device')
      (data) =>
        json = JSON.parse data
        @set 'state', json.state
        @set 'level', json.level

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
