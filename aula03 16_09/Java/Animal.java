public class Animal {
    protected String especie;
    protected String nome;

    public Animal(String especie, String nome) {
        this.especie = especie;
        this.nome = nome;
    }

    public String emitirSom(){
        return ""; //Método a ser sobreescrito
    }
}

class Cachorro extends Animal{

    public Cachorro(String nome) {
        super("Cachorro", nome);
    }

    @Override
    public String emitirSom() {
        return "Au Au";
    }
}

class Gato extends Animal{

    public Gato(String nome){
        super("Gato", nome);
    }

    @Override
    public String emitirSom() {
        return "Miau";
    }
}
