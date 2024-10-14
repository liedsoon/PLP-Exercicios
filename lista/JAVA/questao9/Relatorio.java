package questao9;
/*
Interfaces/Protocolos Em Java e Golang, defina uma interface para imprimível que
tenha um método imprimir. Implemente essa interface em classes como Relatório e
Contrato. Em Python, use a abordagem de protocolo ou classes abstratas.
*/
public class Relatorio implements Imprimivel{
    private String conteudo;
    public Relatorio(String conteudo){
        this.conteudo = conteudo;
    }
    @Override
    public void imprimir() {
        System.out.println("Imprimindo o relatório: " + conteudo);
    }

}
