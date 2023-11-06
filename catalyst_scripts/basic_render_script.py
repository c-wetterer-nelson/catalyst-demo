# script-version: 2.0
# Catalyst state generated using paraview version 5.11.1-1644-gd4f1d2607b
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1860, 1494]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.CenterOfRotation = [34.5, 32.45, 27.95]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [246.98453802764786, 32.45, 27.95]
renderView1.CameraFocalPoint = [34.5, 32.45, 27.95]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 54.99504523136608
renderView1.LegendGrid = 'Legend Grid Actor'

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1860, 1494)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML MultiBlock Data Reader'
grid = XMLMultiBlockDataReader(registrationName='grid', FileName=['/Users/c.wetterer-nelson/projects/SC23/CxxFullExample/build/datasets/grid_000000.vtm', '/Users/c.wetterer-nelson/projects/SC23/CxxFullExample/build/datasets/grid_000005.vtm'])
grid.CellArrayStatus = ['pressure']
grid.PointArrayStatus = ['velocity']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from grid
gridDisplay = Show(grid, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'pressure'
pressureTF2D = GetTransferFunction2D('pressure')
pressureTF2D.ScalarRangeInitialized = 1
pressureTF2D.Range = [3.0, 3.00048828125, 0.0, 1.0]

# get color transfer function/color map for 'pressure'
pressureLUT = GetColorTransferFunction('pressure')
pressureLUT.TransferFunction2D = pressureTF2D
pressureLUT.RGBPoints = [3.0, 0.231373, 0.298039, 0.752941, 3.000244140625, 0.865003, 0.865003, 0.865003, 3.00048828125, 0.705882, 0.0156863, 0.14902]
pressureLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'pressure'
pressurePWF = GetOpacityTransferFunction('pressure')
pressurePWF.Points = [3.0, 0.0, 0.5, 0.0, 3.00048828125, 1.0, 0.5, 0.0]
pressurePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
gridDisplay.Representation = 'Surface With Edges'
gridDisplay.ColorArrayName = ['CELLS', 'pressure']
gridDisplay.LookupTable = pressureLUT
gridDisplay.SelectTCoordArray = 'None'
gridDisplay.SelectNormalArray = 'None'
gridDisplay.SelectTangentArray = 'None'
gridDisplay.OSPRayScaleArray = 'velocity'
gridDisplay.OSPRayScaleFunction = 'Piecewise Function'
gridDisplay.Assembly = 'Hierarchy'
gridDisplay.SelectOrientationVectors = 'None'
gridDisplay.ScaleFactor = 6.9
gridDisplay.SelectScaleArray = 'None'
gridDisplay.GlyphType = 'Arrow'
gridDisplay.GlyphTableIndexArray = 'None'
gridDisplay.GaussianRadius = 0.34500000000000003
gridDisplay.SetScaleArray = ['POINTS', 'velocity']
gridDisplay.ScaleTransferFunction = 'Piecewise Function'
gridDisplay.OpacityArray = ['POINTS', 'velocity']
gridDisplay.OpacityTransferFunction = 'Piecewise Function'
gridDisplay.DataAxesGrid = 'Grid Axes Representation'
gridDisplay.PolarAxes = 'Polar Axes Representation'
gridDisplay.ScalarOpacityFunction = pressurePWF
gridDisplay.ScalarOpacityUnitDistance = 1.9662121400426065
gridDisplay.OpacityArrayName = ['POINTS', 'velocity']
gridDisplay.SelectInputVectors = ['POINTS', 'velocity']
gridDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
gridDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
gridDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for pressureLUT in view renderView1
pressureLUTColorBar = GetScalarBar(pressureLUT, renderView1)
pressureLUTColorBar.Title = 'pressure'
pressureLUTColorBar.ComponentTitle = ''

# set color bar visibility
pressureLUTColorBar.Visibility = 1

# show color legend
gridDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.5
animationScene1.EndTime = 0.5
animationScene1.PlayMode = 'Snap To TimeSteps'

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'Time Step'

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [1860, 1494]
pNG1.Writer.Format = 'PNG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(grid)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.GlobalTrigger = 'Time Step'
options.CatalystLiveTrigger = 'Time Step'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
