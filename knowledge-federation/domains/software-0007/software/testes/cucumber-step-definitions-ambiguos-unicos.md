---
id: software.testes.tranche11.000483
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://cucumber.io/docs/cucumber/step-definitions/", "https://cucumber.io/docs/cucumber/cucumber-expressions/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: impedir step definitions ambíguos e duplicados

## Em uma frase
Cucumber precisa de uma definição única que corresponda ao texto de cada step; mais de uma correspondência impede execução inequívoca.

## Por que importa
Expressões genéricas como “I have .*” podem sobrepor passos específicos e falhar só quando nova feature adiciona texto coincidente.

## Como funciona
Prefira expressões limitadas por tipo ou valor e reúna lógica comum numa implementação com parâmetros explícitos.

## Exemplo
O step “saldo é {int}” atende vários valores; uma segunda expressão que também captura qualquer frase de saldo é removida.

## Limites e trade-offs
Expressão regular pode ser necessária, mas grupos capturados devem corresponder à assinatura do método.

## Como verificar
Rode discovery da suíte inteira e acrescente casos de fronteira que exercitem sobreposição de expressões.

## Conexões
- [[cucumber-expressions-parametros-tipados]] — Veja também: Cucumber: converter parâmetros de expressão para tipos de domínio.
- [[cucumber-scenario-outline-examples-linhas]] — Veja também: Cucumber: tratar cada linha de Examples como invocação do outline.

## Fontes
- [Cucumber — Step Definitions](https://cucumber.io/docs/cucumber/step-definitions/) — expressões, correspondência de steps e parâmetros tipados; consultado em 2026-10-02.
- [Cucumber — Cucumber Expressions](https://cucumber.io/docs/cucumber/cucumber-expressions/) — parâmetros nomeados, tipos integrados e expressões de step; consultado em 2026-10-02.
