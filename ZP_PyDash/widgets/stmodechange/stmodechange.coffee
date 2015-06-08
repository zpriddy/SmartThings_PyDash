class Dashing.Stmodechange extends Dashing.ClickableWidget
  constructor: ->
    super


  @accessor 'mode',
    get: -> @_mode ? "Unknown"
    set: (key, value) -> @_mode = value


  ready: ->

  onData: (data) ->


  onClick: (node, event) ->
    path = '/setmode/' + @get('mode')
    $.get path
    Dashing.cycleDashboardsNow(
      boardnumber: @get('page'),
      stagger: @get('stagger'),
      fastTransition: @get('fasttransition'),
      transitiontype: @get('transitiontype'))