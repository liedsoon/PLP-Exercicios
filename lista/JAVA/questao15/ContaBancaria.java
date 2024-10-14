package questao15;
/*
classe de exceção personalizada
SaldoInsuficienteException em Java que seja lançada quando houver uma tentativa
de saque superior ao saldo disponível na classe ContaBancaria
 */
import questao15.exception.SaldoInsuficienteException;
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
    public void sacar(double valor) throws SaldoInsuficienteException{
        if(saldo < valor && valor > 0){
            throw new SaldoInsuficienteException("Saldo insuficiente ou valor inválido");
        }
        System.out.println("Sacando R$" + valor);
        saldo -= valor;
    }
    public void exibirSaldo(){
        System.out.println("Saldo Atual: " + saldo + "\n");
    }

    public static void main(String[] args) {
        try {
            ContaBancaria c1 = new ContaBancaria("João", 1000);
            c1.exibirConta();

            c1.depositar(500);
            c1.exibirSaldo();
            c1.sacar(1500);
            c1.exibirSaldo();
            c1.sacar(1000);

            c1.exibirConta();

        } catch (SaldoInsuficienteException e) {
            System.out.println(e.getMessage());
        }
    }

}
