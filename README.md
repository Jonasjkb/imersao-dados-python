# 📊 Dashboard de Salários na Área de Dados

Este projeto consiste em um dashboard interativo desenvolvido com Python para análise de salários na área de dados, permitindo explorar informações de forma dinâmica e intuitiva.

---

## 🚀 Tecnologias utilizadas

* Python
* Pandas (manipulação de dados)
* Streamlit (criação do dashboard)
* Plotly (visualização interativa)

---

## 📌 Objetivo

O objetivo deste projeto é analisar dados salariais na área de tecnologia, permitindo:

* Exploração por filtros dinâmicos
* Visualização de distribuição salarial
* Comparação entre cargos
* Análise por país
* Identificação de tendências ao longo do tempo

---

## 🎛️ Funcionalidades

* Filtros interativos por:

  * Ano
  * Senioridade
  * Tipo de contrato
  * Tamanho da empresa
  * Modelo de trabalho

* Métricas principais:

  * Salário médio
  * Salário máximo
  * Total de registros
  * Cargo mais frequente

* Visualizações:

  * Top 10 cargos por salário
  * Distribuição salarial (histograma + boxplot)
  * Proporção de modelos de trabalho
  * Mapa global de salários
  * Evolução salarial ao longo do tempo

---

## ⚡ Performance

O projeto utiliza cache de dados com `st.cache_data`, evitando recarregamentos desnecessários e melhorando a performance da aplicação.

Também é possível configurar o tempo de atualização dos dados utilizando `ttl`.

---

## 📂 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o projeto

```bash
streamlit run app.py
```

---

## 📊 Fonte dos dados

Dataset público hospedado no GitHub.

---

## 💡 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conceitos como:

* Manipulação e limpeza de dados com Pandas
* Criação de dashboards interativos
* Filtragem dinâmica com DataFrames
* Visualização de dados com Plotly
* Otimização de performance com cache

---

## 📌 Melhorias futuras

* Deploy em nuvem (Streamlit Cloud ou Render)
* Integração com banco de dados
* Atualização automática dos dados
* Novas análises e métricas

---

## 👨‍💻 Autor

Jonas Barbosa
