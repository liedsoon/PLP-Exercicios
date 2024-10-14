package questao5;
/*
Utilize polimorfismo para criar uma função que receba uma lista de
objetos Animal e chame o método som de cada um, demonstrando comportamento
diferente para cada subclasse.

 */
import java.util.ArrayList;
import java.util.List;

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
class Cachorro extends Animal {
    public Cachorro(String nome){
        super("Cachorro", nome);
    }
    @Override
    public String emitirSom(){
        return "O cachorro faz Au au";
    }
}
class Gato extends Animal {
    public Gato(String nome){
        super("Gato", nome);
    }
    @Override
    public String emitirSom(){
        return "O gato faz Miau";
    }
}
class Galinha extends Animal{
    public Galinha(String nome){
        super("Galinha", nome);
    }
    @Override
    public String emitirSom(){
        return "A galinha faz Có có";
    }
}

class main{
    public static void emitirSomAnimais(List<Animal> animais){
        for(Animal animal : animais){
            System.out.println(animal.emitirSom());
        }
    }

    public static void main(String[] args) {
        List<Animal> animais = new ArrayList<>();

        Animal cachorro = new Cachorro("Rex");
        Animal gato = new Gato("Michonne");
        Animal galinha = new Galinha("Rafinha");

        animais.add(cachorro);
        animais.add(gato);
        animais.add(galinha);

        emitirSomAnimais(animais);

    }
}
