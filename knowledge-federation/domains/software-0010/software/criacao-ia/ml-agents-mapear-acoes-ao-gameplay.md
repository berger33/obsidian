---
id: software.criacao_ia.tranche01.000033
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

# ML-Agents: mapear ações ao gameplay

## Em uma frase

O espaço de ação define quais comandos contínuos ou discretos o agente pode produzir em cada decisão.

## Por que importa

Ações com semântica consistente ajudam o treinador a explorar alternativas que o motor pode executar de forma previsível.

## Como funciona

Escolha ramos discretos para escolhas finitas ou valores contínuos para controle graduado e traduza-os para inputs claramente documentados.

## Exemplo

Um inimigo pode escolher entre patrulhar, investigar ou recuar, enquanto um veículo controla ângulo de direção e aceleração.

## Limites e trade-offs

Escalas erradas, ações impossíveis ou mudanças de frequência podem tornar aprendizagem instável e dificultar comparação.

## Como verificar

Rode um agente heurístico com ações extremas e confirme limites, orientação, velocidade e comportamento no frame de decisão.

## Conexões
- [[ml-agents-escolher-observacoes-uteis]] — ML-Agents: escolher observações úteis.
- [[ml-agents-desenhar-recompensas]] — ML-Agents: desenhar recompensas.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
