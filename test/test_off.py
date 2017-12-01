# -*- coding: utf-8 -*-
#
import meshio
import pytest

import helpers


@pytest.mark.parametrize('mesh', [
    helpers.tri_mesh
    ])
def test_io(mesh):
    helpers.write_read2(
        meshio.off_io.write,
        meshio.off_io.read,
        mesh, 1.0e-15
        )
    return
