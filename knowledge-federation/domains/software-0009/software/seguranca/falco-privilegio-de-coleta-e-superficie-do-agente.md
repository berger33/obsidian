---
id: software.seguranca.tranche17.001669
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

# Falco: Privilégio de coleta e superfície do agente

## Em uma frase
**Falco — Privilégio de coleta e superfície do agente:** Coletar eventos do kernel pode exigir capacidades elevadas; a implantação deve minimizar privilégios e acesso aos dados.

## Por que importa
O recorte de **privilégio de coleta e superfície do agente** ajuda a identificar comportamentos de risco no host ou container e encaminhar alertas acionáveis para resposta. A equipe registra risco, evidência e responsável.

## Como funciona
Para **privilégio de coleta e superfície do agente**, uma fonte de eventos emite dados; regras correlacionadas àquela fonte avaliam condições e produzem alertas com prioridade e contexto. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Compare modo de deployment recomendado com modo privilegiado em cluster não produtivo e documente requisitos do driver. Teste em staging autorizado.

## Limites e trade-offs
Reduzir privilégios pode limitar fontes; ampliar acesso sem threat model cria novo componente sensível. Exceções exigem responsável e prazo.

## Como verificar
Use benchmark de capabilities, host mounts e permissões do agente contra a configuração aprovada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[falco-validacao-de-alerta-antes-do-rollout]] — Complementa o tópico com falco: validação de alerta antes do rollout.

## Fontes
- [Falco — Event Sources](https://falco.org/docs/concepts/event-sources/) — documentação oficial sobre origens de eventos e avaliação por fonte; consultado em 2026-10-04.
- [Falco — Default Rules](https://falco.org/docs/reference/rules/default-rules/) — catálogo oficial de regras padrão, maturidade, condições e prioridades; consultado em 2026-10-04.
