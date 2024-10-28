

import java.util.*;
import java.time.*;

import java.util.Date;
import java.util.Locale;
/**
 * 
 * @author mickael mohammed 51804780
 * M1 Cyber FI
 *
 */
 
public class Paye {

	/**
	 * Methode qui permet a partir d'une annee entree en parametre de la fonction de retourner une liste d'objets
	 * de type LocalDate avec chacune des dates correpondant au 25eme jour du mois sauf s'il s'agit d'un samedi 
	 * auquel cas il s'agit alors du 24eme jour du mois, ou s'il s'agit d'un dimanche auquel cas il s'agit ici 
	 * du 23eme jour du mois
	 *  
	 * @param year 
	 * @return une liste d'elements de type LocalDate
	 */
	public static List<LocalDate> getDates(int year){
		
		List<LocalDate> dates=new ArrayList<LocalDate>();
		
		for(int i=1;i<=12;i++) {
			LocalDate date=LocalDate.of(year, Month.of(i), 25);
			 DayOfWeek jour=date.getDayOfWeek();
			 if(jour.equals(java.time.DayOfWeek.SATURDAY))  {
				 
				 //Si le jour 25 du mois est un samedi alors le vendredi de la meme semaine est un vendredi 24
				 date=LocalDate.of(year, Month.of(i),24);
				 dates.add(date);
				 
			 }else if(jour.equals(java.time.DayOfWeek.SUNDAY)){
				 
				 //Si le jour 25 du mois est un dimanche alors le vendredi de la meme semaine est un vendredi 23
				 date=LocalDate.of(year, Month.of(i), 23);
				 dates.add(date);
				 
			 }else {
				 dates.add(date);
			 }
				
			
		}
		return dates;
		
	}
	
	/**
	 * 
	 * @param dates Prend en entree un tableau d'objets de type LocalDate
	 *Affiche une liste de dates conforme a la syntaxe specifie dans l'enonce 
	 *
	 */
	public static void DisplayDates(List<LocalDate> dates) {
		
		List<String> DisplayDates=new ArrayList<String>();
		
		int year=dates.get(0).getYear();
		String date="";
		
		//Pour toutes les dates du tableau dates on construit un String date conforme a la syntaxe de l'enonce
		for(int i=0;i<=11;i++) {
			Month month=dates.get(i).getMonth();
			int day=dates.get(i).getDayOfMonth();
			date=day+" "+month+" "+year;
			DisplayDates.add(date);
		}
		
		//Affichage des dates
		for(int j=0;j<=11;j++) {
			System.out.println(DisplayDates.get(j));
		}
		
	}
	
	public static void main(String[] args) {
		int year;
		if(args[0].equals("-y"))
		year=Integer.parseInt(args[1]);
		else
			year=Integer.parseInt(args[0]);
		Scanner sc=new Scanner(System.in);
		
		
		
		List<LocalDate> dates=new ArrayList<LocalDate>();
		dates=getDates(year);
		DisplayDates(dates);
		
	}
}
