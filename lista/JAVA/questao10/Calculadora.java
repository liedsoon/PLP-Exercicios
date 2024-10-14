package questao10;
/*
Implemente uma classe Calculadora com métodos somar que aceita diferentes números
de parâmetros (dois ou três números).
 */
public class Calculadora {
    public int somar(int a, int b) {return a + b;}
    public int somar(int a, int b, int c) {return a + b + c;}
    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora();
        int resultado1 = calculadora.somar(10, 10);
        int resultado2 = calculadora.somar(10, 10, 10);
        System.out.println("Somando 10 + 10: " + resultado1);
        System.out.println("Somando 10 + 10 + 10: " + resultado2);
    }
}
