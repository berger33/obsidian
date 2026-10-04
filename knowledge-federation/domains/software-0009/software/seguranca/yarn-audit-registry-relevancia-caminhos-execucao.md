---
id: software.seguranca.tranche17.001670
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://yarnpkg.com/cli/npm/audit#details", "https://yarnpkg.com/cli/npm/audit#usage"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Relevância de advisories no Yarn: cruzar registry, versão e caminho de execução

## Em uma frase
O Yarn observa que relatórios extraídos do npm registry podem ou não ser relevantes para o programa porque nem toda vulnerabilidade afeta todos os caminhos de código.

## Por que importa
A equipe precisa distinguir presença de versão vulnerável de exposição real, mantendo tratamento sério sem inflar achados como exploração confirmada.

## Como funciona
Confirme a faixa advisory, pacote selecionado, dependência reversa e uso da funcionalidade; registre decisão de risco mesmo quando não houver chamada observável.

## Exemplo
Para um achado em utilitário de parsing, rastreie chamadas no produto, superfície de entrada e modo de compilação antes de decidir prioridade e atualização.

## Limites e trade-offs
Ausência de chamada em teste não prova ausência em produção; código opcional e configurações alternativas podem ativar caminhos não exercitados.

## Como verificar
Combine o relatório do Yarn com revisão do grafo, testes e análise de execução e mantenha evidência da versão exata usada.

## Conexões
- [[yarn-why-triagem-pacote-transitivo-origem]] — `yarn why` depois do audit: localizar quem introduziu uma dependência transitiva.

## Fontes
- [Yarn — relevância de advisories](https://yarnpkg.com/cli/npm/audit#details) — ressalva oficial de que findings do registry podem não afetar todos os caminhos; consultado em 2026-10-04.
- [Yarn — execução do audit](https://yarnpkg.com/cli/npm/audit#usage) — comando e finalidade da consulta de advisories; consultado em 2026-10-04.
