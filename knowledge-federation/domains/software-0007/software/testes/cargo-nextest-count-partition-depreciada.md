---
id: software.testes.tranche15.000862
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
fontes: ["https://nexte.st/docs/ci-features/partitioning/", "https://nexte.st/docs/ci-features/archiving/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-nextest: substituir count por um particionamento documentado

## Em uma frase
A partição por `count` está depreciada; código de CI novo deve escolher entre as estratégias atuais e deixar explícita a política de estabilidade ou balanceamento.

## Por que importa
Manter um parâmetro depreciado pode funcionar temporariamente, mas torna o pipeline dependente de compatibilidade futura e obscurece o comportamento que os mantenedores pretendem suportar.

## Como funciona
A migração precisa considerar como seletores e números de shards são interpretados na versão do nextest fixada pelo projeto.

## Exemplo
Fixe a versão de nextest e converta a configuração para `slice` ou `hash` com a mesma contagem de buckets; compare os resultados de seleção antes de remover a implementação antiga.

## Limites e trade-offs
`slice` e `hash` possuem propriedades distintas, então substituir o texto mecanicamente pode alterar atribuições de testes ou a repetibilidade de builds.

## Como verificar
Consulte a referência de partições na versão efetivamente instalada e execute todos os shards num build de comparação antes de editar a configuração estável.

## Conexões
- [[cargo-nextest-hash-bin-id-e-identidade-do-teste]] — Veja também: cargo-nextest: entender a chave estável da partição hash.
- [[cargo-nextest-filtersets-e-seletores-cargo]] — Veja também: cargo-nextest: combinar filtersets e filtros de substring conscientemente.

## Fontes
- [cargo-nextest — Partitioning test runs in CI](https://nexte.st/docs/ci-features/partitioning/) — partições slice/hash/count, distribuição por shard e combinação de resultados; consultado em 2026-10-02.
- [cargo-nextest — Archiving and reusing builds](https://nexte.st/docs/ci-features/archiving/) — conteúdo e requisitos de archives para separar build de execução; consultado em 2026-10-02.
