---
id: software.testes.tranche21.001536
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
fontes: ["https://github.com/sourcefrog/cargo-mutants", "https://crates.io/crates/mutants"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-mutants: marcar funções para pular

## Em uma frase
Com a dependência do micro-crate mutants no Cargo.toml, o atributo #[mutants::skip] numa função a remove da lista de mutantes.

## Por que importa
Há código de cache e efeito colateral de performance que deve existir sem teste unitário; a recusa precisa ser declarada, não implicada.

## Como funciona
Declare a dependência minúscula, anote as funções fora do escopo e deixe o atributo ser só metadado para o compilador.

## Exemplo
O README frisa que o crate é pequeno e o atributo não tem efeito algum no código compilado, além de marcar a função para a ferramenta.

## Limites e trade-offs
Cada skip solto abre espaço para a próxima função meio-testada se esconder atrás dele; peça justificativa no code review.

## Como verificar
Anote uma função sobrevivente com skip e confirme que ela some da nova corrida.

## Conexões
- [[cargo-mutants-list-diff-json]] — Veja também: cargo-mutants: ver mutantes sem rodá-los.
- [[cargo-mutants-output-directory]] — Veja também: cargo-mutants: o que há em mutants.out.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [mutants — crate de anotação](https://crates.io/crates/mutants) — dependência mínima para #[mutants::skip]; consultado em 2026-10-03.
