package questao11;
/*
Classes Abstratas Crie uma classe abstrata Funcionario com um método abstrato
calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
implementam calcularSalario de formas distintas.
*/
public abstract class Funcionario {
    protected String nome;
    public Funcionario(String nome) {
        this.nome = nome;
    }
    public abstract double calcularSalario();
}
