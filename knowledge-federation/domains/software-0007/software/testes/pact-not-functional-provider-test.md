---
id: software.testes.tranche09.000262
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://docs.pact.io/consumer", "https://docs.pact.io/provider"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: não usar contrato como teste funcional do provider

## Em uma frase
Pact verifica entendimento compartilhado de requests e responses de interações consumer-provider, não todas as regras funcionais do serviço.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. Empilhar regras de negócio do provider em contratos amplia o número de interações e acopla consumer a detalhes que não afetam seu uso.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Mantenha cenários de comportamento interno na suíte funcional do provider e use Pact para requests e respostas observáveis pelo consumer.

## Exemplo
O contrato confirma que o endpoint devolve os campos consumidos; outro teste do provider verifica autorização e regra de elegibilidade completa.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. Um efeito colateral de uma verificação pode revelar defeito do provider, mas não muda o propósito nem a cobertura sistemática do teste.

## Como verificar
Compare cada expectativa do pact ao código cliente e pergunte qual quebra de compatibilidade do consumer seria detectada por ela.

## Conexões
- [[pact-matchers-consumer-relevant]] — Veja também: Pact: escolher matchers por relevância para o consumidor.
- [[pact-provider-verify-local-instance]] — Veja também: Pact: verificar contracts contra instância local do provider.

## Fontes
- [Pact — Writing consumer tests](https://docs.pact.io/consumer) — escopo de testes consumer, matching e evitar testes funcionais do provider; consultado em 2026-10-02.
- [Pact — Verifying pacts](https://docs.pact.io/provider) — verificação local do provider, stubs downstream e publicação de resultados; consultado em 2026-10-02.
