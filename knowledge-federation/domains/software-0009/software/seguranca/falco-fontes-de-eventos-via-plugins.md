---
id: software.seguranca.tranche17.001662
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

# Falco: Fontes de eventos via plugins

## Em uma frase
**Falco — Fontes de eventos via plugins:** Plugins estendem fontes além de syscall e podem ter regras aplicáveis apenas ao formato de evento correspondente.

## Por que importa
O recorte de **fontes de eventos via plugins** ajuda a identificar comportamentos de risco no host ou container e encaminhar alertas acionáveis para resposta. A equipe registra risco, evidência e responsável.

## Como funciona
Para **fontes de eventos via plugins**, uma fonte de eventos emite dados; regras correlacionadas àquela fonte avaliam condições e produzem alertas com prioridade e contexto. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Ative uma fonte de auditoria Kubernetes em staging e avalie regra vinculada explicitamente a essa fonte. Teste em staging autorizado.

## Limites e trade-offs
Falco não correlaciona automaticamente eventos de fontes diferentes, então uma regra não substitui SIEM para correlação cruzada. Exceções exigem responsável e prazo.

## Como verificar
Valide instalação do plugin, nome da fonte e regra disparada por uma entrada de teste. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[falco-condicao-e-saida-da-regra]] — Complementa o tópico com falco: condição e saída da regra.

## Fontes
- [Falco — Event Sources](https://falco.org/docs/concepts/event-sources/) — documentação oficial sobre origens de eventos e avaliação por fonte; consultado em 2026-10-04.
- [Falco — Default Rules](https://falco.org/docs/reference/rules/default-rules/) — catálogo oficial de regras padrão, maturidade, condições e prioridades; consultado em 2026-10-04.
