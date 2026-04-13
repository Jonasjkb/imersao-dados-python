import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# --- CACHE DE DADOS (PERFORMANCE) ---
# Com o Time to Live, onde dados serão recarregados no intervalo de tempo informado
@st.cache_data(ttl=3600)
def load_data():
    url = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
    return pd.read_csv(url)

df = load_data()

# --- BOTÃO PARA ATUALIZAR DADOS MANUALMENTE ---
if st.sidebar.button("🔄 Atualizar dados"):
    st.cache_data.clear()

# --- SIDEBAR ---
st.sidebar.header("🔍 Filtros")

anos = sorted(df['ano'].unique())
anos_sel = st.sidebar.multiselect("Ano", anos, default=anos)

senioridades = sorted(df['senioridade'].unique())
senioridades_sel = st.sidebar.multiselect("Senioridade", senioridades, default=senioridades)

contratos = sorted(df['contrato'].unique())
contratos_sel = st.sidebar.multiselect("Tipo de Contrato", contratos, default=contratos)

tamanhos = sorted(df['tamanho_empresa'].unique())
tamanhos_sel = st.sidebar.multiselect("Tamanho da Empresa", tamanhos, default=tamanhos)

modelos = sorted(df['remoto'].unique())
modelos_sel = st.sidebar.multiselect("Modelo de Trabalho", modelos, default=modelos)

# --- FILTRO ---
df_filtrado = df[
    (df['ano'].isin(anos_sel)) &
    (df['senioridade'].isin(senioridades_sel)) &
    (df['contrato'].isin(contratos_sel)) &
    (df['tamanho_empresa'].isin(tamanhos_sel)) &
    (df['remoto'].isin(modelos_sel))
]

# --- UX: DATAFRAME VAZIO ---
if df_filtrado.empty:
    st.warning("⚠️ Nenhum dado encontrado com os filtros selecionados.")
    st.stop()

# --- HEADER ---
st.title("📊 Dashboard de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados. Ajuste os filtros à esquerda.")

# --- KPI ---
st.subheader("📌 Métricas Gerais")

salario_medio = df_filtrado['usd'].mean()
salario_maximo = df_filtrado['usd'].max()
total_registros = df_filtrado.shape[0]
cargo_top = df_filtrado["cargo"].mode()[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Salário médio", f"${salario_medio:,.0f}")
col2.metric("🚀 Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("📊 Registros", f"{total_registros:,}")
col4.metric("👨‍💻 Cargo mais frequente", cargo_top)

st.markdown("---")

# --- GRÁFICOS ---
st.subheader("📈 Análises Visuais")

col1, col2 = st.columns(2)

# --- TOP CARGOS ---
with col1:
    top_cargos = (
        df_filtrado
        .groupby('cargo')['usd']
        .mean()
        .nlargest(10)
        .sort_values()
        .reset_index()
    )

    fig_cargos = px.bar(
        top_cargos,
        x='usd',
        y='cargo',
        orientation='h',
        title="Top 10 cargos por salário médio",
        labels={'usd': 'Salário médio (USD)', 'cargo': ''},
        template="plotly_white"
    )

    fig_cargos.update_traces(
        texttemplate='%{x:,.0f}',
        textposition='outside'
    )

    st.plotly_chart(fig_cargos, use_container_width=True)

# --- HISTOGRAMA + BOX ---
with col2:
    fig_hist = px.histogram(
        df_filtrado,
        x='usd',
        nbins=30,
        title="Distribuição salarial",
        template="plotly_white",
        marginal="box"
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# --- SEGUNDA LINHA ---
col3, col4 = st.columns(2)

# --- REMOTO ---
with col3:
    remoto_df = df_filtrado['remoto'].value_counts().reset_index()
    remoto_df.columns = ['tipo', 'quantidade']

    fig_pie = px.pie(
        remoto_df,
        names='tipo',
        values='quantidade',
        hole=0.5,
        title="Modelo de trabalho",
        template="plotly_white"
    )

    fig_pie.update_traces(textinfo='percent+label')

    st.plotly_chart(fig_pie, use_container_width=True)

# --- MAPA ---
with col4:
    df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']

    if not df_ds.empty:
        df_map = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

        fig_map = px.choropleth(
            df_map,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='Viridis',
            title='Salário médio de Data Scientists por país',
            labels={'usd': 'Salário médio (USD)'},
            template="plotly_white"
        )

        st.plotly_chart(fig_map, use_container_width=True)
    else:
        st.info("Sem dados para Data Scientist com os filtros atuais.")

# --- LINHA DO TEMPO ---
st.subheader("📅 Evolução Salarial")

df_tempo = df_filtrado.groupby('ano')['usd'].mean().reset_index()

fig_linha = px.line(
    df_tempo,
    x='ano',
    y='usd',
    markers=True,
    title="Evolução do salário médio ao longo dos anos",
    template="plotly_white"
)

st.plotly_chart(fig_linha, use_container_width=True)

# --- TABELA ---
st.subheader("📋 Dados Detalhados")

st.dataframe(df_filtrado, use_container_width=True)

# --- SIDEBAR INFO ---
st.sidebar.markdown("---")
st.sidebar.markdown(f"📊 **Registros filtrados:** {len(df_filtrado)}")
