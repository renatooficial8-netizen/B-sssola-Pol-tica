import streamlit as st

st.set_page_config(
    page_title="Menos Pior - Escolha para Presidente (2º Turno)",
    page_icon="⚖️",
    layout="centered",
)

st.title(
    "⚖️ Lula x Flávio: Qual é o mais compatível com o seu perfil"
    " socioeconômico?"
)
st.write(
    "Ferramenta analítica baseada em perfis socioeconômicos, cruzando"
    " **histórico político** e **trechos oficiais dos planos de governo"
    " (TSE)**."
)

st.divider()

# 1. Seleção de Perfil do Usuário
perfil_usuario = st.selectbox(
    "Qual é a sua principal ocupação ou perfil socioeconômico atual?",
    [
        "Selecione...",
        "Trabalhador CLT",
        "Micro e Pequeno Empresário",
        "Servidor Público",
        "Profissional Liberal",
        "Estudante Universitário",
        "Desempregado",
        "Aposentado",
    ],
)

# 2. Pautas e Pesos por Perfil (1 a 5)
pautas_por_perfil = {
    "Trabalhador CLT": {
        "protecao_trabalhista": 5,
        "desburocratizacao_empresas": 2,
        "valorizacao_servico_publico": 3,
        "liberdade_economica": 2,
        "investimento_social_educacao": 3,
        "soberania_nacional": 5,
    },
    "Micro e Pequeno Empresário": {
        "protecao_trabalhista": 3,
        "desburocratizacao_empresas": 4,
        "valorizacao_servico_publico": 2,
        "liberdade_economica": 4,
        "investimento_social_educacao": 3,
        "soberania_nacional": 5,
    },
    "Servidor Público": {
        "protecao_trabalhista": 4,
        "desburocratizacao_empresas": 1,
        "valorizacao_servico_publico": 5,
        "liberdade_economica": 2,
        "investimento_social_educacao": 4,
        "soberania_nacional": 5,
    },
    "Profissional Liberal": {
        "protecao_trabalhista": 2,
        "desburocratizacao_empresas": 3,
        "valorizacao_servico_publico": 2,
        "liberdade_economica": 3,
        "investimento_social_educacao": 3,
        "soberania_nacional": 5,
    },
    "Estudante Universitário": {
        "protecao_trabalhista": 3,
        "desburocratizacao_empresas": 2,
        "valorizacao_servico_publico": 4,
        "liberdade_economica": 2,
        "investimento_social_educacao": 5,
        "soberania_nacional": 5,
    },
    "Desempregado": {
        "protecao_trabalhista": 4,
        "desburocratizacao_empresas": 2,
        "valorizacao_servico_publico": 3,
        "liberdade_economica": 1,
        "investimento_social_educacao": 5,
        "soberania_nacional": 4,
    },
    "Aposentado": {
        "protecao_trabalhista": 3,
        "desburocratizacao_empresas": 1,
        "valorizacao_servico_publico": 4,
        "liberdade_economica": 1,
        "investimento_social_educacao": 4,
        "soberania_nacional": 5,
    },
}

# 3. Posições dos candidatos refinadas
perfis_candidatos = {
    "Lula": {
        "protecao_trabalhista": 5,
        "desburocratizacao_empresas": 4,
        "valorizacao_servico_publico": 4,
        "liberdade_economica": 3,
        "investimento_social_educacao": 4,
        "soberania_nacional": 4,
    },
    "Flávio": {
        "protecao_trabalhista": 2,
        "desburocratizacao_empresas": 5,
        "valorizacao_servico_publico": 2,
        "liberdade_economica": 5,
        "investimento_social_educacao": 3,
        "soberania_nacional": 2,
    },
}

link_tse = "https://divulgacandcontas.tse.jus.br/divulga/#/candidato/BR/BR/2040602022"

