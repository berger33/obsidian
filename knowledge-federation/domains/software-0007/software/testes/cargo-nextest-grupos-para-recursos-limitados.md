---
id: software.testes.tranche15.000865
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
fontes: ["https://nexte.st/docs/configuration/test-groups/", "https://nexte.st/docs/configuration/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-nextest: limitar concorrência de testes que disputam o mesmo recurso

## Em uma frase
Grupos de teste do nextest oferecem uma forma de limitar quantos casos associados a um recurso podem rodar simultaneamente, mesmo que o restante da suíte use mais paralelismo.

## Por que importa
Um serviço de banco, sandbox com quota ou simulador de hardware pode ter capacidade menor que a quantidade de threads global.

## Como funciona
Associar testes a um grupo nomeado e definir limite de slots evita que a scheduler sobrecarregue esse recurso compartilhado.

## Exemplo
Configure um grupo `postgres` com dois slots e atribua os testes que usam esse servidor; mantenha o número global de threads maior para que testes sem essa dependência continuem em paralelo.

## Limites e trade-offs
Um limite local não isola dados nem impede outros processos ou outros jobs de usar o servidor; a infraestrutura ainda precisa de namespaces ou bancos independentes.

## Como verificar
Observe espera por slots e utilização do recurso durante uma execução; aumente o limite apenas quando o backend demonstrar capacidade e os casos forem independentes.

## Conexões
- [[cargo-nextest-deps-e-selecao-de-subgrafo]] — Veja também: cargo-nextest: usar deps e rdeps para delimitar um subgrafo de crates.
- [[cargo-nextest-perfis-com-defaults-e-overrides]] — Veja também: cargo-nextest: usar perfis para separar política local e de CI.

## Fontes
- [cargo-nextest — Test groups for mutual exclusion](https://nexte.st/docs/configuration/test-groups/) — semaforização de subconjuntos e limites de concorrência por grupo; consultado em 2026-10-02.
- [cargo-nextest — Repository configuration](https://nexte.st/docs/configuration/) — perfis, herança e precedência de configurações do repositório; consultado em 2026-10-02.
