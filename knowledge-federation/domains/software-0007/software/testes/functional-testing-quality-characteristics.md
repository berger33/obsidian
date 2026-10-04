---
id: software.testes.functional.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md"
revisor: ""
fontes: ["https://astqb.org/2-2-test-levels-and-test-types/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Functional testing", "Teste funcional verifica o que o sistema deve fazer"]
lote: software-testes-2000-0001
---

# Teste funcional verifica o que o sistema deve fazer

## Em uma frase
Teste funcional avalia as funções que um componente ou sistema deve executar, em relação ao comportamento especificado.

## Por que importa
Uma tela que abre ou um serviço que responde pode ainda violar regras de negócio, produzir dado incorreto ou omitir comportamento requerido. Verificar função exige comparar resultado com base e critérios definidos.

## Como funciona
O CTFL trata funcionalidades como “o que” o objeto de teste deve fazer e descreve completude funcional, correção funcional e adequação funcional como objetivos principais. Testes podem ser derivados de requisitos, user stories, contratos ou outra base aplicável e ocorrer em níveis diferentes. O tipo funcional não é um nível: funções podem ser testadas em componente, integração, sistema ou aceitação.

## Exemplo
Num fluxo de pagamento, os casos podem confirmar que uma autorização válida atualiza o estado do pedido, uma recusa mantém o pedido não pago e uma repetição segura não gera cobrança duplicada.

## Limites e trade-offs
Conformidade funcional não demonstra desempenho, segurança, usabilidade ou adequação completa a necessidades. Critérios incompletos limitam o que o teste pode concluir.

## Como verificar
Associe cada caso à função e à regra esperada; confira entradas, resultados e efeitos persistentes e complemente com tipos não funcionais relevantes.

## Conexões
- [[test-levels-overview]] — distingue tipo de teste de nível.
- [[test-objectives-context]] — relaciona evidência ao propósito.

## Fontes
- [ASTQB — CTFL §2.2.2, Test Types](https://astqb.org/2-2-test-levels-and-test-types/) — definição e objetivos de teste funcional; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.2.2; acesso em 2026-10-01.