# 4. Detalhamento estruturado com todas as vírgulas garantidas entre os blocos
detalhes_por_perfil = {
    "Trabalhador CLT": {
        "Lula": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Defesa de mais regulação"
                " estatal nas relações de trabalho, valorização de convenções"
                " coletivas e debates sobre jornada.",
                "**Histórico Pretérito:** Manutenção e defesa de direitos"
                " históricos na CLT e política de ganho real para o salário"
                " mínimo.",
            ],
            "link": link_tse,
        },
        "Flávio": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Foco na autonomia"
                " contratual entre patrão e empregado e desoneração da folha.",
                "**Histórico Parlamentar:** Postura contrária a intervenções"
                " rígidas na jornada de trabalho (oposição a imposições como o"
                " fim obrigatório da escala 6x1 por via legislativa direta).",
            ],
            "link": link_tse,
        },
    },
    "Micro e Pequeno Empresário": {
        "Lula": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Proposta de ampliação de"
                " crédito subsidiado e fomento ao consumo interno.",
                "**Histórico Pretérito:** Criação histórica do marco legal do"
                " **MEI** em 2008.",
            ],
            "link": link_tse,
        },
        "Flávio": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Enfoque em redução de"
                " burocracias e simplificação tributária.",
                "**Histórico Parlamentar:** Propostas de facilitação de crédito"
                " microempresarial e menor intervenção regulatória.",
            ],
            "link": link_tse,
        },
    },
    "Servidor Público": {
        "Lula": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Fortalecimento dos órgãos"
                " públicos e valorização do funcionalismo.",
                "**Histórico Pretérito:** Oposição a reformas administrativas"
                " redutoras de garantias.",
            ],
            "link": link_tse,
        },
        "Flávio": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Defesa de reforma"
                " administrativa com foco no teto de gastos.",
                "**Histórico Parlamentar:** Atuação voltada ao corte de"
                " privilégios e limitação de despesas públicas.",
            ],
            "link": link_tse,
        },
    },
    "Profissional Liberal": {
        "Lula": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Foco na reindustrialização e"
                " mercado interno.",
                "**Histórico Pretérito:** Expansão do crédito geral e consumo.",
            ],
            "link": link_tse,
        },
        "Flávio": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Autonomia jurídica e"
                " facilidades para o regime PJ.",
                "**Histórico Parlamentar:** Apoio a desonerações fiscais e menor"
                " burocracia profissional.",
            ],
            "link": link_tse,
        },
    },
    "Estudante Universitário": {
        "Lula": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Expansão de federais e"
                " reajuste de bolsas.",
                "**Histórico Pretérito:** Histórico de forte expansão da rede"
                " federal superior.",
            ],
            "link": link_tse,
        },
        "Flávio": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Parcerias público-privadas"
                " na educação e gestão eficiente.",
                "**Histórico Parlamentar:** Defesa de autonomia gerencial das"
                " instituições.",
            ],
            "link": link_tse,
        },
    },
    "Desempregado": {
        "Lula": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Ênfase em transferência de"
                " renda e obras públicas.",
                "**Histórico Pretérito:** Governos marcados por fortes programas"
                " sociais.",
            ],
            "link": link_tse,
        },
        "Flávio": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Desregulamentação e"
                " atração de capital privado.",
                "**Histórico Parlamentar:** Apoio a privatizações e reformas"
                " liberais.",
            ],
            "link": link_tse,
        },
    },
    "Aposentado": {
        "Lula": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Valorização do salário"
                " mínimo e reforço do SUS.",
                "**Histórico Pretérito:** Política de recuperação do poder de"
                " compra dos benefícios.",
            ],
            "link": link_tse,
        },
        "Flávio": {
            "pontos": [
                "**Ancoragem no Plano de Governo:** Responsabilidade fiscal e"
                " controle inflacionário.",
                "**Histórico Parlamentar:** Apoio a reformas de ajuste fiscal.",
            ],
            "link": link_tse,
        },
    },
}

st.divider()

# 5. Processamento e Exibição
if perfil_usuario != "Selecione...":
  if st.button("Calcular com base em Histórico e Propostas", type="primary"):
    respostas_usuario = pautas_por_perfil[perfil_usuario]

    distancias = {}
    for candidato, pautas in perfis_candidatos.items():
      distancia_total = sum(
          abs(respostas_usuario[pauta] - pautas[pauta])
          for pauta in respostas_usuario
      )
      distancias[candidato] = distancia_total

    inversos = {cand: 1.0 / (dist + 1) for cand, dist in distancias.items()}
    soma_inversos = sum(inversos.values())

    resultados = {
        cand: round((inv / soma_inversos) * 100, 2)
        for cand, inv in inversos.items()
    }

    st.subheader(f"📊 Resultado da Análise Proporcional para: {perfil_usuario}")
    for candidato, afinidade in resultados.items():
      st.write(f"- **{candidato}**: {afinidade}% de compatibilidade")

    candidato_mais_proximo = max(resultados, key=resultados.get)
    st.success(
        f"Com base no cruzamento entre o seu perfil, os planos de governo"
        f" oficiais e o histórico político, o candidato com maior"
        f" proximidade proporcional é: **{candidato_mais_proximo}**."
    )

    st.divider()
    st.markdown(
        f"### 🔍 Ancoragem Documental e Histórico Parlamentar para:"
        f" **{perfil_usuario}**"
    )

    for candidato, dados in detalhes_por_perfil[perfil_usuario].items():
      with st.expander(f"Ver propostas e histórico de {candidato}"):
        for item in dados["pontos"]:
          st.markdown(f"- {item}")
        st.markdown(
            f"🔗 **[Acessar o Plano de Governo Oficial de {candidato} no"
            f" TSE]({dados['link']})**"
        )
else:
  st.info("👆 Por favor, selecione uma categoria acima para prosseguir.")

# --- Rodapé com Assinatura ---
st.divider()
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 0.9em;'>"
    "Criado por <strong>Renato Silva Ortega</strong> | "
    "📸 Siga no Instagram: <a href='https://www.instagram.com/renatoter9' "
    "target='_blank'>Renato</a>"
    "</div>",
    unsafe_allow_html=True,
)
