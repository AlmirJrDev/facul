// Simulacao do sistema de vagas da faculdade
// Cenario: manha de segunda-feira — quadras enchendo e esvaziando
public class Main {

    public static void main(String[] args) {

        // Configura o estacionamento com 3 quadras
        SistemaEstacionamento sistema = new SistemaEstacionamento("Estacionamento FACAMP");
        sistema.adicionarQuadra(new Quadra("Quadra A", 3));
        sistema.adicionarQuadra(new Quadra("Quadra B", 2));
        sistema.adicionarQuadra(new Quadra("Quadra C", 2));

        // Situacao inicial — tudo vazio
        sistema.consultarVagas();

        // Veiculos chegando de manha
        System.out.println("-- Veiculos chegando --");
        sistema.registrarEntrada("Quadra A");
        sistema.registrarEntrada("Quadra A");
        sistema.registrarEntrada("Quadra A"); // Quadra A cheia
        sistema.registrarEntrada("Quadra B");
        sistema.registrarEntrada("Quadra B"); // Quadra B cheia
        sistema.registrarEntrada("Quadra C");
        sistema.registrarEntrada("Quadra C"); // Tudo cheio

        // Consulta: sistema avisa que esta lotado
        sistema.consultarVagas();

        // Tenta entrar mas nao tem vaga
        System.out.println("-- Mais um veiculo tenta entrar --");
        sistema.registrarEntrada("Quadra A");
        sistema.registrarEntrada("Quadra B");

        // Horario do almoco: duas pessoas saem
        System.out.println("\n-- Veiculos saindo --");
        sistema.registrarSaida("Quadra A");
        sistema.registrarSaida("Quadra C");

        // Consulta final — agora tem vaga de novo
        sistema.consultarVagas();
    }
}
