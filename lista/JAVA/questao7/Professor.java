package questao7;
/*
Crie uma classe Escola e uma classe Professor. A associação deve permitir
que uma escola tenha vários professores, e um professor possa lecionar em várias escolas.

Classe Professor:

*/
import java.util.ArrayList;
import java.util.List;

public class Professor {
    private String nome;
    private List<Escola> escolas;
    public Professor(String nome){
        this.nome = nome;
        this.escolas = new ArrayList<>();
    }
    public String getNome() {
        return nome;
    }
    public void adicionarEscola(Escola escola){
        if(!escolas.contains(escola)){
            escolas.add(escola);
            escola.adicionarProfessor(this);
        }
        else{
            System.out.println("O Professor " + nome + " já cadastrado na escola " + escola.getNome() + "\n");
        }
    }

    public void exibirEscolas(){
        System.out.println("Escolas do professor: " + nome);
        for(Escola escola : escolas){
            System.out.println("º "+ escola.getNome());
        }
        System.out.println(" ");
    }
}
