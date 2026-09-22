import java.util.Scanner;
import java.util.ArrayList; 

public class main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Anime Finder");

        System.out.print("Enter an anime: ");
        String anime = scan.nextLine();
        System.out.println("You entered: " + anime);

        Anime naruto = new Anime("Naruto", "Action", 220, 8.0);
        Anime bleach = new Anime("Bleach", "Action", 366, 8.2);
        Anime onePiece = new Anime("One Piece", "Adventure", 1150, 9.0);
        Anime AttackonTitan = new Anime("Attack on Titan", "Action", 87, 9.1);
        Anime DeathNote = new Anime("Death Note", "Thriller", 37, 8.6);
        Anime JujutsuKaisen = new Anime("Jujutsu Kaisen", "Action", 47, 8.6);

        ArrayList<Anime> animeDatabase = new ArrayList<Anime>();
        animeDatabase.add(naruto);
        animeDatabase.add(bleach);
        animeDatabase.add(onePiece);
        animeDatabase.add(AttackonTitan);
        animeDatabase.add(DeathNote);
        animeDatabase.add(JujutsuKaisen);

        boolean found = false; 

        for (int i = 0; i < animeDatabase.size(); i++) 
        {
            if(anime.equalsIgnoreCase(animeDatabase.get(i).name))
            {
                System.out.println("Anime: " + animeDatabase.get(i).name);
                System.out.println("Genre: " + animeDatabase.get(i).genre);
                System.out.println("Episodes: " + animeDatabase.get(i).episodes);
                System.out.println("Rating: " + animeDatabase.get(i).rating);
                found = true;
            }
            
        }
        if(!found)
        {
            System.out.println("Anime Not Found");
        }
        
    }
    
}

