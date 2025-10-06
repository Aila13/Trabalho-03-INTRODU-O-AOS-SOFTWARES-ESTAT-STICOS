# Comparação de Bibliotecas de Visualização e Aceleração Computacional em Python: Um Estudo com Dados da Fauna de Collembola

## 📄 Informações do Projeto

| Instituição | UNIVERSIDADE FEDERAL DA PARAÍBA |
| :--- | :--- |
| **Centro** | CENTRO DE CIÊNCIAS EXATAS E DA NATUREZA |
| **Departamento** | DEPARTAMENTO DE ESTATÍSTICA |
| **Disciplina** | INTRODUÇÃO AOS SOFTWARES ESTATÍSTICOS |

---

## 🧑‍💻 Autor

* **Nome:** Aila Soares Ferreira
* **Matrícula:** 20240045022

---

## 🎯 Objetivo

Este projeto tem como objetivo principal **comparar e demonstrar** a aplicação prática de bibliotecas essenciais do ecossistema Python:

1.  **Visualização de Dados:** Comparar as abordagens e resultados de **Matplotlib**  e **Plotnine** .
2.  **Aceleração Computacional:** Demonstrar os ganhos de performance obtidos com a compilação *just-in-time* da biblioteca **Numba** em tarefas numéricas intensivas (Método de Monte Carlo).

O estudo utiliza dados reais de **fauna de Collembola** (artrópodes do solo) coletados em diferentes áreas da Paraíba para contextualizar as análises.

---

## 🛠️ Como Visualizar e Replicar

O relatório completo e finalizado está contido no arquivo **`[Trabalho].qmd`** ou **`Trabalho.html`** . https://aila13.github.io/Trabalho-03-INTRODU-O-AOS-SOFTWARES-ESTAT-STICOS/

### Arquivos Principais

* `dados.xlsx`: Arquivo de entrada contendo os dados de abundância da fauna.
* `gerar_graficos.py`: Script auxiliar usado para gerar os arquivos PNG de visualização separadamente.
* `analise_numba.py`: Script auxiliar usado para medir e obter o resultado de aceleração do Numba.
* `referencias.bib`: Arquivo BibTeX contendo as referências bibliográficas.

### Dependências

Para executar os scripts e renderizar o Quarto, você precisará das seguintes bibliotecas Python:

```bash
pip install pandas matplotlib plotnine numpy numba openpyxl
