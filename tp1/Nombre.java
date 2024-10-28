
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Calendar;
import java.util.*;

/**
 * 
 * @author Mickael MOHAMMED 51804780 M1 Cybersecurite FI
 *
 */
 
public class Nombre {

	/**
	 * L'idee de la methode est de parser la date : recuperer a partir d'un string , un entier l'annee , le mois en numero et le jour en int
	 * 
	 * @param date la date 
	 * @param lang la langue
	 * @return un objet date de type LocalDate utile pour effectuer la soustraction de 2 dates liees au package java.time
	 */

	
	public static LocalDate parsingDate(String date,String lang) {
		//On considere que sur la ligne de commande les arguments date et la langue sont separees par un espace
		
		
		String year; 
		StringBuilder build=new StringBuilder();
		
		//L annee dans la date est constituee de 4 caracteres au debut donc comprise entre les indices 0 et 4 de la chaine date
		for(int i=0;i<=3;i++) {
		      build.append(date.charAt(i));    
		}
		year=build.toString();
		

		int year1=Integer.parseInt(year); // L annee est convertir en entier pour l'utiliser

		//Le mois est situe apres le 1er tiret qui suit l'annee et donc la 1ere lettre du mois est a la postion 5 dans la chaine date
		String Month1;
		StringBuilder build2=new StringBuilder();
		int j=5; // Postion de la 1ere lettre du mois
		while(date.charAt(j)!='-') {
		
			build2.append(date.charAt(j));
			j++;
		}
		Month1=build2.toString();
		
	
		
		StringBuilder build3=new StringBuilder();
          
		//Recuperation du jour sous forme de string (on le recupere apres le dernier tiret)
		for(int k=j+1;k<j+3;k++) {
		        build3.append(date.charAt(k)); 
			
		}
		
		String day=build3.toString();
		
		//Conversion de la chaine jour en entier
		int day1=Integer.parseInt(day);
		

	    //On va creer ici une liste de tous les mois de l'annee dont la langue est celle donnee en ligne de commande
		 List<String> months=new ArrayList<String>();
		 for(int i=1;i<=12;i++) {
		    	LocalDate date1=LocalDate.of(year1, Month.of(i), 1); 
		    	DateTimeFormatter traduction = DateTimeFormatter.ofPattern("MMMM", new Locale(lang));
		    	
		    		 String monthTraduct=traduction.format(date1);
		    	months.add(monthTraduct);	 
		    	
			 }
		 
		
		 
		 //On verifie enfin si le mois entree en ligne de commande est bien dans la liste pour recuperer ce mois sous forme d'objet Month 
	      int monthNumber=0;	 
		 for(int k=0;k<=11;k++) {
			if(Month1.equals(months.get(k))){
					monthNumber=k+1;
					}
		 }
		 
		 //Creation d'un objet LocalDate date
		 LocalDate localDate=LocalDate.of(year1, monthNumber, day1);
	
		 
		return localDate;
		
	}
	
	
	
