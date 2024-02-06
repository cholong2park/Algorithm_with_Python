"""
N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다. 이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한
화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다. 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한으
화폐 개수이다.
- 입력 조건
    - 첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10000)
    - 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10000보다 작거나 같은 자연수이다.
- 출력 조건
    - 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
    - 불가능할 때는 -1을 출력한다.
"""