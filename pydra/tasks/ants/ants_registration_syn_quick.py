"""
ANTSRegistrationSynQuick
========================

Examples
--------

>>> task = ANTSRegistrationSyNQuick(
...     dimension=3,
...     fixed_image="fixedImage.nii.gz",
...     moving_image="movingImage.nii.gz",
...     output_prefix="output",
... )
>>> task.cmdline
'antsRegistrationSyNQuick.sh -d 3 -f fixedImage.nii.gz -m movingImage.nii.gz -o output'
"""
import os

import attrs

import pydra

__all__ = ["ANTSRegistrationSyNQuick"]


@attrs.define(slots=False, kw_only=True)
class ANTSRegistrationSyNQuickSpec(pydra.specs.ShellSpec):
    """Specifications for antsRegistrationSyNQuick."""

    dimension: int = attrs.field(
        metadata={
            "help_string": "image dimension",
            "mandatory": True,
            "argstr": "-d",
            "allowed_values": {2, 3},
        }
    )

    fixed_image: os.PathLike = attrs.field(
        metadata={
            "help_string": "fixed image",
            "mandatory": True,
            "argstr": "-f",
        }
    )

    moving_image: os.PathLike = attrs.field(
        metadata={
            "help_string": "moving image",
            "mandatory": True,
            "argstr": "-m",
        }
    )

    output_prefix: os.PathLike = attrs.field(
        default="registered",
        metadata={
            "help_string": "output prefix",
            "argstr": "-o",
        },
    )


class ANTSRegistrationSyNQuick(pydra.engine.ShellCommandTask):
    """Task definition for antsRegistrationSyNQuick."""

    input_spec = pydra.specs.SpecInfo(
        name="antsRegistrationSyNQuickInput",
        bases=(ANTSRegistrationSyNQuickSpec,),
    )

    executable = "antsRegistrationSyNQuick.sh"
