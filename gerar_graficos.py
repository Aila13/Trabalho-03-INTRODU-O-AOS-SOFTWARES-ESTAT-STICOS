import pandas as pd
import matplotlib.pyplot as plt
from plotnine import (
    ggplot,
    aes,
    geom_col,
    labs,
    theme_classic,
    coord_flip,
    facet_wrap,
    element_text,
    scale_fill_brewer,
    # ADICIONE ESTA LINHA:
    theme, 
)
import numpy as np
import sys

# --- 2.1 PREPARAÇÃO DOS DADOS ---

print("Iniciando a leitura e processamento de dados...")

try:
    # Lendo o arquivo XLSX. Se o Pandas der erro, pode ser necessário instalar o openpyxl:
    # py -m pip install openpyxl
    df = pd.read_excel("dados.xlsx")
except FileNotFoundError:
    print("\nERRO: Arquivo 'dados.xlsx' não encontrado.")
    print("Certifique-se de que o arquivo está na mesma pasta que o script.")
    sys.exit(1)
except Exception as e:
    print(f"\nERRO ao ler o arquivo: {e}")
    print("Tente instalar o motor de leitura de Excel: py -m pip install openpyxl")
    sys.exit(1)

# Renomear a primeira coluna para 'Espécie'
df = df.rename(columns={df.columns[0]: "Espécie"})

# Transformar os dados do formato 'wide' para 'long' (tidy data)
df_long = df.melt(
    id_vars="Espécie",
    var_name="Área",
    value_name="Abundância"
)

# Calcular a abundância total por Área e por Espécie (para os gráficos)
abundancia_por_area = (
    df_long.groupby("Área")["Abundância"].sum().reset_index()
)
abundancia_por_especie = (
    df_long.groupby("Espécie")["Abundância"].sum().reset_index()
)

# Pegar as 10 espécies mais abundantes
top_10_especies = abundancia_por_especie.nlargest(10, "Abundância")
df_top_10 = df_long[
    df_long["Espécie"].isin(top_10_especies["Espécie"])
]

print("Processamento de dados concluído com sucesso.")

# --- 2.2 GRÁFICOS EM MATPLOTLIB ---

# Gráfico 1: Abundância Total por Área
print("Gerando e salvando Gráfico 1 (Matplotlib)...")
fig1, ax1 = plt.subplots(figsize=(10, 6))

barras = ax1.bar(
    abundancia_por_area["Área"],
    abundancia_por_area["Abundância"],
    color="#3690c0"
)

ax1.set_title(
    "Abundância Total de Collembola por Área",
    fontsize=16,
    fontweight="bold"
)
ax1.set_xlabel("Área de Coleta", fontsize=12)
ax1.set_ylabel("Abundância (Total de Indivíduos)", fontsize=12)

plt.xticks(rotation=45, ha="right")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
fig1.savefig('grafico_1_matplotlib.png', dpi=300, bbox_inches='tight')
plt.close(fig1)

# Gráfico 2: Distribuição das Top 10 Espécies por Área (Empilhamento)
print("Gerando e salvando Gráfico 2 (Matplotlib)...")
df_pivot = df_top_10.pivot_table(
    index="Área",
    columns="Espécie",
    values="Abundância",
    fill_value=0
)

fig2, ax2 = plt.subplots(figsize=(12, 7))

df_pivot.plot(kind="bar", stacked=True, ax=ax2, colormap="viridis")

ax2.set_title(
    "Distribuição das 10 Espécies Mais Abundantes por Área",
    fontsize=16,
    fontweight="bold"
)
ax2.set_xlabel("Área de Coleta", fontsize=12)
ax2.set_ylabel("Abundância (Total de Indivíduos)", fontsize=12)

ax2.legend(
    title="Espécie",
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
fig2.savefig('grafico_2_matplotlib.png', dpi=300, bbox_inches='tight')
plt.close(fig2)


# --- 2.3 GRÁFICOS EM PLOTNINE ---

# Gráfico 3: Abundância Total por Área (Coordenadas Invertidas)
print("Gerando e salvando Gráfico 3 (Plotnine)...")
plot_area_pn = (
    ggplot(abundancia_por_area, aes(x="Área", y="Abundância"))
    + geom_col(fill="#3690c0")
    + coord_flip()
    + labs(
        title="Abundância Total de Collembola por Área",
        y="Abundância (Total de Indivíduos)",
        x="Área de Coleta"
    )
    + theme_classic()
    + theme(
        plot_title=element_text(
            size=16, weight="bold"
        )
    )
)
plot_area_pn.save('grafico_3_plotnine.png', width=10, height=6, dpi=300)

# Gráfico 4: Distribuição das Top 10 Espécies entre Áreas (Faceting)
print("Gerando e salvando Gráfico 4 (Plotnine)...")
plot_facet_pn = (
    ggplot(
        df_top_10,
        aes(
            x="Espécie",
            y="Abundância",
            fill="Espécie"
        )
    )
    + geom_col(show_legend=False)
    + facet_wrap("~ Área")
    + labs(
        title="Distribuição da Abundância das 10 Espécies Mais Comuns por Área",
        y="Abundância",
        x=""
    )
    + theme_classic()
    + theme(
        axis_text_x=element_text(
            rotation=90, hjust=1
        ),
        strip_text_x=element_text(
            size=10, weight="bold"
        ),
        plot_title=element_text(
            size=16, weight="bold"
        ),
    )
    + scale_fill_brewer(type="qual", palette="Set3")
)
plot_facet_pn.save('grafico_4_plotnine.png', width=12, height=7, dpi=300)

print("\nSUCESSO: Todos os 4 gráficos foram salvos como arquivos PNG na sua pasta.")