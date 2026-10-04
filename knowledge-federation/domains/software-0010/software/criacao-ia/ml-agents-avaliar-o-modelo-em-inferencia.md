---
id: software.criacao_ia.tranche01.000040
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

# ML-Agents: avaliar o modelo em inferência

## Em uma frase

Modelo treinado deve ser avaliado no modo de execução usado pelo jogo, com a inferência incorporada ao projeto Unity.

## Por que importa

Separar inferência do treinador revela problemas de desempenho, comportamento e compatibilidade que não aparecem durante a coleta.

## Como funciona

Carregue o modelo exportado conforme documentação vigente, use configuração de Behavior compatível e execute a cena sem conexão de treinamento.

## Exemplo

Uma build de NPC usa Sentis para inferir ações localmente e registra taxa de vitória contra baseline fixa.

## Limites e trade-offs

Bom retorno no treino pode ser sobreajuste; mudança de versão, plataforma ou observações pode alterar a inferência.

## Como verificar

Teste em builds alvo e episódios nunca usados na otimização, medindo desempenho, latência e falhas de carregamento.

## Conexões
- [[ml-agents-configurar-ppo-ou-sac-por-evidencia]] — ML-Agents: configurar PPO ou SAC por evidência.
- [[unreal-separar-behavior-tree-e-blackboard]] — Unreal: separar Behavior Tree e Blackboard.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
