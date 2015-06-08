class Dashing.Stswitch extends Dashing.ClickableWidget
  constructor: ->
    super
    @queryState()

  @accessor 'state',
    get: -> @_state ? 'Unknown'
    set: (key, value) -> @_state = value
    

  @accessor 'icon',
    get: -> if @['icon'] then @['icon'] else
      if @get('state') == 'on' then @get('iconon') else @get('iconoff')
    set: Batman.Property.defaultAccessor.set

  @accessor 'iconon',
    get: -> @get('icon') ? 'connectdevelop'
    set: Batman.Property.defaultAccessor.set

  @accessor 'iconoff',
    get: -> @get('icon') ? 'connectdevelop'
    set: Batman.Property.defaultAccessor.set

  @accessor 'icon-style', ->
    if @get('state') == 'on' then 'switch-icon-on' else 'switch-icon-off' 

  toggleState: ->
    newState = if @get('state') == 'on' then 'off' else 'on'
    @set 'state', newState
    return newState   


  queryState: ->
    path = '/switch/' + @get('device')
    $.get path,
      (data) =>
        json = JSON.parse(data)
        @set 'state', json.switch



  postState: ->
    @toggleState()
    path = '/switch/' + @get('device') + '/'
    $.post path,
      deviceType: 'switch',
      deviceId: @get('device'),
      command: 't',
      

  ready: ->

  onData: (data) ->
    @queryState()

  onClick: (event) ->
    @postState()

