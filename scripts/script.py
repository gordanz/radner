from vtk import *

lut = vtk.vtkLookupTable()
lut.SetNumberOfColors(256)
lut.SetHueRange(0.4,0.5)
lut.Build()
rng = [0,0]

reader = vtk.vtkPolyDataReader()
reader.SetFileName("c.vtk")
reader.Update()

geofilter = vtk.vtkGeometryFilter()
geofilter.SetInputConnection(reader.GetOutputPort())

theMapper = vtk.vtkDataSetMapper()
theMapper.SetInputConnection(reader.GetOutputPort())

theActor = vtk.vtkActor()
theActor.SetMapper(theMapper)

ren = vtk.vtkRenderer()
ren.AddActor(theActor)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetPosition(900,500)
renWin.SetSize(1050, 800)



iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

iren.Initialize()
renWin.Render()
iren.Start()
