
#### 해당 프로그래밍은 파이썬 공부를 목적으로 만든 간략화된 블랙잭 게임입니다.

## Rules

블랙잭 게임은 다음과 같이 간략화한 규칙에 따라서 진행되는 것으로 가정합니다.

 - Dealer(Computer) & Player
 - 총 13 * 4 개 카드(Spade, Diamond, Heart, Clover)
 - J, Q, K는 모두 10 으로 계산.
 - A 카드는 1 또는 11 선택 가능.
 - 21에 가까운 사람이 승리 (단, 21 초과시 패)
 - Dealer(Computer)는 17보다 작을 경우만 카드 추가됨.
 - Player는 본인 의지대로 카드 추가 및 중지 가능.
## 프로그램 개발 방향

블랙잭은 다음과 같이 구성한다.

### Person.py
Player와 Dealer의 부모 클래스인 Person class를 만든다. 
Person class는 기본적인 멤버변수와 메서드를 가진다.
Player와 Dealer는 Person class를 상속받아서 필요한 메서드를 추가하거나, override한다.

### Gameplay.py
Gameplay에서는 블랙젝 게임을 진행하는 데 필요한 것들을 만든다.
카드를 만드는 ```card()```, 처음에 Player와 Dealer에게 2장의 카드를 주는 ```give_2card()```, Player와 Dealer의 점수를 비교하는 ```outcome()```, 게임을 진행여부를 묻는 ```close_game()```을 구현한다.

### Game.py
Game에서는 

