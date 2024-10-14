package questao11;
/*
Classes Abstratas Crie uma classe abstrata Funcionario com um método abstrato
calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
implementam calcularSalario de formas distintas.
*/

public class Main {
    public static void main(String[] args) {
        FuncionarioHorista fh = new FuncionarioHorista("João", 30, 100);
        FuncionarioAssalariado fa = new FuncionarioAssalariado("Maria", 4500);

        System.out.println("Salario de " + fh.nome + " (Funcionario Horista): " + fh.calcularSalario());
        System.out.println("Salario de " + fa.nome + " (Funcionario Assalariado): " + fa.calcularSalario());
    }
}
