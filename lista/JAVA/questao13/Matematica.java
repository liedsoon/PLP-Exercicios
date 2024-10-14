package questao13;
/*
Adicione um método estático à classe Matematica que calcula o
fatorial de um número. Em Python, utilize @staticmethod, em Java static, e em Golang crie
uma função regular na struct.
*/

public class Matematica {
    public static long calcularFatorial(int n){
        if (n < 0) {
            throw new IllegalArgumentException("O fatorial não está definido para números negativos.");
        }
        if (n == 0) {
            return 1;
        }
        return n * calcularFatorial(n - 1);
    }

    public static void main(String[] args) {
        int numero = 5;
        long resultado = calcularFatorial(numero);
        System.out.println("Fatorial de 5 é: " + resultado);
    }
}
