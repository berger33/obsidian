---
id: software.testes.tranche22.001649
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://github.com/SpectoLabs/hoverfly/blob/master/README.md", "https://docs.hoverfly.io/en/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hoverfly: build e testes de contribuição

## Em uma frase
Desenvolver no Hoverfly é Go puro: clonar o repo, make build e os binários caem em target/; make test roda as suítes unitárias e funcionais do projeto — algumas de middleware pedem ruby e python no ambiente.

## Por que importa
A seção de contribuição do README fixa o fluxo de fork → branch → PR com descrição do porquê, como testar e que testes foram feitos, o formato mínimo para uma PR sobrevivente.

## Como funciona
brew install ruby && brew install python aparece como pré-requisito para os middleware tests no macOS, sinal de que o produto testa seus próprios contratos de middleware com dois interpretadores.

## Exemplo
Instalação antiga de Go via apt-get ou homebrew deve ser removida antes de seguir as instruções oficiais do site do Go — o README chama isso explicitamente.

## Limites e trade-offs
O projeto é Apache 2 com copyright da Hoverfly Cloud; verifique o arquivo LICENSE antes de redistribuir binários em artefatos corporativos.

## Como verificar
Rode make test num clone limpo com ruby e python presentes e confirme que as suítes de middleware não entram na lista de pulos.

## Conexões
- [[hoverfly-java-bindings]] — Veja também: Hoverfly: binding Java e middleware de qualquer linguagem.

## Fontes
- [Hoverfly — README oficial](https://github.com/SpectoLabs/hoverfly/blob/master/README.md) — proposta, quickstart, build em Go e contribuição; consultado em 2026-10-03.
- [Hoverfly — documentação inicial](https://docs.hoverfly.io/en/latest/index.html) — conceitos-chave, reference e troubleshooting do v1.12.15; consultado em 2026-10-03.
