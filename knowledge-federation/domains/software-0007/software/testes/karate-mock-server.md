---
id: software.testes.tranche15.000917
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://karatelabs.github.io/karate/#mock-server", "https://karatelabs.github.io/karate/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karate: simular serviços com o servidor mock

## Em uma frase
O servidor mock do Karate descreve rotas, respostas e validações em feature files, cobrindo contratos antes de o serviço real existir.

## Por que importa
Testes de integração que dependem de terceiros ficam lentos e instáveis, e um mock descrito na mesma linguagem dos testes reduz a distância entre contrato e verificação.

## Como funciona
Descreva cenários de caminho felizes e de erro no mock, configure o servidor para responder em porta disponível e aponte a suíte para ele no ambiente de teste.

## Exemplo
Um mock pode responder com sucesso e depois com falha segundo o estado da requisição, exercitando o tratamento de erro do consumidor.

## Limites e trade-offs
Um mock que não valida a requisição recebida pode aceitar chamadas erradas e dar falsa confiança; o contrato precisa cobrir também os campos obrigatórios.

## Como verificar
Compare a resposta do mock com a documentação do serviço real e execute um cenário de erro para confirmar que o consumidor reage como esperado.

## Conexões
- [[karate-tags-selection]] — Veja também: Karate: selecionar cenários por tags.
- [[karate-print-and-debug]] — Veja também: Karate: registrar evidências do passo.

## Fontes
- [Karate — Mock server](https://karatelabs.github.io/karate/#mock-server) — servidor mock baseado em feature files para contratos e testes; consultado em 2026-10-02.
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
