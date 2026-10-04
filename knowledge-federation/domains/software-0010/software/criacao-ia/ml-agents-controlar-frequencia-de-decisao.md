---
id: software.criacao_ia.tranche01.000036
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

# ML-Agents: controlar frequência de decisão

## Em uma frase

Decisão a cada frame não é sempre necessária; período de decisão e ação repetida alteram custo e dinâmica do controle.

## Por que importa

Frequência adequada economiza treinamento sem eliminar reações que são críticas para movimentos rápidos.

## Como funciona

Escolha intervalo de decisão considerando física e controle, mantenha a ação aplicada nos passos intermediários e meça estabilidade.

## Exemplo

Um NPC que planeja rota pode decidir poucas vezes por segundo, enquanto um personagem que equilibra corpo exige comandos frequentes.

## Limites e trade-offs

Período grande atrasa resposta; período pequeno aumenta volume de passos e pode alterar a tarefa aprendida.

## Como verificar

Compare latência e sucesso em frequências distintas e inspecione colisões, oscilação e tempo até reagir a um evento.

## Conexões
- [[ml-agents-encerrar-e-reiniciar-episodios]] — ML-Agents: encerrar e reiniciar episódios.
- [[ml-agents-criar-cena-de-treinamento-representativa]] — ML-Agents: criar cena de treinamento representativa.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
