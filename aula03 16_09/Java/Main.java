public class Main {
    public static void main(String[] args) {

        Animal cachorro = new Cachorro("Rex");
        Animal gato = new Gato("Michonner");

        System.out.println(cachorro.emitirSom());
        System.out.println(gato.emitirSom());
    }
}