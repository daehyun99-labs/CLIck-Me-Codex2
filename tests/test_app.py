"""`cli_intro` 애플리케이션 테스트."""

import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from click.testing import CliRunner

from cli_intro.app import main


def test_main_success(monkeypatch):
    monkeypatch.setenv("DEV_NAME", "테스트")
    monkeypatch.setenv("DEV_EMAIL", "test@example.com")
    monkeypatch.setenv("DEV_TITLE", "개발자")

    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "테스트" in result.output


def test_main_missing_profile(monkeypatch):
    monkeypatch.delenv("DEV_NAME", raising=False)
    monkeypatch.delenv("DEV_EMAIL", raising=False)
    monkeypatch.delenv("DEV_TITLE", raising=False)

    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code != 0
    assert "프로필 정보" in result.output


def test_main_load_from_env_file(monkeypatch):
    env_path = pathlib.Path(__file__).resolve().parents[1] / "config" / ".env"
    env_content = "\n".join([
        "DEV_NAME=파일",
        "DEV_EMAIL=file@example.com",
        "DEV_TITLE=파일 개발자",
    ])
    env_path.write_text(env_content)
    try:
        monkeypatch.delenv("DEV_NAME", raising=False)
        monkeypatch.delenv("DEV_EMAIL", raising=False)
        monkeypatch.delenv("DEV_TITLE", raising=False)

        runner = CliRunner()
        result = runner.invoke(main)
        assert result.exit_code == 0
        assert "파일" in result.output
    finally:
        env_path.unlink(missing_ok=True)
