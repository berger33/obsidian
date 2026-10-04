---
id: software.criacao_ia.tranche01.000034
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

# ML-Agents: desenhar recompensas

## Em uma frase

A recompensa informa ao algoritmo se a transição observada aproxima ou afasta o agente do objetivo definido.

## Por que importa

Um sinal mal desenhado pode ensinar exploração da própria métrica em vez da tarefa de jogo pretendida.

## Como funciona

Comece com objetivo e penalidades mínimos, atribua retorno em eventos observáveis e documente que comportamento cada sinal incentiva.

## Exemplo

Num puzzle, recompense resolver a sala e penalize passos redundantes somente se isso não bloquear exploração necessária.

## Limites e trade-offs

Recompensas densas podem criar atalhos e pesos arbitrários; sinais esparsos podem tornar a aprendizagem mais lenta.

## Como verificar

Revise trajetórias completas, procure estratégias inesperadas e compare sucesso real da tarefa com a soma de recompensas.

## Conexões
- [[ml-agents-mapear-acoes-ao-gameplay]] — ML-Agents: mapear ações ao gameplay.
- [[ml-agents-encerrar-e-reiniciar-episodios]] — ML-Agents: encerrar e reiniciar episódios.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
