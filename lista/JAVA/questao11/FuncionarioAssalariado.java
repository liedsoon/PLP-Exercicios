package questao11;
/*
Classes Abstratas Crie uma classe abstrata Funcionario com um método abstrato
calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
implementam calcularSalario de formas distintas.
*/
public class FuncionarioAssalariado extends Funcionario {
    private double salario;
    public FuncionarioAssalariado(String nome, double salario) {
        super(nome);
        this.salario = salario;
    }
    @Override
    public double calcularSalario() {
        return salario;
    }
}
