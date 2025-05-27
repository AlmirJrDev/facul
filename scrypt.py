from shiny import App, ui, render, reactive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import io
import base64

# Função para gerar dados simulados com loops e condicionais
def gerar_dados_vendas():
    """Gera dados simulados de vendas usando loops e condicionais"""
    vendedores = ["Ana Silva", "João Santos", "Maria Costa", "Pedro Oliveira", "Carla Souza"]
    produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam", "Headset"]
    regioes = ["Norte", "Sul", "Leste", "Oeste", "Centro"]
    
    dados = []
    
    # Loop para gerar 500 registros de vendas
    for i in range(500):
        # Condicionais para definir características dos dados
        vendedor = np.random.choice(vendedores)
        produto = np.random.choice(produtos)
        regiao = np.random.choice(regioes)
        
        # Condicional para definir preço baseado no produto
        if produto == "Notebook":
            preco_base = np.random.uniform(2000, 5000)
        elif produto == "Monitor":
            preco_base = np.random.uniform(800, 2000)
        elif produto in ["Mouse", "Teclado"]:
            preco_base = np.random.uniform(50, 200)
        else:  # Webcam, Headset
            preco_base = np.random.uniform(100, 500)
        
        # Condicional para aplicar desconto baseado na região
        if regiao in ["Norte", "Sul"]:
            desconto = 0.1  # 10% desconto
        elif regiao == "Centro":
            desconto = 0.05  # 5% desconto
        else:
            desconto = 0  # Sem desconto
        
        preco_final = preco_base * (1 - desconto)
        quantidade = np.random.randint(1, 10)
        
        # Condicional para bônus do vendedor
        if quantidade >= 5:
            bonus_vendedor = preco_final * 0.02  # 2% de bônus
        else:
            bonus_vendedor = preco_final * 0.01  # 1% de bônus
        
        # Data aleatória nos últimos 12 meses
        data_venda = datetime.now() - timedelta(days=np.random.randint(0, 365))
        
        dados.append({
            'data': data_venda.strftime('%Y-%m-%d'),
            'vendedor': vendedor,
            'produto': produto,
            'regiao': regiao,
            'quantidade': quantidade,
            'preco_unitario': round(preco_final, 2),
            'total_venda': round(preco_final * quantidade, 2),
            'bonus_vendedor': round(bonus_vendedor, 2)
        })
    
    return pd.DataFrame(dados)

# Função para calcular estatísticas com loops e condicionais
def calcular_estatisticas(df):
    """Calcula estatísticas usando loops e condicionais"""
    stats = {}
    
    # Loop através dos vendedores para calcular estatísticas individuais
    vendedores_stats = {}
    for vendedor in df['vendedor'].unique():
        dados_vendedor = df[df['vendedor'] == vendedor]
        
        # Condicionais para classificar performance
        total_vendas = dados_vendedor['total_venda'].sum()
        if total_vendas >= 50000:
            performance = "Excelente"
        elif total_vendas >= 30000:
            performance = "Boa"
        elif total_vendas >= 15000:
            performance = "Regular"
        else:
            performance = "Baixa"
        
        vendedores_stats[vendedor] = {
            'total_vendas': total_vendas,
            'num_vendas': len(dados_vendedor),
            'performance': performance,
            'bonus_total': dados_vendedor['bonus_vendedor'].sum()
        }
    
    stats['vendedores'] = vendedores_stats
    
    # Loop através das regiões
    regioes_stats = {}
    for regiao in df['regiao'].unique():
        dados_regiao = df[df['regiao'] == regiao]
        regioes_stats[regiao] = {
            'total_vendas': dados_regiao['total_venda'].sum(),
            'vendas_count': len(dados_regiao)
        }
    
    stats['regioes'] = regioes_stats
    stats['total_geral'] = df['total_venda'].sum()
    stats['media_venda'] = df['total_venda'].mean()
    
    return stats

