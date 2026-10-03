---
id: software.testes.tranche15.000864
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
fontes: ["https://nexte.st/docs/filtersets/", "https://nexte.st/docs/machine-readable/junit/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-nextest: usar deps e rdeps para delimitar um subgrafo de crates

## Em uma frase
Predicados de dependência do filterset permitem selecionar testes ligados a um pacote sem escrever manualmente uma lista frágil de crates.

## Por que importa
`deps` pode abranger um pacote e suas dependências, enquanto `rdeps` seleciona dependentes; glob, interseção e negação ajudam a expressar recortes do workspace.

## Como funciona
O resultado reflete o grafo de pacotes conhecido por Cargo, não um grafo arbitrário de imports em runtime.

## Exemplo
Para rodar uma crate e suas dependências, use `cargo nextest run -E 'deps(my-crate)'`; para diagnosticar quem depende de uma família, liste o conjunto com `rdeps` e revise-o antes de transformar em política permanente.

## Limites e trade-offs
Seleção baseada no grafo pode ser mais ampla do que a alteração parece, e testar só o subgrafo não substitui a suíte completa na integração principal.

## Como verificar
Compare `cargo nextest list -E 'deps(my-crate)'` com o inventário de crates esperado e verifique a expressão após inclusão de dependência ou mudança de workspace.

## Conexões
- [[cargo-nextest-filtersets-e-seletores-cargo]] — Veja também: cargo-nextest: combinar filtersets e filtros de substring conscientemente.
- [[cargo-nextest-grupos-para-recursos-limitados]] — Veja também: cargo-nextest: limitar concorrência de testes que disputam o mesmo recurso.

## Fontes
- [cargo-nextest — Filterset DSL](https://nexte.st/docs/filtersets/) — predicados, união e interseção de filtros de testes e pacotes; consultado em 2026-10-02.
- [cargo-nextest — JUnit support](https://nexte.st/docs/machine-readable/junit/) — formato XML, inclusão de stdout/stderr, skipped tests e estado flaky; consultado em 2026-10-02.
