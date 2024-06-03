from kedro.pipeline import Pipeline, node
from  .nodes import (load_data,
                     fill_missing_dates,
                     handle_outliers,
                     fill_missing_data)

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=load_data,
                inputs='raw_data',
                outputs='pivot_data',
                name='load_data_node'
            ),

            node(
                func=fill_missing_dates,
                inputs='pivot_data',
                outputs='complete_dates',
                name='fill_missing_dates_node'
            ),

            node(
                func=handle_outliers,
                inputs='complete_dates',
                outputs='no_outliers',
                name='handle_outliers_node'
            ),

            node(
                func=fill_missing_data,
                inputs='no_outliers',
                outputs='preprocessed_data',
                name='fill_missing_data_node'
            ),
        ]
    )