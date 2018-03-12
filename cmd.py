import click
from chrome.bookmark import Bookmark

@click.group()
def cmd():
    pass

@cmd.command(help="list bookmark")
def bookmark():
    bookmark = Bookmark()
    


@cmd.command(help="list history")
def history():
    pass

def main():
    cmd()


if __name__ == "__main__":
    main()