---
id: software.testes.tranche12.000554
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
fontes: ["https://playwright.dev/docs/test-snapshots", "https://playwright.dev/docs/test-projects"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright Test: snapshots visuais e baseline

## Em uma frase
`toHaveScreenshot()` compara uma captura atual com uma imagem de referência gerada e versionada para aquele teste.

## Por que importa
Uma comparação visual detecta alterações de layout e renderização que assertions de texto ou de presença podem não descrever, desde que a referência represente o resultado aprovado.

## Como funciona
Gere a baseline em ambiente controlado, revise a imagem e comite-a junto do teste; ao atualizar, use a opção de update de snapshots apenas depois de confirmar a mudança visual pretendida.

## Exemplo
Uma página de recibo pode comparar o painel inteiro, enquanto uma segunda assertion valida que o identificador e o total continuam acessíveis como texto.

## Limites e trade-offs
Browser, sistema operacional, fontes e modo headless podem alterar pixels sem regressão de produto. Uma baseline aceita automaticamente pode transformar um defeito em novo resultado esperado.

## Como verificar
Rode a comparação no mesmo ambiente da baseline e revise visualmente cada PNG alterado antes de aceitar mudanças no diretório de snapshots.

## Conexões
- [[playwright-sharding-ci-particionamento]] — Veja também: Playwright Test: particionamento por shards na CI.
- [[playwright-page-object-contract]] — Veja também: Playwright Test: limites de um Page Object.

## Fontes
- [Playwright — Visual comparisons](https://playwright.dev/docs/test-snapshots) — baselines de screenshot, diferenças de ambiente e atualização de snapshots; consultado em 2026-10-02.
- [Playwright — Projects](https://playwright.dev/docs/test-projects) — projetos por browser/dispositivo/ambiente, dependências, teardown e parametrização; consultado em 2026-10-02.
