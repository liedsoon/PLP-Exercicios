package questao12;
/*
Sobrecarga de Operadores (Python) / Métodos de Conveniência (Java, Go) Em Python,
sobrecarregue o operador + para somar dois objetos Produto baseados no preço. Em Java
e Golang, crie métodos que permitam essa funcionalidade.
 */

public class Produto {
    private String nome;
    private double preco;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }
    public double getPreco() {
        return preco;
    }
    public static double somarPrecos(Produto p1, Produto p2) {
        return p1.getPreco() + p2.getPreco();
    }
    @Override
    public String toString() {
        return nome + ": R$" + preco;
    }

    public static void main(String[] args) {
        Produto p1 = new Produto("Livro", 25.00);
        Produto p2 = new Produto("Caderno", 40.00);

        System.out.println("Produtos:");
        System.out.println(p1);
        System.out.println(p2);
        double total = Produto.somarPrecos(p1, p2);
        System.out.println("Preço total: R$" + total);
    }
}

