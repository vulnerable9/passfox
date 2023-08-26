import secrets
from rich import print

print(f"""[bold cyan]
  /\_/\\
 ( o.o ) PassFox
  > ^ <
      [/bold cyan]""")

for i in range(5):
    password = secrets.token_urlsafe()
    print(f"• [bright_magenta]{password}[/bright_magenta]")
