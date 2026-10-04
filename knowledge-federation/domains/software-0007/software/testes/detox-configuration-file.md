---
id: software.testes.tranche16.000959
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
fontes: ["https://wix.github.io/Detox/docs/introduction/project-setup", "https://wix.github.io/Detox/docs/introduction/getting-started"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Detox: descrever alvos no arquivo de configuração

## Em uma frase
O arquivo de configuração declara aplicativos, dispositivos e configurações nomeadas usadas pelos comandos de build e de teste.

## Por que importa
Centralizar essas definições evita repetir caminhos e identificadores na linha de comando e permite que o mesmo teste rode em alvos diferentes.

## Como funciona
Defina uma configuração por alvo, nomeie-a de forma previsível e mantenha os comandos de construção referenciando o mesmo arquivo.

## Exemplo
Uma configuração de simulador pode compilar e executar o aplicativo com variáveis próprias, enquanto outra aponta para emulador com identificador distinto.

## Limites e trade-offs
Configurações divergentes entre máquina local e integração contínua produzem resultados diferentes; o arquivo precisa ser versionado e único para o projeto.

## Como verificar
Execute o mesmo caso com duas configurações nomeadas e compare o alvo efetivamente iniciado no relatório de cada execução.

## Conexões
- [[detox-artifacts-failure]] — Veja também: Detox: preservar artefatos das falhas.
- [[detox-ci-stability]] — Veja também: Detox: estabilizar a execução em integração contínua.

## Fontes
- [Detox — Project Setup](https://wix.github.io/Detox/docs/introduction/project-setup) — configuração por alvo, arquivo de configuração e comandos de build e teste; consultado em 2026-10-03.
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
