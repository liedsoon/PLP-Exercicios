package questao3;
/*
Implemente uma classe ContaBancaria com atributos saldo, titular e
métodos depositar e sacar. Use encapsulamento para proteger o atributo saldo
 */

public class ContaBancaria {
    String titular;
    private double saldo;

    public ContaBancaria(String titular, double saldo){
        this.titular = titular;
        this.saldo = saldo;
    }

    public double getSaldo() {
        return saldo;
    }
    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void exibirConta(){
        System.out.println("Titular: " + titular);
        System.out.println("Saldo: " + getSaldo());
    }

    public void depositar(double valor){
        if (valor > 0){
            System.out.println("Depositando R$" + valor);
            saldo += valor;
        }
        else {
            System.out.println("Valor inválido");
        }
    }
    public void sacar(double valor){
        if(saldo >= valor && valor > 0){
            System.out.println("Sacando R$" + valor);
            saldo -= valor;
        }
        else {
            System.out.println("Saldo insuficiente ou valor inválido\n");
        }
    }
    public void exibirSaldo(){
        System.out.println("Saldo Atual: " + saldo + "\n");
    }

    public static void main(String[] args) {
        ContaBancaria c1 = new ContaBancaria("João", 1000);
        c1.exibirConta();

        c1.exibirSaldo();
        c1.depositar(500);
        c1.exibirSaldo();
        c1.sacar(300);
        c1.exibirSaldo();

        c1.exibirConta();
    }

}
