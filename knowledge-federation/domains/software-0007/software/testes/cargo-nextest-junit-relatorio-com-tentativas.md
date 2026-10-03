---
id: software.testes.tranche15.000868
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

# cargo-nextest: preservar no JUnit falhas anteriores e retries

## Em uma frase
A exportação JUnit pode comunicar ao CI detalhes de testes que foram repetidos, permitindo distinguir passagem direta, recuperação após falha e falha persistente.

## Por que importa
Uma taxa de sucesso isolada pode esconder instabilidade se o formato final não carregar as tentativas anteriores.

## Como funciona
O relatório estruturado dá aos dashboards e à análise histórica um lugar consistente para ler `flakyFailure`, `flakyError` ou falhas reexecutadas.

## Exemplo
Configure o reporter JUnit do nextest para gravar um arquivo no diretório de artefatos, mantenha o upload mesmo em falha e associe o XML ao commit e à versão da configuração.

## Limites e trade-offs
Cada CI interpreta extensões JUnit de modo próprio; verifique o parser real usado pelo serviço e não apague os relatórios quando retries falham.

## Como verificar
Gere um teste de laboratório que falha uma vez e passa na repetição, depois confira no XML se o caso tem os elementos de retry/flaky documentados.

## Conexões
- [[cargo-nextest-retry-e-sinal-de-teste-flaky]] — Veja também: cargo-nextest: registrar retry como evidência de flakiness, não como cura.
- [[cargo-nextest-archive-exige-checkout-compativel]] — Veja também: cargo-nextest: separar build e execução com archive sem esquecer fontes.

## Fontes
- [cargo-nextest — Retries and flaky tests](https://nexte.st/docs/features/retries/) — tentativas, resultado flaky, backoff, overrides e integração JUnit; consultado em 2026-10-02.
- [cargo-nextest — JUnit support](https://nexte.st/docs/machine-readable/junit/) — formato XML, inclusão de stdout/stderr, skipped tests e estado flaky; consultado em 2026-10-02.
