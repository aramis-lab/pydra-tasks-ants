"""
N4BiasFieldCorrection
=====================
"""
import os

import attrs

import pydra

__all__ = ["N4BiasFieldCorrection"]


@attrs.define(slots=False, kw_only=True)
class N4BiasFieldCorrectionSpec(pydra.specs.ShellSpec):
    """Specifications for N4BiasFieldCorrection."""

    dimensionality: int = attrs.field(
        metadata={
            "help_string": "specify image dimensionality (inferred otherwise)",
            "argstr": "-d",
            "allowed_values": {2, 3},
        }
    )

    input_image: os.PathLike = attrs.field(
        metadata={
            "help_string": "input image",
            "mandatory": True,
            "argstr": "-i",
        }
    )

    mask_image: os.PathLike = attrs.field(
        metadata={
            "help_string": "mask image",
            "argstr": "-f",
        }
    )

    rescale_intensities: bool = attrs.field(
        metadata={
            "help_string": "compute new intensity mapping at each iteration",
            "format": lambda rescale_intensities: f"-r {int(rescale_intensities)}",
            "requires": {"mask_image"},
        }
    )

    weight_image: os.PathLike = attrs.field(
        metadata={
            "help_string": "weight image for b-spline fitting",
            "argstr": "-w",
        }
    )

    shrink_factor: int = attrs.field(
        metadata={
            "help_string": "speed computation up with downsizing by this factor",
            "argstr": "-s",
        }
    )

    output_image: os.PathLike = attrs.field(
        metadata={
            "help_string": "output image",
            "mandatory": True,
            "argstr": "-o",
        }
    )


class N4BiasFieldCorrection(pydra.engine.ShellCommandTask):
    """Task definition for N4BiasFieldCorrection."""

    input_spec = pydra.specs.SpecInfo(
        name="N4BiasFieldCorrectionInput",
        bases=(N4BiasFieldCorrectionSpec,),
    )

    executable = "N4BiasFieldCorrection"
