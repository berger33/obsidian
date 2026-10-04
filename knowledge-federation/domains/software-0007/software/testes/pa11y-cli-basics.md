---
id: software.testes.tranche16.001023
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

# Pa11y: executar a varredura de uma página

## Em uma frase
O comando recebe um endereço, abre a página em navegador sem interface e aplica verificações do motor escolhido, reportando os problemas encontrados.

## Por que importa
Verificar acessibilidade automaticamente em cada mudança detecta regressões simples sem depender de inspeção manual repetitiva.

## Como funciona
Instale a ferramenta como dependência de desenvolvimento, rode contra um ambiente reproduzível e trate o resultado como parte do trabalho de revisão.

## Exemplo
A execução padrão usa o motor baseado em análise estática do documento e o nível de conformidade intermediário, produzindo uma primeira leitura ampla.

## Limites e trade-offs
A varredura cobre uma página por execução e não navega nem interage, de modo que estados escondidos atrás de clique ficam fora do escopo.

## Como verificar
Rode a mesma página em duas revisões e compare a lista de problemas para confirmar que a ferramenta está medindo o que se espera.

## Conexões
- [[pa11y-standards-and-levels]] — Veja também: Pa11y: escolher o padrão de conformidade.

## Fontes
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
