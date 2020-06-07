public class Magic8 {
  public static void main(String[] args) {
       
    String userName = "Paddy";

    String userQuestion = "Is this magic 8 ball working properly?";

    System.out.println(userName + " asked : " + userQuestion);

    int randomNumber = (int)Math.floor(Math.random() * 8);
    
    String eightBall = "";
    
    System.out.println("--------------------------------");
    System.out.println("            ____");
    System.out.println("        ,dP9CGG88@b,");
    System.out.println("      ,IP  _   Y888@@b,");
    System.out.println("     dIi  (_)   G8888@b");
    System.out.println("    dCII  (_)   G8888@@b");
    System.out.println("    GCCIi     ,GG8888@@@");
    System.out.println("    GGCCCCCCCGGG88888@@@");
    System.out.println("    GGGGCCCGGGG88888@@@@...");
    System.out.println("    Y8GGGGGG8888888@@@@P.....");
    System.out.println("     Y88888888888@@@@@P......");
    System.out.println("     `Y8888888@@@@@@@P'......");
    System.out.println("       `@@@@@@@@@P'.......");
    System.out.println("           """"........");
    System.out.println("--------------------------------");
    
    switch (randomNumber) {
      case 0:
        eightBall = "It is certain";
        break;
      case 1:
        eightBall = "It is decidedly so";
        break;
      case 2:
        eightBall = "Reply hazy try again";
        break;
      case 3:
        eightBall = "Cannot predict now";
        break;
      case 4:
        eightBall = "Do not count on it";
        break;
      case 5:
        eightBall = "My sources say no";
        break;
      case 6:
        eightBall = "Outlook not so good";
        break;
      case 7:
        eightBall = "Signs point to yes";
        break;
    }

System.out.println("The eight ball answered: " + eightBall);
  }
}
