import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ListeMots {
	
public static void main (String args[]) throws IOException {
		

		if(args.length!=1) {
			System.out.println("Erreur: il faut indiquer le chemin ou le nom d'un fichier");
		}


		try (
				//Lecture du fichier
				BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
			StringBuilder build = new StringBuilder();
			String ligne;
			
			//Lecture d'une ligne 
		   while ((ligne = reader.readLine()) != null) {
				build.append(ligne + " ");
				
			}
           
			String contenuFichier = build.toString();
			
			//Permet d'avoir toutes les lettres de la chaine de caractères en minuscules
			String minuscules=contenuFichier.toLowerCase();
			
			
			//On a supprimé les retour à la ligne simple, les espaces et les tabultations mais pas les saut de ligne
			String[] tab = minuscules.split("[ \n\t]");
		
			//Utilisation des stream
			
			List<String> liste = List.of(tab);
		
			//Permet d'avoir la liste des mots supprimés de tous les sauts de lignes (different de retour à la ligne)
			
	        List<String> mots = liste.stream()
	        		
                    .filter(x -> x!="")
                    
                    .collect(Collectors.toList());
	        
	        //Permet d'avoir une nouvelle liste qui contient une et une seule occurence de chacune des mots de la liste de mots
	        
	        List<String> motsDistincts= mots.stream()
	        .distinct()
            .collect(Collectors.toList());

	        //Affichage 
	        Stream.of(motsDistincts)
			.flatMap( Collection::stream )
			.forEach(System.out::println);
					
		
		} catch (FileNotFoundException e) {
			System.err.println("Le fichier " + args[0] + " n'existe pas.");
			System.exit(2);}
}

}