# Interface do usuário usando a API mais recente
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.h3("🔧 Filtros"),
        ui.input_selectize(
            "vendedor_filtro",
            "Selecione Vendedor(es):",
            choices=[],
            multiple=True
        ),
        ui.input_selectize(
            "regiao_filtro", 
            "Selecione Região(ões):",
            choices=[],
            multiple=True
        ),
        ui.input_selectize(
            "produto_filtro",
            "Selecione Produto(s):", 
            choices=[],
            multiple=True
        ),
        ui.input_date_range(
            "data_filtro",
            "Período:",
            start="2023-01-01",
            end="2024-12-31"
        ),
        ui.input_action_button("gerar_dados", "🔄 Gerar Novos Dados", class_="btn-primary"),
        width=300
    ),
    
    ui.div(
        ui.h1("📊 Dashboard de Análise de Vendas"),
        
        # Cards com estatísticas
        ui.div(
            ui.div(
                ui.div(
                    ui.h4("Total de Vendas", style="color: #007bff;"),
                    ui.h2(ui.output_text("total_vendas"), style="color: #007bff;"),
                    style="background: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center; border-left: 4px solid #007bff;"
                ),
                class_="col-md-3 mb-3"
            ),
            ui.div(
                ui.div(
                    ui.h4("Número de Vendas", style="color: #28a745;"),
                    ui.h2(ui.output_text("num_vendas"), style="color: #28a745;"),
                    style="background: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center; border-left: 4px solid #28a745;"
                ),
                class_="col-md-3 mb-3"
            ),
            ui.div(
                ui.div(
                    ui.h4("Ticket Médio", style="color: #17a2b8;"),
                    ui.h2(ui.output_text("ticket_medio"), style="color: #17a2b8;"),
                    style="background: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center; border-left: 4px solid #17a2b8;"
                ),
                class_="col-md-3 mb-3"
            ),
            ui.div(
                ui.div(
                    ui.h4("Melhor Vendedor", style="color: #ffc107;"),
                    ui.h2(ui.output_text("melhor_vendedor"), style="color: #ffc107;"),
                    style="background: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center; border-left: 4px solid #ffc107;"
                ),
                class_="col-md-3 mb-3"
            ),
            class_="row"
        ),
        
        # Tabs para diferentes visualizações
        ui.navset_card_tab(
            ui.nav_panel("📈 Gráficos",
                ui.div(
                    ui.div(
                        ui.output_plot("grafico_vendedores"),
                        class_="col-md-6"
                    ),
                    ui.div(
                        ui.output_plot("grafico_regioes"),
                        class_="col-md-6"
                    ),
                    class_="row mb-4"
                ),
                ui.div(
                    ui.div(
                        ui.output_plot("grafico_produtos"),
                        class_="col-md-6"
                    ),
                    ui.div(
                        ui.output_plot("grafico_timeline"),
                        class_="col-md-6"
                    ),
                    class_="row"
                )
            ),
            
            ui.nav_panel("📋 Dados Detalhados",
                ui.output_data_frame("tabela_dados")
            ),
            
            ui.nav_panel("📊 Relatório de Performance",
                ui.output_ui("relatorio_performance")
            )
        ),
        
        style="padding: 20px;"
    ),
    
    title="Dashboard de Vendas",
    fillable=True
)

