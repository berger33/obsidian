---
id: software.testes.tranche09.000261
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
fontes: ["https://docs.pact.io/consumer", "https://docs.pact.io/getting_started/terminology"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: escolher matchers por relevância para o consumidor

## Em uma frase
Matching deve ser exato quando o consumer depende do valor e flexível quando apenas formato ou tipo importam.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. Matchers excessivamente rígidos criam incompatibilidade por mudanças irrelevantes; tolerância excessiva pode deixar passar quebra que o cliente não suporta.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Decida por campo qual propriedade afeta o consumer e use matcher que preserve somente essa expectativa necessária.

## Exemplo
O teste exige formato específico para URL usada como link, mas aceita qualquer identificador do tipo string em campo apenas exibido.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. Correspondência flexível não substitui validação de esquema e uma regra genérica pode não refletir a semântica da aplicação.

## Como verificar
Introduza uma mudança controlada em cada campo e confirme que somente alterações incompatíveis com o consumer fazem a verificação falhar.

## Conexões
- [[pact-consumer-request-as-sent]] — Veja também: Pact: capturar a requisição que o cliente realmente envia.
- [[pact-not-functional-provider-test]] — Veja também: Pact: não usar contrato como teste funcional do provider.

## Fontes
- [Pact — Writing consumer tests](https://docs.pact.io/consumer) — escopo de testes consumer, matching e evitar testes funcionais do provider; consultado em 2026-10-02.
- [Pact — Terminology](https://docs.pact.io/getting_started/terminology) — interactions, contracts, provider states e verificação; consultado em 2026-10-02.
