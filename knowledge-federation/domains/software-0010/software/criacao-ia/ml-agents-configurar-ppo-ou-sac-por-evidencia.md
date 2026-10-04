---
id: software.criacao_ia.tranche01.000039
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

# ML-Agents: configurar PPO ou SAC por evidência

## Em uma frase

Os treinadores PPO e SAC têm pressupostos e configurações diferentes; seleção deve acompanhar o tipo de ação e o sinal de aprendizagem.

## Por que importa

Escolher por familiaridade pode desperdiçar tempo de simulação ou produzir instabilidade difícil de diagnosticar.

## Como funciona

Use exemplos oficiais como ponto inicial, altere poucos hiperparâmetros de cada vez e mantenha experimentos comparáveis.

## Exemplo

Para controle contínuo, compare uma baseline documentada com alternativa apropriada, em vez de ajustar taxa, lote e rede simultaneamente.

## Limites e trade-offs

Valores de exemplo não são recomendação universal e podem mudar entre versões do toolkit.

## Como verificar

Compare taxa de conclusão, variância entre execuções e custo de treinamento em várias sementes antes de escolher configuração.

## Conexões
- [[ml-agents-iniciar-treinamento-reproduzivel]] — ML-Agents: iniciar treinamento reproduzível.
- [[ml-agents-avaliar-o-modelo-em-inferencia]] — ML-Agents: avaliar o modelo em inferência.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
