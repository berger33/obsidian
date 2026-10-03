---
id: software.testes.tranche15.000861
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
fontes: ["https://nexte.st/docs/ci-features/partitioning/", "https://nexte.st/docs/machine-readable/junit/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-nextest: entender a chave estável da partição hash

## Em uma frase
A partição `hash` usa a identidade do binário e o nome do teste para decidir o bucket, o que evita depender apenas da posição ordinal numa lista.

## Por que importa
Em comparação com dividir por índice, a alocação não muda por causa de qualquer teste inserido antes na enumeração; ainda assim, renomear o teste ou mover sua identidade de binário altera a chave e pode movê-lo para outro shard.

## Como funciona
Estabilidade diz respeito à entrada idêntica, não a imutabilidade diante de refactors.

## Exemplo
Grave no log do job o seletor, binário e índice/total da partição. Ao comparar commits, examine a lista de testes de cada bucket para descobrir se mudanças de nomes redistribuíram carga de modo esperado.

## Limites e trade-offs
Hash estável não significa que cada bucket terá a mesma quantidade ou duração, e todos os jobs devem fixar a mesma divisão e filtros para evitar lacunas ou duplicatas.

## Como verificar
Rode `cargo nextest list` por shard para dois commits consecutivos e compare a atribuição de testes que mantiveram binário e nome, além de auditar a união dos buckets.

## Conexões
- [[cargo-nextest-slice-versus-hash]] — Veja também: cargo-nextest: escolher partição slice ou hash conforme a estabilidade.
- [[cargo-nextest-count-partition-depreciada]] — Veja também: cargo-nextest: substituir count por um particionamento documentado.

## Fontes
- [cargo-nextest — Partitioning test runs in CI](https://nexte.st/docs/ci-features/partitioning/) — partições slice/hash/count, distribuição por shard e combinação de resultados; consultado em 2026-10-02.
- [cargo-nextest — JUnit support](https://nexte.st/docs/machine-readable/junit/) — formato XML, inclusão de stdout/stderr, skipped tests e estado flaky; consultado em 2026-10-02.
