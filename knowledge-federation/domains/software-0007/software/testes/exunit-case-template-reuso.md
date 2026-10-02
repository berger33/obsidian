---
id: software.testes.tranche12.000625
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://ex-unit.hexdocs.pm/ExUnit.CaseTemplate.html", "https://ex-unit.hexdocs.pm/ExUnit.Callbacks.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ExUnit: compartilhar convenções com `CaseTemplate`

## Em uma frase
`ExUnit.CaseTemplate` permite que módulos de teste usem um template com callbacks e funções comuns.

## Por que importa
Templates reduzem duplicação de import e setup entre suites, mantendo a opção de cada módulo consumidor configurar seu próprio modo async.

## Como funciona
Defina setup e helpers no módulo-template, importe funções necessárias dentro do bloco `using` e mantenha no template apenas convenções realmente comuns.

## Exemplo
Um `MyApp.DataCase` pode importar helpers de banco e preparar contexto para testes que o utilizam, enquanto um `ConnCase` fornece outra API de integração.

## Limites e trade-offs
Colocar todas as fixtures no template executa preparação irrelevante para casos que não dependem daquele recurso e torna a herança de setup opaca.

## Como verificar
Crie dois módulos consumidores com necessidades diferentes e confirme que ambos recebem apenas os imports e callbacks previstos.

## Conexões
- [[exunit-async-global-state]] — Veja também: ExUnit: habilitar `async: true` com estado independente.
- [[exunit-capture-io-isolamento]] — Veja também: ExUnit: capturar IO com segurança em testes async.

## Fontes
- [ExUnit 1.20.4 — ExUnit.CaseTemplate](https://ex-unit.hexdocs.pm/ExUnit.CaseTemplate.html) — template de módulos de teste com callbacks e funções compartilhadas; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit.Callbacks](https://ex-unit.hexdocs.pm/ExUnit.Callbacks.html) — setup, setup_all, contexto, processos supervisionados e on_exit; consultado em 2026-10-02.
