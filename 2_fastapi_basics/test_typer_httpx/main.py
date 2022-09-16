from pathlib import Path
from typing import Optional
from rich.table import Table
from rich.console import Console
import typer
import json
import asyncio
import httpx

app = typer.Typer()
console = Console()

async def post_product(client, url: str, req_body) -> None:
    await client.post(url, data=json.dumps(req_body, indent = 4) )

async def read_data(file_addr:str, url:str):
    tasks = list()
    with open(file_addr) as file:
        async with httpx.AsyncClient() as client:
            data = json.load(file)
            for product in data:
                p = {
                        "name":product["name"],
                        "price": product["basePrice"]
                        }
                print(p)
                tasks.append(asyncio.create_task(post_product(client, url, p)))

            await asyncio.gather(*tasks)

@app.command()
def initial_data(file_addr: str, url: str = "http://127.0.0.1:8000"):
    asyncio.run(read_data(file_addr, url))
      
 
@app.command()
def main(config: Optional[Path] = typer.Option(None)):
    """
    Examples: \n
    1- python main.py --help \n
    2- python main.py data.json \n
    3- python main.py --config ../../data.json
    """
    if config is None:
        print("No config file")
        raise typer.Abort()
    if config.is_file():
        text = config.read_text()
        products_dict = json.loads(text)
        #typer.echo(products_dict)
        table  = Table(title="Products")
        table.add_column("Id", style="magenta", no_wrap=True)
        table.add_column("Price", style="green")
        table.add_column("DiscountedPrice", style="red")
        table.add_column("Title",justify="right",  style="cyan")
        for p in products_dict:
            #table.add_row(title=p["name"], price=p["basePrice"])
            table.add_row(p["_id"], f'${p["basePrice"]}', f'${p["discountedPrice"]}', p["name"])
        console.print(table)
    elif config.is_dir():
        print("Config is a directory, will use all its config files")
    elif not config.exists():
        print("The config doesn't exist")


if __name__ == "__main__":
    #typer.run(main)
    asyncio.run(app())

