class Dashing.Stmode extends Dashing.ClickableWidget
  constructor: ->
    super
    @queryState()

  @accessor 'mode',
    get: -> @_mode ? "Unknown"
    set: (key, value) -> @_mode = value

  queryState: ->
    $.get '/mode/',
      deviceType: 'mode'
      (data) =>
        json = JSON.parse data
        @set 'mode', json.mode

  ready: ->

  onData: (data) ->
    @queryState()

  onClick: (node, event) ->
    Dashing.cycleDashboardsNow(
      boardnumber: @get('page'),
      stagger: @get('stagger'),
      fastTransition: @get('fasttransition'),
      transitiontype: @get('transitiontype'))