package questao9;
/*
Interfaces/Protocolos Em Java e Golang, defina uma interface para imprimível que
tenha um método imprimir. Implemente essa interface em classes como Relatório e
Contrato. Em Python, use a abordagem de protocolo ou classes abstratas.
*/

public class Main {
    public static void main(String[] args) {
        Relatorio relatorio = new Relatorio("\nLorem ipsum dolor sit amet, consectetur adipiscing elit\n" +
                "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\n");
        relatorio.imprimir();

        Contrato contrato = new Contrato("Contrato de Trabalho",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit");

        contrato.imprimir();
    }
}