	public static void main(String[] args) {
			//2021 fev 1
		//     2020 dec 25
	//On suppose dans ce programme que l'utilisateur aura entre correctement les dates selon le format yyyy-MMMM-dd
     //-d1 date1 -d2 date2 [-l] locale]
		
		//On va creer deux objets Localdate date sur les 2 dates en entree pour utiliser les methodes de java.time

LocalDate d1=null;
LocalDate d2=null;
if(args.length==6) {
	
	
	//si on entre la commande de type -d1 date1 -d2 date2 -l langue
d1=parsingDate(args[1],args[5]);

		 d2=parsingDate(args[3],args[5]);

}

//si on entre la commande de type -d1 date1 -d2 date2  langue
else if(args.length==5) {
	d1=parsingDate(args[1],args[4]);

	 d2=parsingDate(args[3],args[4]);
}

//La langue par defaut est fr
else if(args.length==4) {
	d1=parsingDate(args[1],"fr");

	 d2=parsingDate(args[3],"fr");
}

//si on entre la commande de type -d1 date1 -d2 date2 

	int diffYear=d2.getYear()-d1.getYear();
	
	
	int diffMonth;  //indique la difference en mois entre les deux dates
	diffMonth=d2.getMonthValue()-d1.getMonthValue();
	
	if(diffMonth<0) {
		// Si le mois de la date 1 est plus grand que le mois de la date 2 alors on decremente le nombre d'annees 
		diffYear--;
		diffMonth=-(diffMonth);// valeur absolue du mois 
	}
	
	int DaysToEnd; //Indique le nombre de jour avant la fin du mois de la date 1
	int monthSize; //indique le nombre de jour dans un mois donnee
	
	boolean bissextile=false; //indique si l'annee de la date 1 est bissextile ou non
	
	//On verifie si le mois de la date 1 est egale a un des mois contenant 31 jours

     if((d1.getMonthValue()==1) || (d1.getMonthValue()==3) || (d1.getMonthValue()==5) ||(d1.getMonthValue()==7) ||(d1.getMonthValue()==8) ||(d1.getMonthValue()==10) || (d1.getMonthValue()==12))
            monthSize=31;
     //9 11 6 4
     
     //On verifie si le mois de la date 1 est egale a un des mois contenant 30 jours
     else if((d1.getMonthValue()==4) || (d1.getMonthValue()==6) || (d1.getMonthValue()==9) || (d1.getMonthValue()==11))
    	 monthSize=30;
     
     //On verifie si on a une annee bissexitile si le mois de la date 1 est le fevrier	
     // la condition ((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0)) permet de verifier si l annee de la date 2 est bien bissextile 
     else if((d1.getMonthValue()==2) && (((d1.getYear()%4 == 0) && (d1.getYear()%100 != 0) || (d1.getYear()%400 == 0)))) {
    	 bissextile=true;
    	 monthSize=29; //si annee bissextile alors la taille du mois est 29 jours sinon 28
     }else {
    	 monthSize=28;
     }
    	DaysToEnd=monthSize-d1.getDayOfMonth(); 
    	
    
    	int sumDays=d2.getDayOfMonth(); //sumDays indiquera le nombre de jours totale entre les deux dates
    	sumDays+=DaysToEnd;
    	// Pour les mois de la date 1 on compte le nombre de jours contenu dans chacun de ses mois jusqu a arriver a la difference des deux mois des deux dates
    	
    	for(int i=1;i<diffMonth;i++) {
    		if((d1.getMonthValue()+i==1) || (d1.getMonthValue()+i==3) || (d1.getMonthValue()+i==5) ||(d1.getMonthValue()+i==7) ||(d1.getMonthValue()+i==8) ||(d1.getMonthValue()+i==10) || (d1.getMonthValue()+i==12)) {
    			sumDays+=31;
    		}
    		else if((d1.getMonthValue()+i==4) || (d1.getMonthValue()+i==6) || (d1.getMonthValue()+i==9) || (d1.getMonthValue()+i==11)) {
    			sumDays+=30;
    		}
    		else if((d1.getMonthValue()==2) && (((d1.getYear()%4 == 0) && (d1.getYear()%100 != 0) || (d1.getYear()%400 == 0)))) {
    			bissextile=true;
    			sumDays+=29;
    		}else {
    			sumDays+=28;
    		}
    	}
    	//indique le nombre d annees bissextiles
    	int cptBissextiles;
    	if(bissextile==true)
    	      cptBissextiles=1;
    	//On verifie si pour les annees comprises entre les deux dates et differentes des annees des deux dates si elles sont ou non bissextiles
    	else cptBissextiles=0;
    	//compter le nombre d annees entre les deux dates qui sont bissextiles ou non
    	for(int i=0;i<=diffYear;i++) {
    		int year=d1.getYear()+i;
    		if((year%4==0) && (year%100!=0) || (year%400==0))
    			cptBissextiles++;
    		
    	}
    	
    	int nbAnneesNormal=diffYear-cptBissextiles;//nombres d'annees non bissextiles
    	
    	//nombre de jours totale pour les annees bissextiles
    	int daysBissextiles=366*cptBissextiles;
    	
    	//nombre de jours totale pour les annnes non bissextiles
    	int normalDays=365*nbAnneesNormal;
    	
    	
    	sumDays+=daysBissextiles;
    	sumDays+=normalDays;
    	
    	//affichage du nombre de jours totale 
    System.out.println(sumDays);
 
    
    
       
	}
}

	
