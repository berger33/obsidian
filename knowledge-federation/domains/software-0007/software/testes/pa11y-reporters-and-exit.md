---
id: software.testes.tranche16.001027
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/pa11y/pa11y", "https://github.com/pa11y/pa11y-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pa11y: escolher formato de saída e código de retorno

## Em uma frase
A ferramenta oferece relatórios em texto, formato estruturado e formato de valores separados, e o código de saída indica se o limite de problemas foi excedido.

## Por que importa
Formato estruturado permite arquivar evidência e processar resultados, enquanto o código de retorno faz a esteira reagir sem interpretação humana.

## Como funciona
Use formato legível no desenvolvimento, formato estruturado no pipeline e arquive a saída como evidência de cada execução.

## Exemplo
Guardar o resultado estruturado permite comparar listas entre revisões e evidenciar correções ao longo do tempo.

## Limites e trade-offs
O código de saída não distingue tipos de problema por si só, e o relatório precisa ser lido para saber o que motivou a falha.

## Como verificar
Provoque um problema conhecido e confirme que o código de retorno é diferente de zero e que o item aparece no relatório estruturado.

## Conexões
- [[pa11y-actions]] — Veja também: Pa11y: preparar a página com ações.
- [[pa11y-threshold-policy]] — Veja também: Pa11y: usar limite como política temporária.

## Fontes
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
