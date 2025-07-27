# CLIck-Me-Codex2

이 프로젝트는 `click`, `rich`, `pyfiglet`을 이용하여 CLI 환경에서 개발자가 본인을 소개할 수 있는 간단한 프로그램입니다.

## 설치 방법
1. [Rye](https://github.com/astral-sh/rye)를 설치합니다.
2. 의존성을 설치합니다.
   ```bash
   rye sync
   ```

환경 변수는 `config/.env.example` 파일을 참고하여 설정합니다.

## 사용법
```bash
rye run intro --details
```
`--details` 옵션을 주면 연락처 정보가 함께 출력됩니다.

## 테스트 실행
```bash
rye run pytest
```