def server(input, output, session):
    # Dados reativos
    dados_vendas = reactive.Value(gerar_dados_vendas())
    
    # Atualizar choices dos filtros quando os dados mudarem
    @reactive.Effect
    def atualizar_filtros():
        df = dados_vendas()
        
        ui.update_selectize(
            "vendedor_filtro",
            choices=sorted(df['vendedor'].unique().tolist())
        )
        ui.update_selectize(
            "regiao_filtro", 
            choices=sorted(df['regiao'].unique().tolist())
        )
        ui.update_selectize(
            "produto_filtro",
            choices=sorted(df['produto'].unique().tolist())
        )
    
    # Gerar novos dados quando botão for clicado
    @reactive.Effect
    @reactive.event(input.gerar_dados)
    def gerar_novos_dados():
        dados_vendas.set(gerar_dados_vendas())
    
    # Filtrar dados baseado nos inputs
    @reactive.Calc
    def dados_filtrados():
        df = dados_vendas().copy()
        
        # Aplicar filtros condicionalmente
        if input.vendedor_filtro():
            df = df[df['vendedor'].isin(input.vendedor_filtro())]
        
        if input.regiao_filtro():
            df = df[df['regiao'].isin(input.regiao_filtro())]
            
        if input.produto_filtro():
            df = df[df['produto'].isin(input.produto_filtro())]
        
        # Filtro de data
        df['data'] = pd.to_datetime(df['data'])
        data_inicio = pd.to_datetime(input.data_filtro()[0])
        data_fim = pd.to_datetime(input.data_filtro()[1])
        df = df[(df['data'] >= data_inicio) & (df['data'] <= data_fim)]
        
        return df
    
    # Outputs dos cards de estatísticas
    @output
    @render.text
    def total_vendas():
        return f"R$ {dados_filtrados()['total_venda'].sum():,.2f}"
    
    @output
    @render.text  
    def num_vendas():
        return f"{len(dados_filtrados()):,}"
    
    @output
    @render.text
    def ticket_medio():
        df = dados_filtrados()
        if len(df) > 0:
            return f"R$ {df['total_venda'].mean():,.2f}"
        return "R$ 0,00"
    
    @output
    @render.text
    def melhor_vendedor():
        df = dados_filtrados()
        if len(df) > 0:
            vendas_por_vendedor = df.groupby('vendedor')['total_venda'].sum()
            return vendas_por_vendedor.idxmax()
        return "N/A"
    
    # Gráficos
    @output
    @render.plot
    def grafico_vendedores():
        df = dados_filtrados()
        if len(df) == 0:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.text(0.5, 0.5, 'Nenhum dado disponível', ha='center', va='center', transform=ax.transAxes)
            return fig
            
        vendas_vendedor = df.groupby('vendedor')['total_venda'].sum().sort_values(ascending=True)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(range(len(vendas_vendedor)), vendas_vendedor.values)
        
        # Loop para colorir barras condicionalmente
        for i, bar in enumerate(bars):
            if vendas_vendedor.values[i] >= 40000:
                bar.set_color('green')
            elif vendas_vendedor.values[i] >= 25000:
                bar.set_color('orange') 
            else:
                bar.set_color('red')
        
        ax.set_yticks(range(len(vendas_vendedor)))
        ax.set_yticklabels(vendas_vendedor.index)
        ax.set_xlabel('Total de Vendas (R$)')
        ax.set_title('Vendas por Vendedor')
        plt.tight_layout()
        return fig
    
    @output
    @render.plot
    def grafico_regioes():
        df = dados_filtrados()
        if len(df) == 0:
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.text(0.5, 0.5, 'Nenhum dado disponível', ha='center', va='center', transform=ax.transAxes)
            return fig
            
        vendas_regiao = df.groupby('regiao')['total_venda'].sum()
        
        fig, ax = plt.subplots(figsize=(8, 8))
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
        ax.pie(vendas_regiao.values, labels=vendas_regiao.index, autopct='%1.1f%%', colors=colors)
        ax.set_title('Distribuição de Vendas por Região')
        return fig
    
    @output
    @render.plot
    def grafico_produtos():
        df = dados_filtrados()
        if len(df) == 0:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.text(0.5, 0.5, 'Nenhum dado disponível', ha='center', va='center', transform=ax.transAxes)
            return fig
            
        vendas_produto = df.groupby('produto')['total_venda'].sum().sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(range(len(vendas_produto)), vendas_produto.values)
        
        # Colorir barras baseado no valor
        for i, bar in enumerate(bars):
            if vendas_produto.values[i] >= vendas_produto.mean():
                bar.set_color('darkgreen')
            else:
                bar.set_color('lightcoral')
        
        ax.set_xticks(range(len(vendas_produto)))
        ax.set_xticklabels(vendas_produto.index, rotation=45)
        ax.set_ylabel('Total de Vendas (R$)')
        ax.set_title('Vendas por Produto')
        plt.tight_layout()
        return fig
    
    @output
    @render.plot
    def grafico_timeline():
        df = dados_filtrados()
        if len(df) == 0:
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.text(0.5, 0.5, 'Nenhum dado disponível', ha='center', va='center', transform=ax.transAxes)
            return fig
            
        df['data'] = pd.to_datetime(df['data'])
        vendas_mes = df.groupby(df['data'].dt.to_period('M'))['total_venda'].sum()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(range(len(vendas_mes)), vendas_mes.values, marker='o', linewidth=2, markersize=6)
        ax.set_xticks(range(len(vendas_mes)))
        ax.set_xticklabels([str(x) for x in vendas_mes.index], rotation=45)
        ax.set_ylabel('Total de Vendas (R$)')
        ax.set_title('Evolução das Vendas ao Longo do Tempo')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        return fig
    
    # Tabela de dados
    @output
    @render.data_frame
    def tabela_dados():
        df = dados_filtrados()
        return df.sort_values('total_venda', ascending=False)
    
    # Relatório de performance
    @output
    @render.ui
    def relatorio_performance():
        df = dados_filtrados()
        if len(df) == 0:
            return ui.p("Nenhum dado disponível para os filtros selecionados.")
        
        stats = calcular_estatisticas(df)
        
        # Criar relatório usando loops e condicionais
        relatorio_html = []
        
        relatorio_html.append(ui.h3("🏆 Relatório de Performance"))
        relatorio_html.append(ui.hr())
        
        # Seção de vendedores
        relatorio_html.append(ui.h4("👥 Performance por Vendedor"))
        
        for vendedor, dados in stats['vendedores'].items():
            # Condicional para ícone baseado na performance
            if dados['performance'] == "Excelente":
                icone = "🏆"
                cor_style = "color: green;"
            elif dados['performance'] == "Boa":
                icone = "👍"
                cor_style = "color: blue;"
            elif dados['performance'] == "Regular":
                icone = "⚠️"
                cor_style = "color: orange;"
            else:
                icone = "📉"
                cor_style = "color: red;"
            
            relatorio_html.append(
                ui.div(
                    ui.p(f"{icone} {vendedor}", style="font-weight: bold;"),
                    ui.p(f"Total de Vendas: R$ {dados['total_vendas']:,.2f}", style=cor_style),
                    ui.p(f"Número de Vendas: {dados['num_vendas']}"),
                    ui.p(f"Performance: {dados['performance']}"),
                    ui.p(f"Bônus Total: R$ {dados['bonus_total']:,.2f}"),
                    ui.hr(),
                    style="margin-bottom: 20px; padding: 15px; background: #f8f9fa; border-radius: 8px;"
                )
            )
        
        # Seção de regiões
        relatorio_html.append(ui.h4("🗺️ Performance por Região"))
        
        for regiao, dados in stats['regioes'].items():
            relatorio_html.append(
                ui.div(
                    ui.p(f"📍 {regiao}", style="font-weight: bold;"),
                    ui.p(f"Total de Vendas: R$ {dados['total_vendas']:,.2f}"),
                    ui.p(f"Número de Vendas: {dados['vendas_count']}"),
                    ui.hr(),
                    style="margin-bottom: 20px; padding: 15px; background: #f8f9fa; border-radius: 8px;"
                )
            )
        
        # Resumo geral
        relatorio_html.append(ui.h4("📈 Resumo Geral"))
        relatorio_html.append(
            ui.div(
                ui.p(f"💰 Total Geral: R$ {stats['total_geral']:,.2f}", style="font-weight: bold; color: green;"),
                ui.p(f"📊 Média por Venda: R$ {stats['media_venda']:,.2f}"),
                style="margin-bottom: 20px; padding: 15px; background: #e8f5e8; border-radius: 8px;"
            )
        )
        
        return ui.div(*relatorio_html)

# Criar aplicação
app = App(app_ui, server)

if __name__ == "__main__":
    app.run() 