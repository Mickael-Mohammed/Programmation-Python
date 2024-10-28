import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.stream.Collectors;
import java.util.stream.Stream;
/*
 * 
 */

//MOHAMMED MICKAEL 51804780
public class CompteMots {
	
	//Indiquer le chemin du fichier en ligne de commande
	public static void main (String args[]) throws IOException {
		

		if(args.length!=1) {
			System.out.println("Erreur: il faut indiquer le chemin ou le nom d'un fichier");
		}
		try (
				BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
			StringBuilder build = new StringBuilder();
			String ligne;
			
		   while ((ligne = reader.readLine()) != null) {
				build.append(ligne + " ");
				
			}
            		
			String contenuFichier = build.toString();
			
			//On a supprimé les retour à la ligne simple, les espaces et les tabultations mais pas les saut de ligne
			String[] tab = contenuFichier.split("[ \n\t]");
		
			//Utilisation des stream
			
			List<String> liste = List.of(tab);
		
			//On supprime les sauts de ligne et on insère les mots restants dans la nouvelle liste
	        List<String> mots = liste.stream()
	        		
                    .filter(x -> x!="")
                    
                    .collect(Collectors.toList());
	        
	        System.out.println(mots.stream().count()+" mots");
					
		
		} catch (FileNotFoundException e) {
			System.err.println("Le fichier " + args[0] + " n'existe pas.");
			System.exit(2);
	}

	
	
	
}
}