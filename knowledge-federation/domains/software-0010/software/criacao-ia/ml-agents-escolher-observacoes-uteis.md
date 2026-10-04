---
id: software.criacao_ia.tranche01.000032
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

# ML-Agents: escolher observações úteis

## Em uma frase

Observações são os dados que o agente consegue usar para inferir o estado relevante da cena, por sensores vetoriais ou visuais.

## Por que importa

Sinais incompletos tornam a tarefa impossível; sinais redundantes ou vazados podem permitir atalhos que não existem na partida real.

## Como funciona

Inclua posições relativas, velocidade e eventos que o personagem poderia perceber, normalizando escalas quando isso fizer sentido.

## Exemplo

Um robô de dungeon recebe direção para a porta e leituras de obstáculos próximos, não a localização de inimigos ocultos pelo mapa.

## Limites e trade-offs

Mais observações elevam custo e podem criar dependência de informação privilegiada que quebra ao mudar a cena.

## Como verificar

Visualize o vetor em estados contrastantes e teste se a política ainda funciona com pequenas variações e informação removida.

## Conexões
- [[ml-agents-estruturar-um-agent]] — ML-Agents: estruturar um Agent.
- [[ml-agents-mapear-acoes-ao-gameplay]] — ML-Agents: mapear ações ao gameplay.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
