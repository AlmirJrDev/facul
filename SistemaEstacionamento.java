import java.util.ArrayList;
import java.util.List;

// Gerencia todas as quadras e responde se ha vaga disponivel
public class SistemaEstacionamento {

    private String nomeFaculdade;
    private List<Quadra> quadras;

    public SistemaEstacionamento(String nomeFaculdade) {
        this.nomeFaculdade = nomeFaculdade;
        this.quadras = new ArrayList<>();
    }

    public void adicionarQuadra(Quadra quadra) {
        quadras.add(quadra);
    }

    // Pergunta principal do sistema: tem vaga em alguma quadra?
    public void consultarVagas() {
        System.out.println("\n=== " + nomeFaculdade + " — Vagas disponiveis ===");
        boolean algumaTem = false;
        for (Quadra q : quadras) {
            System.out.println("  " + q);
            if (q.temVaga()) algumaTem = true;
        }
        if (!algumaTem) {
            System.out.println("  >> Estacionamento LOTADO. Nenhuma vaga disponivel.");
        }
        System.out.println("===========================================\n");
    }

    // Registra entrada em uma quadra especifica pelo nome
    public void registrarEntrada(String nomeQuadra) {
        for (Quadra q : quadras) {
            if (q.getNome().equalsIgnoreCase(nomeQuadra)) {
                if (q.entrarVeiculo()) {
                    System.out.println("[ENTRADA] " + nomeQuadra + " — vaga ocupada. Restam: " + q.getVagasLivres());
                } else {
                    System.out.println("[ENTRADA] " + nomeQuadra + " — SEM VAGAS.");
                }
                return;
            }
        }
        System.out.println("[ENTRADA] Quadra '" + nomeQuadra + "' nao encontrada.");
    }

    // Registra saida em uma quadra especifica pelo nome
    public void registrarSaida(String nomeQuadra) {
        for (Quadra q : quadras) {
            if (q.getNome().equalsIgnoreCase(nomeQuadra)) {
                if (q.sairVeiculo()) {
                    System.out.println("[SAIDA]   " + nomeQuadra + " — vaga liberada. Disponiveis: " + q.getVagasLivres());
                } else {
                    System.out.println("[SAIDA]   " + nomeQuadra + " — nenhuma vaga ocupada para liberar.");
                }
                return;
            }
        }
        System.out.println("[SAIDA] Quadra '" + nomeQuadra + "' nao encontrada.");
    }
}
