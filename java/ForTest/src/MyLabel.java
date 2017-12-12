import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class MyLabel extends JLabel {
	int barSize = 0; // ¹ÙÀÇ Å©±â
	int maxBarSize;
	
	MyLabel(int maxBarSize) { 
		this.maxBarSize = maxBarSize;
	}
	
	public void paintComponent(Graphics g) {
		super.paintComponent(g); 
		g.setColor(Color.MAGENTA);
		int width = (int) (((double)(getWidth()))/maxBarSize*barSize);
		if(width==0) return; // Å©±â°¡ 0ÀÌ±â ¶§¹®¿¡ ¹Ù¸¦ ±×¸± ÇÊ¿ä ¾øÀ½
		g.fillRect(0, 0, width, this.getHeight());
	}
	
	synchronized void fill() {
		if(barSize == maxBarSize) {
			try {
				wait(); // ¹ÙÀÇ Å©±â°¡ ÃÖ´ëÀÌ¸é, ComsumerThread¿¡ ÀÇÇØ ¹ÙÀÇ Å©±â°¡ ÁÙ¾îµé ¶§±îÁö ´ë±â
			} catch (InterruptedException e) { return; }
		}
		barSize++;
		repaint(); // ¹Ù ´Ù½Ã ±×¸®±â
		notify(); // ±â´Ù¸®´Â ConsumerThread ½º·¹µå ±ú¿ì±â
	}
	synchronized void consume() {
		if(barSize == 0) {
			try {
				wait(); // ¹ÙÀÇ Å©±â°¡ 0ÀÌ¸é ¹ÙÀÇ Å©±â°¡ 0º¸´Ù Ä¿Áú¶§±îÁö ´ë±â
			} catch (InterruptedException e) { return; }
		}
		barSize--;
		repaint(); // ¹Ù ´Ù½Ã ±×¸®±â
		notify(); // ±â´Ù¸®´Â ÀÌº¥Æ® ½º·¹µå ±ú¿ì±â
	}	
}

class ConsumerThread extends Thread {
	MyLabel bar;
	
	ConsumerThread(MyLabel bar) {
		this.bar = bar;
	}
	public void run() {
		while(true) {
			try {
				sleep(100);
				bar.consume(); // 0.1ÃÊ¸¶´Ù ¹Ù¸¦ 1¾¿ ÁÙÀÎ´Ù.
			} catch (InterruptedException e) { return; }
		}
	}
}

public class TabAndThreadEx  extends JFrame {
	MyLabel bar = new MyLabel(100); // ¹ÙÀÇ ÃÖ´ë Å©±â¸¦ 100À¸·Î ¼³Á¤
	
	TabAndThreadEx(String title) {
		super(title);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container c = getContentPane();
		c.setLayout(null);
		bar.setBackground(Color.ORANGE);
		bar.setOpaque(true);
		bar.setLocation(20,  50);
		bar.setSize(300, 20); // 300x20 Å©±âÀÇ ¹Ù
		c.add(bar);
		
		// ÄÁÅÙÆ®ÆÒ¿¡ Å° ÀÌº¥Æ® ÇÚµé·¯ µî·Ï
		c.addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent e) {
				bar.fill(); // Å°¸¦ ´©¸¦¶§¸¶´Ù ¹Ù°¡ 1¾¿ Áõ°¡ÇÑ´Ù.
			}
		});
		setSize(350,200);
		setVisible(true);
		
		c.requestFocus(); // ÄÁÅÙÆ®ÆÒ¿¡°Ô Å° Ã³¸®±Ç ºÎ¿©
		ConsumerThread th = new ConsumerThread(bar); // ½º·¹µå »ý¼º
		th.start(); // ½º·¹µå ½ÃÀÛ
	}

	public static void main(String[] args) {
		new TabAndThreadEx("¾Æ¹«Å°³ª »¡¸® ´­·¯ ¹Ù Ã¤¿ì±â");
	}
}