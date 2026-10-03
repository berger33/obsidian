---
id: software.testes.tranche15.000867
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
fontes: ["https://nexte.st/docs/features/retries/", "https://nexte.st/docs/machine-readable/junit/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-nextest: registrar retry como evidência de flakiness, não como cura

## Em uma frase
`--retries` repete um teste que falhou; se ele passar em uma tentativa posterior, o nextest o marca como flaky e pode incluí-lo nos relatórios.

## Por que importa
O estado final pode ser sucesso mesmo após uma falha inicial, dependendo da política `flaky-result`.

## Como funciona
Essa informação é útil para reduzir ruído operacional, mas a primeira falha ainda revela não determinismo ou uma dependência que merece investigação.

## Exemplo
Use `cargo nextest run --retries 2` para um job diagnóstico e publique o resultado JUnit; se a equipe exigir que qualquer intermitência bloqueie integração, configure `flaky-result = "fail"`.

## Limites e trade-offs
Retries acrescentam tempo e podem repetir efeito externo; configure delays e escopo por teste com cuidado, e não promova um teste intermitente a confiável só porque uma repetição passou.

## Como verificar
Introduza falha alternada num teste descartável e confirme tentativas, etiqueta flaky, código de saída para cada política e marcação no JUnit.

## Conexões
- [[cargo-nextest-perfis-com-defaults-e-overrides]] — Veja também: cargo-nextest: usar perfis para separar política local e de CI.
- [[cargo-nextest-junit-relatorio-com-tentativas]] — Veja também: cargo-nextest: preservar no JUnit falhas anteriores e retries.

## Fontes
- [cargo-nextest — Retries and flaky tests](https://nexte.st/docs/features/retries/) — tentativas, resultado flaky, backoff, overrides e integração JUnit; consultado em 2026-10-02.
- [cargo-nextest — JUnit support](https://nexte.st/docs/machine-readable/junit/) — formato XML, inclusão de stdout/stderr, skipped tests e estado flaky; consultado em 2026-10-02.
