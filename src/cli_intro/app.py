"""CLI 진입점 모듈."""

import click

from .controllers.intro_controller import display_banner, show_profile
from .services.profile_service import load_profile
from .utils.logger import get_logger

logger = get_logger(__name__)


@click.command()
@click.option("--details", is_flag=True, help="세부 정보를 출력합니다.")
def main(details: bool) -> None:
    """개발자 소개 CLI 프로그램의 메인 함수."""
    profile = load_profile()
    if profile is None:
        logger.error("프로필 정보를 불러올 수 없습니다. 환경 변수를 확인하세요.")
        raise click.ClickException("프로필 정보가 없습니다.")

    display_banner(profile.name)
    show_profile(profile, details=details)


if __name__ == "__main__":
    main()
