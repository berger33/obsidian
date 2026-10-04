---
id: software.testes.tranche22.001569
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
fontes: ["https://github.com/bats-core/bats-core/blob/master/README.md", "https://github.com/bats-core/bats-core/blob/master/docs/versions.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: do repositório parado ao fork comunitário

## Em uma frase
O Bats original de sstephenson parou de evoluir; em 19 de setembro de 2017 a comunidade forkou o projeto no commit 0360811 usando git clone --bare e --mirror para preservar o histórico, e o repositório antigo foi arquivado somente-leitura em 29 de abril de 2021.

## Por que importa
Saber a linhagem importa ao ler tutoriais antigos: sintaxe e flags publicados antes de 2017 referem-se ao upstream morto, e o canonical atual é o GitHub bats-core com docs no readthedocs.

## Como funciona
O projeto é MIT; versões anteriores à v1.2.1 têm documentação separada em docs/versions.md dentro do repositório, sinal de compatibilidade mantida entre gerações.

## Exemplo
git log --oneline --grep=0360811 no clone do bats-core localiza o commit herdado do upstream original.

## Limites e trade-offs
A biblioteca de exemplos oficiais mora em docs/examples no mesmo repositório, mas quem copia snippets de blogs pré-2017 pode encontrar run antigo sem --flag de status.

## Como verificar
Diferencie uma behavior de versão checando docs/versions.md: se o recurso não está lá, provavelmente veio do upstream abandonado.

## Conexões
- [[bats-formatters]] — Veja também: bats-core: pretty, TAP, tap13 e JUnit.

## Fontes
- [Bats-core — README oficial](https://github.com/bats-core/bats-core/blob/master/README.md) — proposta TAP, história do fork e licença MIT; consultado em 2026-10-03.
- [Bats-core — docs de versões antigas](https://github.com/bats-core/bats-core/blob/master/docs/versions.md) — documentação de versões anteriores à v1.2.1; consultado em 2026-10-03.
