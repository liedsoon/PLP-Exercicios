package questao6;
/*
Implemente uma classe Motor e associe-a a uma classe Carro. A classe
Carro deve ter um objeto do tipo Motor como um de seus atributos.

Classe Motor
 */

public class Motor {
    private String tipo;
    private int potencia;

    public Motor(String tipo, int potencia){
        this.tipo = tipo;
        this.potencia = potencia;
    }

    public String getTipo() {
        return tipo;
    }

    public int getPotencia() {
        return potencia;
    }
}
