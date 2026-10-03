---
id: software.testes.tranche23.001739
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://hyperfoil.io/docs/", "https://hyperfoil.io/docs/overview/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Fora do YAML: REST API OpenAPI, steps customizados em JVM e guia de migração

## Em uma frase
O índice oficial da documentação organiza o produto em nove seções, e três delas definem o teto de extensibilidade: Controller API (OpenAPI 3 specification do controller), Extensions (como desenvolver suas próprias extensões) e Custom components no Quickstart 8 — a porta para escrever a lógica em Java "ou qualquer outra linguagem JVM" quando o DSL YAML aperta, além da seção Migration para quem vem de outras ferramentas.

## Por que importa
Um framework de benchmark vive ou morre pela cobertura de protocolo; a doc assume explicitamente que o YAML é a camada de entrada, não a única, e o Overview repete o compromisso com o DSL: "we're not trying to invent a new programming language" — quando o cenário precisa de lógica, você programa, não luta com o formato.

## Como funciona
A superfície REST documentada (OpenAPI) significa que subir, iniciar e acompanhar runs é scriptável de qualquer linguagem HTTP — a mesma API que o CLI usa internamente contra o start-local do quickstart.

## Exemplo
Abra a página Controller API da doc e valide que existe especificação OpenAPI; no seu projeto, gere um client a partir dela e suba um benchmark pelo endpoint REST em vez do CLI.

## Limites e trade-offs
O índice documenta a existência das seções, não o conteúdo de cada uma — os detalhes do contrato REST (paths, payloads, paginação de stats) estão na especificação hospedada, e as versões da doc podem divergir do release binário local.

## Como verificar
Confirme no índice da documentação as nove seções nomeadas e a frase sobre a linguagem do DSL na seção Versatility do Overview.

## Conexões
- [[hyperfoil-stats]] — Veja também: O stats por dentro: percentis, classes de status e os contadores de erro.

## Fontes
- [Hyperfoil — índice da documentação](https://hyperfoil.io/docs/) — nove seções: overview, quickstarts, user guide, API REST, extensions; consultado em 2026-10-03.
- [Hyperfoil — Overview](https://hyperfoil.io/docs/overview/) — licença, distribuição, acurácia e versatilidade do DSL; consultado em 2026-10-03.
