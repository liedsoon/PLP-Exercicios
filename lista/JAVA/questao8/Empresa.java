package questao8;

import java.util.ArrayList;
import java.util.List;

public class Empresa {
    private String nome;
    private List <Empregado> empregados;

    public Empresa(String nome) {
        this.nome = nome;
        this.empregados = new ArrayList<>();
    }

    public void adicionarEmpregado(Empregado empregado){
        if(!empregados.contains(empregado)){
            empregados.add(empregado);
        }
    }

    public void exibirEmpregados(){
        System.out.println("Empregados da Empresa: " + nome);
        for(Empregado empregado: empregados){
            System.out.println("º Nome: "+ empregado.getNome());
            System.out.println("º Cargo: "+ empregado.getCargo());
            System.out.println("º Salário: "+ empregado.getSalario());
        }
    }

}
