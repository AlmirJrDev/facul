import java.util.ArrayList;
import java.util.List;

// Representa uma quadra do estacionamento da faculdade
// Composicao: uma Quadra contem varias Vagas
public class Quadra {

    private String nome;
    private List<Vaga> vagas;

    public Quadra(String nome, int totalVagas) {
        this.nome = nome;
        this.vagas = new ArrayList<>();
        for (int i = 1; i <= totalVagas; i++) {
            vagas.add(new Vaga(i));
        }
    }

    // Ocupa a proxima vaga livre disponivel
    // Retorna true se conseguiu, false se a quadra esta cheia
    public boolean entrarVeiculo() {
        for (Vaga v : vagas) {
            if (v.isLivre()) {
                v.ocupar();
                return true;
            }
        }
        return false; // quadra cheia
    }

    // Libera uma vaga quando veiculo sai
    // Retorna true se havia vaga ocupada para liberar
    public boolean sairVeiculo() {
        for (Vaga v : vagas) {
            if (!v.isLivre()) {
                v.liberar();
                return true;
            }
        }
        return false; // nenhuma vaga ocupada
    }

    public int getVagasLivres() {
        int count = 0;
        for (Vaga v : vagas) {
            if (v.isLivre()) count++;
        }
        return count;
    }

    public boolean temVaga() {
        return getVagasLivres() > 0;
    }

    public String getNome() {
        return nome;
    }

    public int getTotalVagas() {
        return vagas.size();
    }

    @Override
    public String toString() {
        if (temVaga()) {
            return nome + ": " + getVagasLivres() + " vaga(s) disponivel(is) de " + getTotalVagas();
        } else {
            return nome + ": SEM VAGAS";
        }
    }
}
