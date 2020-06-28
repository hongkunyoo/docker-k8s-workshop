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

## 클라우드 계정 만들기

준비한 서버가 없다면 다음 클라우드 플랫폼을 이용하여 무료로 서버를 생성하시기 바랍니다.

- `GCP`: https://cloud.google.com/free/
- `AWS`: https://aws.amazon.com/ko/s/dm/landing-page/start-your-free-trial/
- `Azure`: https://azure.microsoft.com/ko-kr/free

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

## 참고자료

### Demo 클러스터
- [Play with k8s](https://labs.play-with-k8s.com/)
- [Playground](https://www.katacoda.com/courses/kubernetes/playground)

### Examples & Tutorials
- [쿠버네티스 공식 튜토리얼](https://kubernetes.io/docs/tutorials/)
- [쿠버네티스 example](https://kubernetesbyexample.com/)

### Books
- [The Kubernetes Book](https://www.amazon.com/Kubernetes-Book-Version-January-2018-ebook/dp/B072TS9ZQZ/ref=sr_1_3?ie=UTF8&qid=1528625195&sr=8-3&keywords=kubernetes&dpID=41SyKBO3UcL&preST=_SX342_QL70_&dpSrc=srch)
- [Designing Distributed System](https://azure.microsoft.com/en-us/resources/designing-distributed-systems/en-us/)

### 읽을거리
- [쿠버네티스란 무엇인가](https://subicura.com/2019/05/19/kubernetes-basic-1.html)
- [쿠버네티스 관련 Blog: coffeewhale.com](https://coffeewhale.com)