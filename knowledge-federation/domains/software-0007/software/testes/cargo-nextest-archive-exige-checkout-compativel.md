---
id: software.testes.tranche15.000869
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nexte.st/docs/ci-features/archiving/", "https://nexte.st/docs/machine-readable/junit/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-nextest: separar build e execução com archive sem esquecer fontes

## Em uma frase
`cargo nextest archive` pode transferir binários de teste e artefatos relacionados para outro job, mas o archive não leva o código-fonte do projeto.

## Por que importa
O ambiente de execução precisa ter o checkout na mesma revisão, além do nextest e bibliotecas necessárias; os binários e metadados sozinhos não satisfazem testes que abrem fixtures relativas ao workspace.

## Como funciona
Artefatos externos podem ser incluídos por configuração quando o processo de build os cria fora do conjunto padrão.

## Exemplo
Construa e arquive no primeiro job com `cargo nextest archive --archive-file tests.tar.zst`; no job seguinte, restaure o mesmo commit e rode `cargo nextest run --archive-file tests.tar.zst`.

## Limites e trade-offs
Um archive não é uma imagem completa de ambiente e não deve ser reutilizado com uma árvore de fontes divergente; arquivos untracked que influenciaram testes também precisam de tratamento explícito.

## Como verificar
Compare o SHA do checkout em ambos os jobs, execute um teste que lê fixture do repositório e outro que depende de biblioteca dinâmica, e valide que todos os arquivos chegaram.

## Conexões
- [[cargo-nextest-junit-relatorio-com-tentativas]] — Veja também: cargo-nextest: preservar no JUnit falhas anteriores e retries.

## Fontes
- [cargo-nextest — Archiving and reusing builds](https://nexte.st/docs/ci-features/archiving/) — conteúdo e requisitos de archives para separar build de execução; consultado em 2026-10-02.
- [cargo-nextest — JUnit support](https://nexte.st/docs/machine-readable/junit/) — formato XML, inclusão de stdout/stderr, skipped tests e estado flaky; consultado em 2026-10-02.
