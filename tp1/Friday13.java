

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.Month;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
/**
 * 
 * @author Mickael MOHAMMED 51804780 M1 Cybersecurite FI
 *
 */
 

public class Friday13 {

	/**
	 * @param year L'annee pour laquelle on veut tous les mois contenant un vendredi 13
	 * @return Une liste de mois dont chacun contient un vendredi 13
	 */
	  public static List<Month> getMonths(int year) {
		  
	    	 List<Month> months=new ArrayList<Month>();
	    	  
	    	 for(int i=1;i<=12;i++) {
	    		 LocalDate date=LocalDate.of(year,Month.of(i),13);
	    		 DayOfWeek jour=date.getDayOfWeek();
	    		 
	    		 //On verifie si le jour 13 du mois correpond a un vendredi
	    		 // Si c est le cas alors on l'ajoute a notre liste de mois contenant chacun un vendredi 13
	    		 
	    		 if(jour.equals(java.time.DayOfWeek.FRIDAY)){
	    			 Month mois=date.getMonth();
	    			 months.add(mois);
	    		 }
	    	 }
	    	 
	    	 return months;
	    	 
	     }
	  
	 
	/**
	 * 
	 * @param months Prend en parametre une liste de mois 
	 * affiche la liste de mois conformement a la syntaxe indiquee dans l'enonce
	 */
	  public static void DisplayMonths(List<Month> months) {
    	  for(int i=0;i<months.size();i++) {
    	         System.out.println(months.get(i));
    	  }
      }
	  
	  /**
	   * Methode principale 
	   * @param args
	   */
	public static void main(String[] args) {	
		
	  	List<Month> months=new ArrayList<Month>();
		int year1;
		if(args[0].equals("-y")) {
			year1=Integer.parseInt(args[1]);
		}
		else {
		 year1=Integer.parseInt(args[0]);
		}
		months=getMonths(year1);
	    DisplayMonths(months);
		
	}
}
