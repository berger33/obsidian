---
id: software.testes.tranche16.001031
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
fontes: ["https://github.com/pa11y/pa11y-ci", "https://github.com/pa11y/pa11y"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pa11y CI: varrer um conjunto de páginas

## Em uma frase
A ferramenta complementar lê uma lista de endereços em arquivo de configuração ou os descobre por mapa do site e produz resumo conjunto da varredura.

## Por que importa
Verificar páginas representativas em uma execução única cobre a jornada principal sem criar um caso de teste por rota.

## Como funciona
Liste as páginas mais relevantes, evite rotas destrutivas no mapa e escolha relatórios adequados à leitura por pessoas e por máquinas.

## Exemplo
Um conjunto inicial pode incluir página inicial, listagem, detalhe e formulário de contato, ampliado depois para rotas secundárias.

## Limites e trade-offs
Mapas do site grandes alongam a execução e podem incluir páginas irrelevantes ou protegidas, exigindo curadoria antes do uso.

## Como verificar
Execute a varredura do conjunto e confirme que cada endereço declarado aparece no resumo, com contagem própria de problemas.

## Conexões
- [[pa11y-config-file]] — Veja também: Pa11y: centralizar configuração do projeto.
- [[pa11y-ci-environment]] — Veja também: Pa11y CI: preparar ambiente e navegador.

## Fontes
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
