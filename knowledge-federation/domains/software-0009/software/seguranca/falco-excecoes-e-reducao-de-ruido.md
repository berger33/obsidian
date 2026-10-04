---
id: software.seguranca.tranche17.001668
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

# Falco: Exceções e redução de ruído

## Em uma frase
**Falco — Exceções e redução de ruído:** Exclusões devem refletir comportamento legítimo conhecido e ficar estreitas o suficiente para manter detecção.

## Por que importa
O recorte de **exceções e redução de ruído** ajuda a identificar comportamentos de risco no host ou container e encaminhar alertas acionáveis para resposta. A equipe registra risco, evidência e responsável.

## Como funciona
Para **exceções e redução de ruído**, uma fonte de eventos emite dados; regras correlacionadas àquela fonte avaliam condições e produzem alertas com prioridade e contexto. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Adicione exceção contextual para ferramenta de manutenção de staging e preserve alerta para processo não autorizado. Teste em staging autorizado.

## Limites e trade-offs
Exceção global por binário pode esconder comportamento abusivo com mesmo executável. Exceções exigem responsável e prazo.

## Como verificar
Teste exceção com processo autorizado e variação de usuário, caminho e container. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[falco-privilegio-de-coleta-e-superficie-do-agente]] — Complementa o tópico com falco: privilégio de coleta e superfície do agente.

## Fontes
- [Falco — Event Sources](https://falco.org/docs/concepts/event-sources/) — documentação oficial sobre origens de eventos e avaliação por fonte; consultado em 2026-10-04.
- [Falco — Default Rules](https://falco.org/docs/reference/rules/default-rules/) — catálogo oficial de regras padrão, maturidade, condições e prioridades; consultado em 2026-10-04.
