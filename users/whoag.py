x=hotkey('w').setup('whToggleTranslateModePress')
x=hotkey('w', release=True).setup('whToggleTranslateModeRelease')
x=hotkey('e').setup('whToggleRotateModePress')
x=hotkey('e', release=True).setup('whToggleRotateModeRelease')
x=hotkey('r').setup('whToggleScaleModePress')
x=hotkey('r', release=True).setup('whToggleScaleModeRelease')
x=hotkey('g').setup('whInitialize')
x=hotkey(',').setup('whPreviousFrame')
x=hotkey('.').setup('whNextFrame')
x=hotkey(',', alt=True).setup('whPreviousKey')
x=hotkey('.', alt=True).setup('whNextKey')
x=hotkey('d', ctl=True, alt=True).setup('snapMe pivot', name='snapme_pivot')
x=hotkey('w', ctl=True, alt=True).setup('snapMe position', name='snapme_position')
x=hotkey('e', ctl=True, alt=True).setup('snapMe rotation', name='snapme_rotation')
x=hotkey('r', ctl=True, alt=True).setup('snapMe scale', name='snapme_scale')

# Display Hotkeys
x=hotkey('D', ctl=True).setup('whToggleDeformers')
x=hotkey('G', ctl=True).setup('whToggleGrid')
x=hotkey('I', ctl=True).setup('whToggleIsolateSelect')
x=hotkey('J', ctl=True).setup('whToggleJoints')
x=hotkey('L', ctl=True).setup('whToggleLocators')
x=hotkey('C', ctl=True).setup('whToggleNurbsCurves')
x=hotkey('N', ctl=True).setup('whToggleNurbsSurfaces')
x=hotkey('P', ctl=True).setup('whTogglePolygons')
x=hotkey('W', ctl=True).setup('whToggleWireframeOnShaded')
x=hotkey('X', ctl=True).setup('whToggleXRay')
x=hotkey('Z', ctl=True).setup('whToggleXRayJoints')
x=hotkey('A', alt=True).setupHotkey('AttributeEditor')
x=hotkey('C', alt=True).setupHotkey('ConnectionEditor')
x=hotkey('G', alt=True).setupHotkey('GraphEditor')
x=hotkey('H', alt=True).setupHotkey('HypergraphHierarchyWindow')
x=hotkey('P', ctl=True, alt=True).setupHotkey('PlayblastOptions')
x=hotkey('H', ctl=True, alt=True).setupHotkey('HypergraphDGWindow')
x=hotkey('H', ctl=True, alt=True, cmd=True).setupHotkey('HotkeyPreferencesWindow')
x=hotkey('H', alt=True, cmd=True).setupHotkey('HypershadeWindow')
x=hotkey('O', alt=True).setupHotkey('OutlinerWindow')
x=hotkey('P', alt=True).setupHotkey('PlayblastWindow')
x=hotkey('R', alt=True).setupHotkey('RenderViewWindow')
x=hotkey('S', alt=True).setupHotkey('ScriptEditor')
x=hotkey('T', alt=True).setupHotkey('ToolSettingsWindow')
x=hotkey('Space', alt=True).setup('abToggleUIVis')