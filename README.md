# 도커 쿠버네티스 워크샵

## 실습환경

- OS: ubuntu 18.04
- root user (sudo)
- CPU 2 core / MEM 4G / Disk 50G
- Public IP 권장 (EC2 / GCE / Azure VM)

## 사전지식
- 리눅스 기본 지식이 필요합니다. (ssh, vim, apt, curl 등)
- 간단한 프로그래밍 지식을 요구합니다. 언어는 무관하지만 이 책에서는 파이썬을 주로 다룹니다. 파이썬을 모르시더라도 전반적인 프로그래밍 지식만으로도 충분히 이해할 수 있습니다.
- 간단한 클라우드 지식이 필요합니다.
- `tmux`, `screen`과 같은 터미널 멀티플랙서를 사용하면 편리합니다.


## 도커

1. [도커 실행](docker/01.md)
2. [도커 레지스트리](docker/02.md)
3. [Dockerfile 작성 및 빌드](docker/03.md)
4. [도커실행 고급](docker/04.md)
5. [docker-compose](docker/05.md)

## 쿠버네티스

1. [명령도구 마스터](k8s/01.md)
2. [Pod 살펴보기](k8s/02.md)
3. [네트워킹](k8s/03.md)
4. [쿠버네티스 리소스](k8s/04.md)


## 프로젝트 (Optional)

1. [Wordpress 서비스 만들기](project/01.md)
2. [ML 모델 학습 시키기](project/02.md)
