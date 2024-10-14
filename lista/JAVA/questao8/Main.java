package questao8;

public class Main {
    public static void main(String[] args) {
        Empresa empresa = new Empresa("Serasa");

        Empregado empregado1 = new Empregado("João", "Desenvolvedor", 8000.00);
        Empregado empregado2 = new Empregado("Maria", "Analista", 10000.00);
        Empregado empregado3 = new Empregado("José", "Gerente", 15000.00);

        empresa.adicionarEmpregado(empregado1);
        empresa.adicionarEmpregado(empregado2);
        empresa.adicionarEmpregado(empregado3);

        empresa.exibirEmpregados();
    }
}
