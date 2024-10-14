package questao4;
/*
Crie uma classe base Animal com métodos como som. Derive classes como
Cachorro e Gato que implementam o método som de maneiras diferentes.
 */
public class Animal {
    protected String especie;
    protected String nome;
    public Animal(String especie, String nome){
        this.especie = especie;
        this.nome = nome;
    }
    public String emitirSom(){
        return "";
    }
}
class Cachorro extends Animal{
    public Cachorro(String nome){
        super("Cachorro", nome);
    }
    @Override
    public String emitirSom(){
        return "Au au";
    }
}
class Gato extends Animal{
    public Gato(String nome){
        super("Gato", nome);
    }
    @Override
    public String emitirSom(){
        return "Miau";
    }
}

class main{
    public static void main(String[] args) {
        Animal cachorro = new Cachorro("Rex");
        Animal gato = new Gato("Michonne");

        System.out.println(cachorro.emitirSom());
        System.out.println(gato.emitirSom());
    }
}
