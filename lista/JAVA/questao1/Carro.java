package questao1;

/*
1. Crie uma classe Carro com atributos como marca, modelo, e ano.
Instancie três objetos dessa classe e exiba os detalhes de cada um.
*/

public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    public Carro(String marca, String modelo, int ano){
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }
    public void exibirCarro() {
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Ano: " + ano);
    }
    public static void main(String[] args) {
        Carro carro1 = new Carro("Fiat", "Uno", 2020);
        Carro carro2 = new Carro("Chevrolet", "Onix", 2021);
        Carro carro3 = new Carro("Volkswagen", "Gol", 2010);

        carro1.exibirCarro();
        carro2.exibirCarro();
        carro3.exibirCarro();
    }
}


