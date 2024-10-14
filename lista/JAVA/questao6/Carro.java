package questao6;

/*
Implemente uma classe Motor e associe-a a uma classe Carro. A classe
Carro deve ter um objeto do tipo Motor como um de seus atributos.

Classe Carro

*/

public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private Motor motor;
    public Carro(String marca, String modelo, int ano, Motor motor){
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.motor = motor;
    }
    public void exibirCarro() {
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Ano: " + ano);
        System.out.println("Motor: " + motor.getPotencia() + " CV, "+ motor.getTipo());
    }
    public static void main(String[] args) {
        Motor motor = new Motor("Flex", 75);
        Carro carro1 = new Carro("Fiat", "Uno", 2020, motor);

        carro1.exibirCarro();
    }
}


