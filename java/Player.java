package blackjack;

import java.util.ArrayList;
import java.util.Iterator;

public abstract class Player {
	String name;
	ArrayList<Card> hand = new ArrayList<Card>();
	int point = 0;
	boolean isHit = true;

	public static final String[] aces = { "CA", "DA", "HA", "SA" };

	public Player() {

	}

	public Player(String name) {
		this.name = name;
	}
	
	public abstract void hasAce() ;

	public int howAces() {
		int result = 0;
		for (Card card : this.hand) {
			switch (card.name) {
			case "CA":
				result++;
				continue;
			case "DA":
				result++;
				continue;
			case "HA":
				result++;
				continue;
			case "SA":
				result++;
				continue;
			default:
				continue;
			}
		}

		return result;
	}

	protected void sum() {
		Iterator<Card> itr = this.hand.iterator();
		this.point = 0;
		
		while (itr.hasNext()) {
			Card card = itr.next();
			this.point += card.point;
		}
	}

	public abstract void isStay();

	public ArrayList<Card> getHand() {
		return this.hand;
	}

	public void setHand(Card card) {
		this.hand.add(card);
	}

	@Override
	public String toString() {
		return this.name + "님";
	}

	protected void check() {
		sum();
		if(this.point > 21) {
			System.out.println(this + " Busted!!");
			this.isHit = false;
		}
		else if(this.point == 21) {
			System.out.println(this + " BlackJack!!");
			this.isHit = false;
		}
	};
	
	public abstract void showHand();	

		
}
