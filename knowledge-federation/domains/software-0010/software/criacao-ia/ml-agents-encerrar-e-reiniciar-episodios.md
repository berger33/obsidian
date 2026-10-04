---
id: software.criacao_ia.tranche01.000035
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

# ML-Agents: encerrar e reiniciar episódios

## Em uma frase

Um episódio precisa terminar em sucesso, falha ou limite definido e voltar a um estado inicial consistente.

## Por que importa

Reset mal implementado mistura experiências de tentativas diferentes e corrompe o aprendizado do agente.

## Como funciona

No início, reinicialize posição, objetivos, física e aleatoriedade; no término, registre o motivo e limpe efeitos transitórios.

## Exemplo

Um inimigo reinicia a arena e a vida do alvo após colisão terminal, sorteando uma posição inicial dentro de limites válidos.

## Limites e trade-offs

Se a distribuição de reset for estreita, a política pode decorar posições; reiniciar cedo demais pode eliminar sinais de conclusão.

## Como verificar

Repita episódios com sementes fixas e variáveis e compare estado inicial, término e limpeza de objetos em cada reinicialização.

## Conexões
- [[ml-agents-desenhar-recompensas]] — ML-Agents: desenhar recompensas.
- [[ml-agents-controlar-frequencia-de-decisao]] — ML-Agents: controlar frequência de decisão.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
