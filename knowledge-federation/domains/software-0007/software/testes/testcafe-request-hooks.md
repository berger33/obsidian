---
id: software.testes.tranche19.001274
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://testcafe.io/documentation", "https://github.com/DevExpress/testcafe"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestCafe: controlar requisições com ganchos

## Em uma frase
Ganchos de requisição permitem observar, simular e substituir chamadas de rede, incluindo atrasos e códigos de erro.

## Por que importa
Simular respostas torna verificáveis os estados de erro e carregamento que dependem de serviços externos.

## Como funciona
Registre ganchos por caso ou por fixture, simule respostas específicas e sempre remova o gancho ao final.

## Exemplo
Um gancho pode responder com erro do servidor para verificar a mensagem exibida ao usuário na falha de carregamento.

## Limites e trade-offs
Ganchos que permanecem ativos contaminam casos seguintes, e simulações que não refletem o contrato real escondem incompatibilidades.

## Como verificar
Simule um código de erro e confirme que a interface exibe o tratamento previsto para a falha.

## Conexões
- [[testcafe-client-functions]] — Veja também: TestCafe: executar código no contexto da página.
- [[testcafe-parallelism-and-browsers]] — Veja também: TestCafe: distribuir execução e escolher navegadores.

## Fontes
- [TestCafe — Documentação](https://testcafe.io/documentation) — guias de início, execução, depuração e relatórios; consultado em 2026-10-03.
- [TestCafe — repositório oficial](https://github.com/DevExpress/testcafe) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
