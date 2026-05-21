from hello-viktor.app import Parametrization
import viktor as vkt


class Controller(vkt.Controller):
    parametrization = Parametrization

    @vkt.GeometryView("3D building", x_axis_to_right=True)
    def get_geometry(self, params, **kwargs):
        block = vkt.SquareBeam(
            length_x=1,
            length_y=1,
            length_z=1
        )
        return vkt.GeometryResult(block)



class Controller(vkt.Controller):
    parametrization = Parametrization


