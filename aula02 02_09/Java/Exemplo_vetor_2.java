
public class Exemplo_vetor_2 {
    public static void main(String[] args) {
        //Cria um vetor de 10 elementos
        int[] vetor = {5, 12, 7, 20, 15, 8, 3, 11, 6, 9};

        //Calcula  a media, o maior valor e o menor valor
        int soma = 0;
        int maiorValor = vetor[0];
        int menorValor = vetor[0];

        for(int i = 0; i < vetor.length; i++) {
            soma += vetor[i];

            if(vetor[i] > maiorValor) {
                maiorValor = vetor[i];
            }

            if(vetor[i] < menorValor) {
                menorValor = vetor[i];
            }
        }
        double media = (double) soma / vetor.length;

        // Exibindo os resultados

        System.out.println("Media: " + media);
        System.out.println("Maior valor: " + maiorValor);
        System.out.println("Menor valor: " + menorValor);
    }
}