---
id: software.testes.tranche13.000656
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://mochajs.org/features/timeouts/", "https://mochajs.org/features/hooks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: dimensionar timeout de teste e hook

## Em uma frase
Mocha aplica limite de duração a testes e hooks, e o valor pode ser configurado em níveis diferentes.

## Por que importa
Um limite curto detecta bloqueio, mas um limite que ignora setup lento pode falhar antes da assertion que se queria observar.

## Como funciona
Use o menor prazo coerente com o contrato do cenário, configure hooks demorados separadamente se necessário e trate `this.timeout(0)` como desativação deliberada, não como ajuste universal.

## Exemplo
Uma integração HTTP pode ter prazo maior que um teste puro, enquanto o hook que inicia o servidor mantém prazo próprio para reportar prontidão.

## Limites e trade-offs
Timeout não cancela automaticamente trabalho externo que seu código deixou solto. Um callback que nunca conclui precisa ser investigado, não apenas receber prazo ilimitado.

## Como verificar
Faça o teste ultrapassar o limite em uma fixture descartável e confirme que o diagnóstico identifica o caso ou hook responsável.

## Conexões
- [[mocha-retry-diagnostic]] — Veja também: Mocha: usar retries como evidência de instabilidade.
- [[mocha-grep-focused-suite]] — Veja também: Mocha: filtrar casos sem deixar foco acidental.

## Fontes
- [Mocha — Timeouts](https://mochajs.org/features/timeouts/) — timeout scope for tests and hooks; consultado em 2026-10-02.
- [Mocha — Hooks](https://mochajs.org/features/hooks/) — nested setup/teardown hooks and async hook behavior; consultado em 2026-10-02.
