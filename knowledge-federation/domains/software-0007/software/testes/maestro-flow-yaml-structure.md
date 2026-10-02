---
id: software.testes.tranche15.000900
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://docs.maestro.dev/api-reference/commands", "https://docs.maestro.dev/getting-started/installing-maestro"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maestro: estruturar um fluxo em YAML

## Em uma frase
Um fluxo do Maestro é um arquivo YAML com identificador do aplicativo no cabeçalho, separador de documento e uma lista de comandos executados em ordem.

## Por que importa
A estrutura é o contrato de leitura da ferramenta: sem o cabeçalho correto o fluxo não sabe qual aplicativo iniciar e sem o separador os comandos não são interpretados.

## Como funciona
Declare `appId` no topo, use `---` para separar metadados da lista e mantenha um fluxo por cenário, extraindo subfluxos quando houver repetição.

## Exemplo
`appId: com.exemplo.loja` seguido de `---`, `- launchApp`, `- tapOn: "Entrar"` e `- assertVisible: "Olá"` descreve um caso mínimo completo.

## Limites e trade-offs
O YAML exige indentação consistente e nomes de comando exatos; um comando desconhecido interrompe a execução e deve ser diagnosticado antes de culpar o aplicativo.

## Como verificar
Execute o fluxo com a CLI e confirme a ordem dos passos no relatório; introduza um comando inválido e verifique a mensagem de erro apontando a linha.

## Conexões
- [[maestro-launch-and-state]] — Veja também: Maestro: controlar estado do aplicativo entre passos.

## Fontes
- [Maestro — Commands](https://docs.maestro.dev/api-reference/commands) — catálogo de comandos de interação, asserção, controle e espera; consultado em 2026-10-02.
- [Maestro — Installing Maestro](https://docs.maestro.dev/getting-started/installing-maestro) — instalação, requisitos e primeiros passos com a CLI; consultado em 2026-10-02.
