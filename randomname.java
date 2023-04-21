package to.msn.wings.selflearn.chap01;

import java.util.Random;
import java.util.Scanner;

public class randomname {
	public static void main(String[] args) {
        // 配列を定義する
        String[] array = {"佐藤","鈴木","高橋","田中","渡辺","伊藤","中村","小林","山本","加藤"};
        String[] array2 = {"ハルト","アオト","リク","ミナト","ハルキ","エマ","メイ","サナ","ミオ","イチカ"};

        Random random = new Random();
        	
        Scanner scanner = new Scanner(System.in);
        System.out.print("名前を作りますか？: ");
        String reply = scanner.nextLine();
        
        if(reply.equals("yes")) {

            String firstname = array[random.nextInt(array.length)];
            String lastname = array2[random.nextInt(array2.length)];
            System.out.println("あなたの名前は" + firstname + lastname);
        	}
        else if(reply.equals("no")) {
        	System.out.println("またお待ちしております");
      		
        }
        
       
    }

}
