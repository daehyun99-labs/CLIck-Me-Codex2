"""프로필 정보 모델 모듈."""

from dataclasses import dataclass


@dataclass
class Profile:
    """개발자 프로필 정보를 담는 데이터 클래스."""

    name: str
    email: str
    title: str
