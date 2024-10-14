package questao2;

/*
2. Adicione um método acelerar e frear à classe Carro que altere um atributo
velocidade. Crie um método para exibir a velocidade atual.
*/

public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private int velocidade;
    public Carro(String marca, String modelo, int ano){
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = 0;
    }

    public void acelerar(int potencia) {
        System.out.println("Acelerando...\n");
        velocidade += potencia;
    }

    public void frear() {
        System.out.println("Freando...\n");
        velocidade = velocidade /  2;
    }
    public void exibirCarro() {
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Ano: " + ano);
        System.out.println(" ");
    }

    public void exibirVelocidade(){
        System.out.println("Velocidade Atual: " + velocidade + "\n");
    }


    public static void main(String[] args) {
        Carro carro1 = new Carro("Fiat", "Uno", 2020);

        carro1.exibirCarro();

        carro1.acelerar(10);
        carro1.exibirVelocidade();
        carro1.acelerar(30);
        carro1.exibirVelocidade();
        carro1.frear();
        carro1.frear();
        carro1.frear();
        carro1.exibirVelocidade();

    }
}



