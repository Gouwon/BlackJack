
#### 해당 프로그래밍은 자바 공부를 목적으로 만든 간략화된 블랙잭 게임입니다.

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

### class Card
카드들은 이름과 점수를 가지고 있는 카드 타입의 객체로 만든다.
카드들은 그 이후, 카드 한 벌을 만든다.

### interface Deck
Deck 인터페이스는 카드 클래스에서 만들어지는 카드 한 벌을 받아서, 셔플하고, 나눠주는 함수를 선언한다.

### class GameRule implements Deck
게임의 진행과 관련하여 필요한 메소드와 객체들을 생성하여 준비한다.
이 곳에는 각 플레이어의 점수를 비교하는 compare(), 사용자의 입력을 받는 ```userInput()```을 선언 및 구현한다.
또한, Deck 인터페이스에서 선언된 ```getDeck()```, , 카드를 분배하는 ```dispenseCard()```의 구현체를 가진다.
마지막으로 게임의 진행 순서를 구현한 ```game()``` 메서드를 선언 및 구현한다.

### abstract class Player
Player는 Dealer와 Gamer의 부모클래스로서, 기본적인 변수와 메서드를 선언 및 구현한다.
자식클래스에서의 공통으로 사용할 수 있는 메서드는 바로 선언 및 구현화하고, 구현체가 달라야 하는 것은 상속받아서 ```override```한다.

### class Dealer extends Player
Dealer는 Player의 자식 클래스이다. 
다만, Dealer는 형제인 Gamer와 다르게 자신의 패를 전부 보여주는 것은 아니기 때문에, bluff 패를 변수로 가진다.

### class Gamer extends Player
Gamer는 Player의 자식 클래스이다. 
추상 클래스인 Player의 abstract 메서드를 구현한다.

### class Main
실제 Main에서는 GameRule의 game() 메서드를 불러서 게임을 진행한다.
여기서는 
