---
id: software.testes.tranche16.001049
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://hurl.dev/docs/asserting-response.html", "https://hurl.dev/docs/manual.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hurl: tratar códigos de status e falhas

## Em uma frase
A execução considera falha quando a resposta diverge do esperado, e o código de saída indica se houve erro de asserção, de execução ou de configuração.

## Por que importa
Códigos distintos permitem que o pipeline reaja de forma diferente a defeito do serviço e a problema no próprio arquivo de teste.

## Como funciona
Verifique o código de saída no pipeline, distinga as classes de erro no relatório e mantenha a linha de status alinhada ao comportamento esperado.

## Exemplo
Um passo que deve ser recusado pelo serviço pode declarar a resposta de erro correspondente, confirmando que a validação funciona.

## Limites e trade-offs
Interromper na primeira falha esconde problemas posteriores; em cenários de verificação ampla, continuar após erro pode ser mais informativo.

## Como verificar
Force um erro de asserção e outro de configuração e compare os códigos de saída produzidos em cada caso.

## Conexões
- [[hurl-assertions]] — Veja também: Hurl: escrever asserções sobre a resposta.
- [[hurl-options-block]] — Veja também: Hurl: configurar comportamento por entrada.

## Fontes
- [Hurl — Asserting response](https://hurl.dev/docs/asserting-response.html) — asserções implícitas e explícitas sobre status, cabeçalhos e corpo; consultado em 2026-10-03.
- [Hurl — Manual (CLI)](https://hurl.dev/docs/manual.html) — modo de teste, paralelismo, repetição, relatórios e códigos de saída; consultado em 2026-10-03.
