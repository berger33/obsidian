---
id: software.criacao_ia.tranche01.000031
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

# ML-Agents: estruturar um Agent

## Em uma frase

Um Agent conecta observações do ambiente, ações recebidas e recompensas que representam progresso numa tarefa aprendida.

## Por que importa

Separar essas responsabilidades torna possível formular o problema de gameplay como ciclo observação-decisão-ação-avaliação.

## Como funciona

Defina estado e término do episódio na cena Unity, implemente as respostas do Agent e associe-o ao Behavior Parameters apropriado.

## Exemplo

Um agente de corrida observa velocidade e distância da curva, escolhe direção e recebe retorno por completar voltas sem colisão.

## Limites e trade-offs

O ciclo não garante que o comportamento aprendido seja divertido, justo ou útil fora da distribuição de treino.

## Como verificar

Registre observações, ações e retorno em episódios curtos e confirme que cada interação corresponde ao estado esperado da simulação.

## Conexões
- [[ferramentas-testar-excecoes-e-falhas-de-execucao]] — Ferramentas: testar exceções e falhas de execução.
- [[ml-agents-escolher-observacoes-uteis]] — ML-Agents: escolher observações úteis.

## Fontes
- [Unity ML-Agents 4.0 — Overview](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/) — Documentação atual da arquitetura de ambientes, agentes, observações, ações, recompensas e inferência. Consulta: 2026-10-04.
- [Unity ML-Agents 4.0 — Training ML-Agents](https://docs.unity3d.com/Packages/com.unity.ml-agents@4.0/manual/Training-ML-Agents.html) — Explica o fluxo de treinamento, configurações e execução com o pacote Python. Consulta: 2026-10-04.
