import java.util.List;

// Gera um relatorio de status do estacionamento
// Separa a responsabilidade de exibir informacoes do sistema principal
public class Relatorio {

    // Exibe o status completo de todas as quadras
    public static void exibirStatus(String nomeFaculdade, List<Quadra> quadras) {
        System.out.println("\n========================================");
        System.out.println("  RELATORIO — " + nomeFaculdade);
        System.out.println("========================================");

        int totalLivres = 0;
        int totalVagas  = 0;

        for (Quadra q : quadras) {
            System.out.println("  " + q);
            totalLivres += q.getVagasLivres();
            totalVagas  += q.getTotalVagas();
        }

        int ocupadas = totalVagas - totalLivres;
        System.out.println("----------------------------------------");
        System.out.println("  Total de vagas  : " + totalVagas);
        System.out.println("  Ocupadas        : " + ocupadas);
        System.out.println("  Disponiveis     : " + totalLivres);

        if (totalLivres == 0) {
            System.out.println("  STATUS          : LOTADO");
        } else {
            System.out.println("  STATUS          : COM VAGAS");
        }
        System.out.println("========================================\n");
    }
}
