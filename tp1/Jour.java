

import java.util.*;
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Locale;
import java.text.*;

class Jour {
	
	   
	       static LocalDate  date = LocalDate.of (2000, Month.JANUARY, 1);
	       	        
	/*
	 * Question 2)
	 * On veut afficher le resultat de la commande precedente en chinois et en allemend.
	 * Pour cela on fait appel a la methode ofPattern de la classe DateTimeFormatter
	 */
	         
    static DateTimeFormatter traductionJourSemaineAllemand = DateTimeFormatter.ofPattern("EEEE", Locale.GERMANY);
	static DateTimeFormatter traductionJourSemaineChinois = DateTimeFormatter.ofPattern("EEEE", Locale.CHINA);
          /*
           * Question 3)
           */
          
    public static String traductOfDate(int year1, String lang) {
    	
    	LocalDate date1=LocalDate.of(year1, Month.JANUARY, 1);
    	
    	DateTimeFormatter traduction = DateTimeFormatter.ofPattern("EEEE", new Locale(lang));
    	String jour=traduction.format(date1);
          System.out.println(jour);
    	return jour;
    }   
	
    public static void main(String[] args) {
    	
    	Scanner sc=new Scanner(System.in);	
    
	
	    // DayOfWeek jour1=java.time.DayOfWeek.SATURDAY.minus(2);
	  //    System.out.println(jour1);
	/* Question 1)
	 Affiche le jour de la semaine correpondant au 1er jour de l'annee 2000
	 A partir de la date en format numerique du 1er jour de l annee 2000 on recupere le jour de la semaine 
	 correpondant a cette date.
	 */
    	
    
    	System.out.println("Question 1"); System.out.println();
	System.out.println(date.getDayOfWeek());
	
	 System.out.println();
	
	System.out.println("Question 2 :"); System.out.println();
    System.out.println("La traduction du jour de la semaine en chinois est: "+traductionJourSemaineChinois.format(date));
    
    
    System.out.println("La traduction du jour de la semaine en allemand est: "+ traductionJourSemaineAllemand.format(date));
    System.out.println();
    
    
	System.out.println("Question 3 :"); System.out.println();
 
	
	String lang="";
    int year=0;
    
    //Si on a entre aucun argument en ligne de commande alors l'annee par defaut est l'annee courante et langue est la langue par defaut
	if(args.length==0) {
		year=java.time.LocalDate.now().getYear();
         lang="EN";
	}
    
    if(args.length==1) {
    	if(args[0].charAt(0)=='2') { //Le debut d'une annee commence par 2
    		//On considere qu'on a passe une annee
    		year=Integer.parseInt(args[0]);
    		lang="EN";
    	}
    	else {
    		//Sinon on considere que la 1er argument est une langue
		    year=java.time.LocalDate.now().getYear();
		    lang=args[0];
		}
	}
	else if(args.length==2) {
    	 if(args[0].equals("-l")) {
    		 //On a passee comme argument l'option -l suivie de la langue
    		 year=java.time.LocalDate.now().getYear();
    		 lang=args[1];
    	 }else if(args[1].equals("-y")) {
    		 //On a passee comme argument l option -y suivie d'une annee
    		 year=Integer.parseInt(args[1]);
    	 }else {
    		 //Sinon on a passe comme arguments l annee puis la langue
    		 year=Integer.parseInt(args[0]);
    		 lang=args[1];
    	 }
     }
     else if(args.length==4) {
    	//On considere que l'utilisateur a tape une commande de type:
    	 // -y annee -l langue
    	// L'annee est alors args[1] et la langue est args[3]
    	 
    	 year=Integer.parseInt(args[1]);
    	 lang=args[3];
    	 
    	 
    	 
     }
	
	traductOfDate(year,lang);
	}

	
	
}

	
