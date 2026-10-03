---
id: software.testes.tranche15.000866
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
fontes: ["https://nexte.st/docs/configuration/reference/", "https://nexte.st/docs/filtersets/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-nextest: usar perfis para separar política local e de CI

## Em uma frase
Perfis do nextest agrupam opções de execução e podem aplicar overrides por teste, permitindo que ambiente e comportamento sejam declarados em configuração revisável.

## Por que importa
Em vez de espalhar flags distintas por workflows, um perfil pode centralizar retries, timeout, reporter, fail-fast e filtros padrão; overrides refinam uma regra para testes identificados por filterset.

## Como funciona
Isso torna diferenças visíveis, mas exige saber qual perfil o comando seleciona.

## Exemplo
Defina `profile.ci` no `.config/nextest.toml`, selecione-o com `--profile ci` e dê a um caso lento um timeout maior por override em vez de elevar o limite de toda a suite.

## Limites e trade-offs
Overrides e flags de linha de comando podem interagir de modo específico; versões do nextest também validam versões mínimas de configuração, portanto não copie sintaxe sem verificar a versão pinada.

## Como verificar
Inspecione configuração efetiva e liste os testes sob cada perfil, incluindo um teste com override e outro sem, para confirmar que ambos recebem a política pretendida.

## Conexões
- [[cargo-nextest-grupos-para-recursos-limitados]] — Veja também: cargo-nextest: limitar concorrência de testes que disputam o mesmo recurso.
- [[cargo-nextest-retry-e-sinal-de-teste-flaky]] — Veja também: cargo-nextest: registrar retry como evidência de flakiness, não como cura.

## Fontes
- [cargo-nextest — Configuration reference](https://nexte.st/docs/configuration/reference/) — opções padrão de perfis, overrides e caminhos de relatórios; consultado em 2026-10-02.
- [cargo-nextest — Filterset DSL](https://nexte.st/docs/filtersets/) — predicados, união e interseção de filtros de testes e pacotes; consultado em 2026-10-02.
