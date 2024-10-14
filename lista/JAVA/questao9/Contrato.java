package questao9;
/*
Interfaces/Protocolos Em Java e Golang, defina uma interface para imprimível que
tenha um método imprimir. Implemente essa interface em classes como Relatório e
Contrato. Em Python, use a abordagem de protocolo ou classes abstratas.
*/
public class Contrato implements Imprimivel{
    private String nome;
    private String conteudo;
    public Contrato(String nome, String conteudo){
        this.nome = nome;
        this.conteudo = conteudo;
    }
    @Override
    public void imprimir() {
        System.out.println("Imprimindo o contrato: " + nome);
        System.out.println("Termos: " + conteudo);
    }
}
