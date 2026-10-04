---
id: software.testes.tranche16.001028
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

# Pa11y: usar limite como política temporária

## Em uma frase
Um limite numérico permite que a execução passe com quantidade pequena de problemas, controlado por parâmetro ou configuração.

## Por que importa
Projetos com passivo acumulado precisam de saída gradual, mas o limite deve ser dívida declarada com prazo, não permissão permanente.

## Como funciona
Registre o valor atual, associe a redução a marcos do projeto e reavalie o número em cada ciclo de melhoria.

## Exemplo
Um projeto legado pode ser aceito com número reduzido de problemas enquanto correções são priorizadas por impacto para a pessoa usuária.

## Limites e trade-offs
Limite alto acomoda regressões novas sem distinção das antigas, e a equipe perde a noção de quanto passivo ainda resta.

## Como verificar
Aumente deliberadamente a quantidade de problemas na página e confirme que a execução falha a partir do valor definido.

## Conexões
- [[pa11y-reporters-and-exit]] — Veja também: Pa11y: escolher formato de saída e código de retorno.
- [[pa11y-ignore-and-scope]] — Veja também: Pa11y: restringir escopo e registrar exceções.

## Fontes
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
