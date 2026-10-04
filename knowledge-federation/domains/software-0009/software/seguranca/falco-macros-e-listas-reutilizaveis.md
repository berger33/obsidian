---
id: software.seguranca.tranche17.001664
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://falco.org/docs/concepts/event-sources/", "https://falco.org/docs/reference/rules/default-rules/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Falco: Macros e listas reutilizáveis

## Em uma frase
**Falco — Macros e listas reutilizáveis:** Macros e listas ajudam a compor condições e exceções que são compartilhadas entre regras.

## Por que importa
O recorte de **macros e listas reutilizáveis** ajuda a identificar comportamentos de risco no host ou container e encaminhar alertas acionáveis para resposta. A equipe registra risco, evidência e responsável.

## Como funciona
Para **macros e listas reutilizáveis**, uma fonte de eventos emite dados; regras correlacionadas àquela fonte avaliam condições e produzem alertas com prioridade e contexto. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Defina lista de binários conhecidos em arquivo de regras versionado e teste regra com processo permitido e desconhecido. Teste em staging autorizado.

## Limites e trade-offs
Allowlist baseada somente em nome de processo pode ser contornada por path diferente ou binário substituído. Exceções exigem responsável e prazo.

## Como verificar
Teste caminho, hash, usuário e container, além do nome, para as exceções sensíveis. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[falco-maturidade-e-selecao-das-regras]] — Complementa o tópico com falco: maturidade e seleção das regras.

## Fontes
- [Falco — Event Sources](https://falco.org/docs/concepts/event-sources/) — documentação oficial sobre origens de eventos e avaliação por fonte; consultado em 2026-10-04.
- [Falco — Default Rules](https://falco.org/docs/reference/rules/default-rules/) — catálogo oficial de regras padrão, maturidade, condições e prioridades; consultado em 2026-10-04.
