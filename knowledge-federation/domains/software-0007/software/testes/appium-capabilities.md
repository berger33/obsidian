---
id: software.testes.tranche17.001106
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://appium.io/docs/en/latest/", "https://github.com/appium/appium"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: declarar capacidades da sessão

## Em uma frase
As capacidades descrevem plataforma, automação, dispositivo e aplicativo, definindo o que a sessão vai controlar antes de qualquer comando.

## Por que importa
Uma sessão mal especificada conecta ao dispositivo errado ou ao aplicativo errado, e os sintomas aparecem depois como falhas de seletores.

## Como funciona
Informe a plataforma, o nome da automação, o identificador do dispositivo e o caminho do aplicativo, mantendo as capacidades versionadas junto do teste.

## Exemplo
Uma execução em emulador Android pode declarar a automação específica da plataforma e o identificador da instância para evitar ambiguidade com dispositivos conectados.

## Limites e trade-offs
O nome do dispositivo não seleciona o alvo por si só, e a ausência do identificador faz a sessão usar o primeiro dispositivo disponível.

## Como verificar
Execute com dois dispositivos conectados e confirme que a sessão foi criada exatamente no identificador declarado.

## Conexões
- [[appium-drivers-architecture]] — Veja também: Appium: entender a arquitetura de drivers.

## Fontes
- [Appium — Documentation](https://appium.io/docs/en/latest/) — capacidades, drivers, seletores, gestos e contexto de sessão; consultado em 2026-10-03.
- [Appium — repositório oficial](https://github.com/appium/appium) — arquitetura de drivers e plugins, CLI de extensões e servidor; consultado em 2026-10-03.
