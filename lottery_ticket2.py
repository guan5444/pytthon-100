import random
from rich.console import Console
from rich.table import Table

# 创建控制台
console = Console()

n = int(input('生成几组号码：'))
red_balls = [i for i in range(1, 34)]
blue_ball_pool = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('num', 'red', 'blue'):
    table.add_column(col_name, justify='center')


for i in range(n):
    select_balls = random.sample(red_balls, 6)
    select_balls.sort()
    blue_ball = random.choice(blue_ball_pool)
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in select_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)