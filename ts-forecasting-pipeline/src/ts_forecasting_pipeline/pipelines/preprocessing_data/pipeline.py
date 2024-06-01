from kedro.pipeline import Pipeline, node
from  nodes import *

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func='',
                inputs='',
                outputs='',
                name=''
            ),
        ]
    )