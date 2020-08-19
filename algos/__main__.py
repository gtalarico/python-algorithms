"""
x
"""
import click
from . import sorting, problems, utils
from .renderer import ConsoleRenderer

sort_functions = dict(
    selection=sorting.Selection,
    bubble=sorting.Bubble,
    insertion=sorting.Insertion,
    merge=sorting.MergeSort,
)


@click.group()
def cli():
    pass


@cli.command(name="sort")
@click.argument("algorithm_name", type=click.Choice(sort_functions.keys()))
@click.option("--width", default=None, help="Width of animation", type=click.INT)
@click.option("--height", default=None, help="Height of animation", type=click.INT)
@click.option("--speed", default=None, help="Frame Speed", type=click.FLOAT)
def cmd_sort(algorithm_name, width, height, speed):
    """Render Sorting Algorithms"""
    SorterCls = sort_functions[algorithm_name]
    with ConsoleRenderer() as renderer:
        sorter = SorterCls(renderer=renderer, speed=speed)
        width = width or int(renderer.term.width / 2)
        height = height or int(renderer.term.height - 4)
        arr = utils.random_array(size=height, lower=1, upper=width)
        sorter.sort(arr)


@cli.command(name="brackets")
@click.argument("brackets", default="(({}))[](])", type=click.STRING)
@click.option("--width", default=None, help="Width of animation", type=click.INT)
@click.option("--height", default=None, help="Height of animation", type=click.INT)
@click.option("--speed", default=None, help="Frame Speed", type=click.FLOAT)
def cmd_brackets(brackets, width, height, speed):
    """Render Sorting Algorithms"""

    with ConsoleRenderer() as renderer:
        solver = problems.BalancedBracked(renderer=renderer, speed=speed)
        width = width or renderer.term.width / 2
        height = height or renderer.term.height - 4
        solver.run(brackets)


if __name__ == "__main__":
    cli()
