package questao14;
/*
Implemente o padrão de projeto Singleton para garantir que apenas uma
instância de uma classe Configuracao seja criada.
 */

public class Configuracao {
    private static Configuracao instance;
    private String parametro;
    private Configuracao() {
        this.parametro = "Padrão";
    }
    public static Configuracao getInstance() {
        if (instance == null) {
            instance = new Configuracao();
        }
        return instance;
    }
    public String getParametro() {
        return parametro;
    }
    public void setParametro(String parametro) {
        this.parametro = parametro;
    }

    public static void main(String[] args) {
        Configuracao configuracao = Configuracao.getInstance();
        Configuracao configuracao2 = Configuracao.getInstance();

        System.out.println(configuracao == configuracao2); // Saída: true

        System.out.println(configuracao.getParametro()); // Saída: "Padrão"
        configuracao.setParametro("Novo Valor");
        System.out.println(configuracao2.getParametro()); // Saída: "Novo Valor"
    }
}