package questao7;
/*
Crie uma classe Escola e uma classe Professor. A associação deve permitir
que uma escola tenha vários professores, e um professor possa lecionar em várias escolas.

Classe Escola:

*/
import java.util.ArrayList;
import java.util.List;

public class Escola {
    private String nome;
    private List<Professor> professores;

    public Escola(String nome){
        this.nome = nome;
        this.professores = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }
    public void adicionarProfessor(Professor professor){
        if(!professores.contains(professor)){
            professores.add(professor);
        }
        else{
            System.out.println("O Professor " + professor.getNome() + " já cadastrado na escola " + nome + "\n");
        }
    }

    public void exibirProfessores(){
        System.out.println("Professores da Escola: " + nome);
        for (Professor professor: professores){
            System.out.println("º "+ professor.getNome());
        }
        System.out.println(" ");

    }


}
