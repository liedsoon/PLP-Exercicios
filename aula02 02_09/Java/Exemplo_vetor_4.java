import java.util.Scanner;

public class Exemplo_vetor_4 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int [] numbers = new int [6];
        int sumEven = 0;
        int countOdd = 0;

        System.out.println("Digite 6 números inteiros: ");

        // Reconhecer os numeros do usuario
        for (int i = 0; i < 6; i++){
            numbers[i] = scanner.nextInt();
        }

        System.out.print("Números pares digitados: ");
        for (int num : numbers){
            if(num % 2 == 0){
                System.out.print(num + " ");
                sumEven += num;
            }
        }

        System.out.println("\nSoma dos números pares: " + sumEven);
        System.out.print("Números ímpares digitados: ");
        for (int num : numbers){
            if(num % 2 != 0){
                System.out.print(num + " ");
                countOdd++;
            }
        }
        System.out.println("\nQuantidade de números ímpares: " + countOdd);
    }
}
