import numpy as np
import onnx

from tests.utils.common import check_onnx_model
from tests.utils.common import make_model_from_nodes


def test_reciprocal() -> None:
    x_variants = (
        np.random.randn(128),
        np.random.randn(64, 128),
        np.random.randn(3, 64, 128),
        np.random.randn(10, 2, 64, 128),
        np.zeros([3, 3, 5]),
    )

    for x in x_variants:
        test_inputs = {'x': x}
        initializers = {}
        node = onnx.helper.make_node(
            op_type='Reciprocal',
            inputs=['x'],
            outputs=['y'],
        )

        model = make_model_from_nodes(nodes=node, initializers=initializers, inputs_example=test_inputs)
        check_onnx_model(model, test_inputs)
