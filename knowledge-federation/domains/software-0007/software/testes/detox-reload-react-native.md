---
id: software.testes.tranche16.000953
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
fontes: ["https://wix.github.io/Detox/docs/introduction/getting-started", "https://wix.github.io/Detox/docs/introduction/project-setup"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Detox: recarregar o JavaScript entre casos

## Em uma frase
A recarga do pacote JavaScript restaura o estado da aplicação sem reconstruir o binário nem reiniciar o processo nativo, reduzindo o tempo entre casos.

## Por que importa
Reconstruir o aplicativo a cada teste é lento, e não limpar o estado faz o caso seguinte herdar telas e dados do anterior.

## Como funciona
Use a recarga em ganchos de preparação por caso e reserve relançamentos completos para fluxos que dependem de estado nativo ou de sessão.

## Exemplo
Um grupo de testes de formulário pode recarregar a aplicação antes de cada caso, garantindo que campos e navegação comecem vazios.

## Limites e trade-offs
A recarga não limpa armazenamento persistente nem reinicia serviços nativos, então cenários que gravam dados localmente continuam precisando de limpeza específica.

## Como verificar
Grave um valor persistente, recarregue e verifique se ele sobrevive; depois remova-o e confirme que o próximo caso começa no estado esperado.

## Conexões
- [[detox-launchapp-options]] — Veja também: Detox: controlar o lançamento do aplicativo.
- [[detox-waitfor-explicit]] — Veja também: Detox: esperar condições que a ferramenta não observa.

## Fontes
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
- [Detox — Project Setup](https://wix.github.io/Detox/docs/introduction/project-setup) — configuração por alvo, arquivo de configuração e comandos de build e teste; consultado em 2026-10-03.
