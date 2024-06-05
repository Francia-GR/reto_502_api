from kedro.pipeline import Pipeline, node
from kedro.io import DataCatalog
from kedro.runner.sequential_runner import SequentialRunner


# additional datasets you want to use
from kedro.datasets.pandas.csv_dataset import CSVDataSet
from kedro.datasets.pandas.parquet_dataset import ParquetDataSet

# the sequential runner is the simplest. It runs one node at a time.
runner = SequentialRunner()

# this is a super simple example pipeline
pipeline = Pipeline(
    [
        node(lambda: range(100), None, "range"),
        node(lambda x: [i ** 2 for i in x], "range", "range**2"),
        node(lambda x: [i for i in x if i > 5000], "range**2", "range>5k"),
        node(lambda x: x[:5], "range>5k", "range>5k-head"),
        node(lambda x: sum(x) / len(x), "range>5k", "range>5k-mean"),
    ]
)

# to get up and running, you can use an empty catalog
catalog = DataCatalog()

runner.run(pipeline, catalog)

'''from kedro.framework.context import KedroContext

def run_model():
    context = KedroContext(package_name='ts-forecasting-pipeline')
    my_pipeline = context.pipeline
    result = context.run(my_pipeline)

    print(result)
    print(type(result))

if __name__ == '__main__':
    run_model()

from kedro.framework.context import KedroContext
from kedro.config import ConfigLoader
from kedro.framework.hooks import get_hook_manager
from kedro.framework.context import KedroContextError

# Replace these with actual values
project_path = "/path/to/your/project"
package_name = "your_project_name"
env = "local"

try:
    config_loader = ConfigLoader(conf_source=f"{project_path}/conf/base")
    hook_manager = get_hook_manager()
    context = KedroContext(
        package_name=package_name,
        project_path=project_path,
        config_loader=config_loader,
        env=env,
        hook_manager=hook_manager
    )
except KedroContextError as exc:
    print(exc)
    context = None

if context:
    # Access the pipeline
    my_pipeline = context.pipeline

    # Run the pipeline
    context.run(my_pipeline)
    '''
