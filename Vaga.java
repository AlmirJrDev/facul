// Representa uma vaga fisica do estacionamento
// O sensor e simulado pelo metodo ocupar()/liberar()
public class Vaga {

    private int numero;
    private boolean ocupada;

    public Vaga(int numero) {
        this.numero = numero;
        this.ocupada = false; // comeca livre
    }

    // Sensor detecta veiculo entrando
    public void ocupar() {
        this.ocupada = true;
    }

    // Sensor detecta veiculo saindo
    public void liberar() {
        this.ocupada = false;
    }

    public boolean isLivre() {
        return !ocupada;
    }

    public int getNumero() {
        return numero;
    }

    @Override
    public String toString() {
        return "Vaga " + numero + ": " + (ocupada ? "OCUPADA" : "LIVRE");
    }
}
