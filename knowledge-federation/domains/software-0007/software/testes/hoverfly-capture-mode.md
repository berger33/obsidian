---
id: software.testes.tranche22.001642
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://docs.hoverfly.io/en/latest/pages/tutorials/basic/exportingsimulations/exportingsimulations.html", "https://docs.hoverfly.io/en/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hoverfly: capture grava o tráfego real

## Em uma frase
Em capture mode o hoverfly registra as conversas que passam pelo proxy — requests e respostas do serviço real — e as acumula como simulação reutilizável; o fluxo oficial é hoverctl start, hoverctl mode capture e depois o cliente apontado para o proxy.

## Por que importa
A forma mais rápida de criar uma simulação fiel é gravar o tráfego de um ambiente real uma vez e versionar o JSON gerado, em vez de escrever stubs à mão.

## Como funciona
O tutorial usa cURL contra um endpoint de hora: curl --proxy http://localhost:8500 http://time.jsontest.com — o proxy local na porta 8500 é o ponto de entrada padrão.

## Exemplo
Por default os headers não entram na captura; o próprio tutorial mostra hoverctl mode capture --headers "User-Agent,Content-Type,Authorization" e a variante --all-headers.

## Limites e trade-offs
Captura com --headers seletivo grava contrato incompleto: um teste de simulação que passa sem Authorization no registro não prova nada sobre o cabeçalho.

## Como verificar
Capture uma chamada real, exporte (nota própria) e confirme se os headers que o seu serviço lê aparecem na simulação gravada.

## Conexões
- [[hoverfly-two-binaries]] — Veja também: Hoverfly: o par hoverfly + hoverctl.
- [[hoverfly-export-simulation]] — Veja também: Hoverfly: exportar filtrando por URL.

## Fontes
- [Hoverfly — Creating and exporting a simulation](https://docs.hoverfly.io/en/latest/pages/tutorials/basic/exportingsimulations/exportingsimulations.html) — capture mode, proxy 8500, headers e export --url-pattern; consultado em 2026-10-03.
- [Hoverfly — documentação inicial](https://docs.hoverfly.io/en/latest/index.html) — conceitos-chave, reference e troubleshooting do v1.12.15; consultado em 2026-10-03.
