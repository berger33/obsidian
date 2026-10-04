---
id: software.criacao_ia.tranche01.000038
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

# ML-Agents: iniciar treinamento reproduzível

## Em uma frase

O comando `mlagents-learn` usa configuração de comportamento, identificador de execução e ambiente pronto para coletar experiências.

## Por que importa

Rastrear execução evita sobrescrever resultados e permite relacionar parâmetros ao modelo que será avaliado.

## Como funciona

Versione arquivo YAML, código da cena e identificador do experimento; guarde logs e checkpoints fora de pastas temporárias.

## Exemplo

Uma corrida chamada `npc-arena-seed12` usa uma configuração registrada e salva modelo exportado com a referência da revisão de código.

## Limites e trade-offs

O mesmo identificador ou configuração não garante resultados idênticos se seed, dependências e ambiente divergirem.

## Como verificar

Repita uma corrida curta com o mesmo commit e configuração, conferindo logs, caminho de saída e carregamento do checkpoint.

## Conexões
- [[ml-agents-criar-cena-de-treinamento-representativa]] — ML-Agents: criar cena de treinamento representativa.
- [[ml-agents-configurar-ppo-ou-sac-por-evidencia]] — ML-Agents: configurar PPO ou SAC por evidência.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
