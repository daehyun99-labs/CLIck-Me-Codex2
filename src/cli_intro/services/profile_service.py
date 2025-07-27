"""프로필 정보를 환경 변수에서 로드하는 서비스."""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from ..models.profile import Profile


def load_profile() -> Optional[Profile]:
    """환경 변수에서 프로필 정보를 읽어 :class:`Profile` 객체를 반환합니다."""
    env_path = Path(__file__).resolve().parents[2].parent / "config" / ".env"
    load_dotenv(env_path)

    name = os.getenv("DEV_NAME")
    email = os.getenv("DEV_EMAIL")
    title = os.getenv("DEV_TITLE")

    if not all([name, email, title]):
        return None
    return Profile(name=name, email=email, title=title)
