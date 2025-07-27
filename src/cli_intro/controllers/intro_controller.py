"""CLI 출력 동작을 담당하는 컨트롤러."""


from rich.console import Console
from rich.table import Table
import pyfiglet

from ..models.profile import Profile

console = Console()


def display_banner(text: str) -> None:
    """pyfiglet를 이용해 배너를 출력합니다."""
    ascii_art = pyfiglet.figlet_format(text, font="slant")
    console.print(ascii_art, style="bold cyan")


def show_profile(profile: Profile, details: bool = False) -> None:
    """프로필 정보를 보기 좋게 출력합니다."""
    console.print(f"안녕하세요, {profile.title} {profile.name}입니다!", style="bold green")
    if details:
        table = Table(title="연락처")
        table.add_column("항목", style="cyan")
        table.add_column("내용", style="magenta")
        table.add_row("Email", profile.email)
        console.print(table)
