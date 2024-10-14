package questao11;
/*
Classes Abstratas Crie uma classe abstrata Funcionario com um método abstrato
calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
implementam calcularSalario de formas distintas.
*/
public class FuncionarioHorista extends Funcionario {
    private double salarioHora;
    private double horasTrabalhadas;
    public FuncionarioHorista(String nome, double salarioHora, double horasTrabalhadas) {
        super(nome);
        this.salarioHora = salarioHora;
        this.horasTrabalhadas = horasTrabalhadas;
    }
    @Override
    public double calcularSalario() {
        return salarioHora * horasTrabalhadas;
    }



}
