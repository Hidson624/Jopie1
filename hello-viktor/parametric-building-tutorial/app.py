import viktor as vkt


class Parametrization(vkt.Parametrization):
    width = vkt.NumberField('Width', min = 0, default=30 )
    length = vkt.NumberField('Length', min = 0, default=30 )

class Controller(vkt.Controller):
    parametrization = Parametrization
    @vkt.GeometryView("3D gebouw", x_axis_to_right=True)
    def get_geometry(self, params, **kwargs):
        #Materials:
        glass = vkt.Material("Glass", color=vkt.Color(150, 150, 255))
        facade = vkt.Material("Concrete")

        floor_glass = vkt.SquareBeam(
            length_x=params.width,
            length_y=params.length,
            length_z=2,                    #<-- change this
            material=glass
        )
        floor_facade = vkt.SquareBeam(
            length_x=params.width+1,       #<-- change this
            length_y=params.length+2,      #<-- change this
            length_z=1,
            material=facade
        )

        floor_facade.translate((0, 0, 1.5)) #<-- add this

        floor = vkt.Group([floor_glass, floor_facade])
        
        building= vkt.LinearPattern(floor, direction=[0, 0, 1], number_of_elements=16, spacing=3)

        return vkt.GeometryResult(building)

