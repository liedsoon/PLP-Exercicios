package questao7;
/*
Crie uma classe Escola e uma classe Professor. A associação deve permitir
que uma escola tenha vários professores, e um professor possa lecionar em várias escolas.

Classe Main:

*/
public class Main {
    public static void main(String[] args) {

        Escola escola1 = new Escola("Paraiso do saber");
        Escola escola2 = new Escola("Maria Caxias");
        Escola escola3 = new Escola("Sao Jose");

        Professor professor1 = new Professor("Joao");
        Professor professor2 = new Professor("Maria");
        Professor professor3 = new Professor("Jose");

        professor1.adicionarEscola(escola1);
        professor1.adicionarEscola(escola2);
        professor2.adicionarEscola(escola1);
        professor2.adicionarEscola(escola3);
        professor3.adicionarEscola(escola2);
        professor3.adicionarEscola(escola3);

        escola1.exibirProfessores();
        escola2.exibirProfessores();
        escola3.exibirProfessores();

        professor1.exibirEscolas();
        professor2.exibirEscolas();
        professor3.exibirEscolas();

    }
}
