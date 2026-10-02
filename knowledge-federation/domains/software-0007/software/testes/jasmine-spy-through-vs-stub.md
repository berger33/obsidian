---
id: software.testes.tranche13.000664
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
fontes: ["https://jasmine.github.io/api/7.0/Spy", "https://jasmine.github.io/api/7.0/SpyStrategy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jasmine: distinguir spy que observa de spy com resposta

## Em uma frase
Um spy pode registrar chamadas e também ser configurado para executar a implementação original ou devolver comportamento falso.

## Por que importa
Separar observação de substituição esclarece se o spec está verificando colaboração real ou isolando uma dependência.

## Como funciona
Use `spyOn` para instrumentar método existente, `and.callThrough()` quando precisa preservar seu efeito e `and.returnValue()` quando o contrato do exemplo requer uma resposta controlada.

## Exemplo
Um teste pode observar que o componente pede um preço sem consultar API real, configurando o spy para devolver um valor conhecido.

## Limites e trade-offs
Um spy que chama método real mantém efeitos colaterais; se o método escreve no banco ou altera estado global, a configuração não é isolamento por si só.

## Como verificar
Verifique o contador e os argumentos da chamada, depois confirme se o método real foi ou não executado conforme a strategy escolhida.

## Conexões
- [[jasmine-mock-date-time]] — Veja também: Jasmine: alinhar new Date ao relógio simulado.
- [[jasmine-spy-call-history]] — Veja também: Jasmine: inspecionar histórico de chamadas de spy.

## Fontes
- [Jasmine 7 — Spy](https://jasmine.github.io/api/7.0/Spy) — spy calls and call-tracking API; consultado em 2026-10-02.
- [Jasmine 7 — SpyStrategy](https://jasmine.github.io/api/7.0/SpyStrategy) — fake, callThrough and return-value strategies; consultado em 2026-10-02.
