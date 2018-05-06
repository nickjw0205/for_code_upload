public class SynchronizedEx {
	public static void main(String[] args) {
		SharedPrinter p = new SharedPrinter(); // °øÀ¯ µ¥ÀÌÅÍ »ý¼º
		String [] engText = { "Wise men say, ",
							  "only fools rush in", 
							  "But I can't help, ",
							  "falling in love with you", 
							  "Shall I stay? ",
							  "Would it be a sin?", 
							  "If I can't help, ",
							  "falling in love with you" };
		String [] korText = { "µ¿ÇØ¹°°ú ¹éµÎ»êÀÌ ¸¶¸£°í ´âµµ·Ï, ",
							  "ÇÏ´À´ÔÀÌ º¸¿ìÇÏ»ç ¿ì¸® ³ª¶ó ¸¸¼¼",
							  "¹«±ÃÈ­ »ïÃµ¸® È­·Á°­»ê, ",
							  "´ëÇÑ »ç¶÷ ´ëÇÑÀ¸·Î ±æÀÌ º¸ÀüÇÏ¼¼",
							  "³²»ê À§¿¡ Àú ¼Ò³ª¹«, Ã¶°©À» µÎ¸¥ µí",
							  "¹Ù¶÷¼­¸® ºÒº¯ÇÔÀº ¿ì¸® ±â»óÀÏ¼¼.", 
							  "¹«±ÃÈ­ »ïÃµ¸® È­·Á°­»ê, ",
							  "´ëÇÑ »ç¶÷ ´ëÇÑÀ¸·Î ±æÀÌ º¸ÀüÇÏ¼¼" }; 	
		// ½º·¹µå »ý¼º½Ã °øÀ¯ ÇÁ¸°ÅÍÀÇ ÁÖ¼Ò¸¦ ¾Ë·ÁÁØ´Ù. µÎ ½º·¹µå´Â °øÀ¯ ÇÁ¸°ÅÍ p¿¡ µ¿½Ã¿¡ Á¢±ÙÇÑ´Ù.		
		Thread th1 = new WorkerThread(p, engText); // ¿µ¹® Ãâ·Â ½º·¹µå
		Thread th2 = new WorkerThread(p, korText); // ±¹¹® Ãâ·Â ½º·¹µå

		// µÎ ½º·¹µå¸¦ ½ÇÇà½ÃÅ²´Ù.
		th1.start(); th2.start();
	}
}

class SharedPrinter { // µÎ WorkerThread ½º·¹µå¿¡ ÀÇÇØ µ¿½Ã Á¢±ÙµÇ´Â °øÀ¯ ÇÁ¸°ÅÍ
	// synchronized¸¦ »ý·«ÇÏ¸é ÇÑ±Û°ú ¿µ¾î°¡ ÇÑ ÁÙ¿¡ ¼¯¿© Ãâ·ÂµÇ´Â °æ¿ì°¡ ¹ß»ýÇÑ´Ù. 	
	synchronized void print(String text) {
		// Thread.yield();
		for(int i=0; i<text.length(); i++)
			System.out.print(text.charAt(i));
		System.out.println();
	}
}

class WorkerThread extends Thread { //½º·¹µå Å¬·¡½º 
	SharedPrinter p; // °øÀ¯ ÇÁ¸°ÅÍ ÁÖ¼Ò
	String [] text;

	WorkerThread(SharedPrinter p, String[] text) { // °øÀ¯ ÇÁ¸°ÅÍ ÁÖ¼Ò¿Í ÅØ½ºÆ® Àü´Þ ¹ÞÀ½
		this.p = p; this.text = text;
	}
	
	public void run() { // ½º·¹µå´Â ¹Ýº¹ÀûÀ¸·Î °øÀ¯ ÇÁ¸°ÅÍ¿¡ 10¹ø Á¢±ÙÇÏ¿© text[]¸¦ Ãâ·ÂÇÑ´Ù.
		for (int i=0; i<text.length; i++) // ÇÑ ÁÙ¾¿ Ãâ·Â
			p.print(text[i]); // °øÀ¯ ÇÁ¸°ÅÍ¿¡ Ãâ·Â
	}
}