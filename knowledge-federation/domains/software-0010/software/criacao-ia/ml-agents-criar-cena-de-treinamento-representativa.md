---
id: software.criacao_ia.tranche01.000037
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/", "https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ML-Agents: criar cena de treinamento representativa

## Em uma frase

Uma cena de treino pode ser a própria experiência ou um ambiente simplificado construído para iterar mais depressa.

## Por que importa

Representatividade evita que o agente aprenda física, obstáculos ou objetivos que desaparecerão na build de produção.

## Como funciona

Mantenha regras e componentes relevantes equivalentes, varie parâmetros importantes e registre diferenças entre cenário de treino e release.

## Exemplo

Uma arena de combate reduz efeitos visuais para acelerar passos, mas preserva hitboxes, alcance e cooldowns do jogo final.

## Limites e trade-offs

Uma simplificação excessiva aumenta a lacuna entre treinamento e uso; cenas visualmente distintas podem mudar sensores.

## Como verificar

Execute a política na cena de produção e meça desempenho nos mesmos cenários, incluindo conteúdo e condições não vistos no treino.

## Conexões
- [[ml-agents-controlar-frequencia-de-decisao]] — ML-Agents: controlar frequência de decisão.
- [[ml-agents-iniciar-treinamento-reproduzivel]] — ML-Agents: iniciar treinamento reproduzível.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
