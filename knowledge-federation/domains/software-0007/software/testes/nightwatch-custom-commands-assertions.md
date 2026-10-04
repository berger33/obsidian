---
id: software.testes.tranche21.001466
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://nightwatchjs.org/guide/reference/settings.html", "https://github.com/nightwatchjs/nightwatch"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nightwatch: estender com comandos e asserções próprios

## Em uma frase
As chaves custom_commands_path e custom_assertions_path registram pastas de comandos e asserções definidos pelo projeto, anexados à API do teste.

## Por que importa
Repetir sequências de cliques e verificações em dez arquivos é uma escolha, não uma obrigação: o que se repete pode virar primitiva nomeada.

## Como funciona
Implemente o comando com a assinatura esperada pelo Nightwatch, coloque o arquivo na pasta registrada e chame-o como qualquer comando nativo da API.

## Exemplo
Um comando entrarSistema pode encapsular navegação, preenchimento e envio, deixando o teste legível como uma frase de negócio.

## Limites e trade-offs
Comandos demais escondem a interação real do teste; uma asserção própria precisa de mensagem de erro clara, senão a falha vira mistério.

## Como verificar
Chame o comando customizado em um teste mínimo e confirme que aparece na API do cliente sem importação explícita.

## Conexões
- [[nightwatch-page-objects-path]] — Veja também: Nightwatch: página de objetos pelo caminho.
- [[nightwatch-parallel-test-workers]] — Veja também: Nightwatch: executar suítes em paralelo.

## Fontes
- [Nightwatch — Referência de Config Settings](https://nightwatchjs.org/guide/reference/settings.html) — chaves de configuração, ambientes, runner, workers e capturas; consultado em 2026-10-03.
- [Nightwatch — repositório oficial](https://github.com/nightwatchjs/nightwatch) — código-fonte, releases e documentação do projeto; consultado em 2026-10-03.
