---
id: software.testes.tranche23.001667
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md", "https://docs.travis-ci.com/user/gui-and-headless-browsers/#karma-and-firefox-inactivity-timeouts"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Três opções para conexões instáveis com o navegador

## Em uma frase
A referência documenta browserNoActivityTimeout (padrão 30000 ms) para desconectar quando o navegador para de responder durante os testes; browserDisconnectTimeout (padrão 2000 ms) define quanto esperar o reconector antes de tratar como falha; e browserDisconnectTolerance (padrão 0) quantas desconexões são toleradas antes de o run quebrar.

## Por que importa
Em CI com link instável entre o servidor Karma e o navegador — um telefone na rede, por exemplo — uma desconexão rápida derruba o build inteiro; essas opções existem exatamente para conexões "flaky", como documenta a própria referência.

## Como funciona
A doc explica que uma desconexão não é tratada como falha imediata: o Karma espera browserDisconnectTimeout e, se o navegador reconecta nesse intervalo, tudo bem; o valor padrão 30000 do no-activity é o recomendado pelo Travis CI, que o doc cita nominalmente.

## Exemplo
Em um dispositivo real conectado por Wi-Fi, force um lag (ou use o modo offline por alguns segundos) e ajuste browserDisconnectTolerance para 1: o run passa a tolerar o reconector em vez de falhar na hora.

## Limites e trade-offs
Tolerar desconexões não tolera testes que de fato travaram: se o navegador volta mas o teste não emite mensagem, o no-activity timeout ainda mata o run — os limites tratam conexão, não performance.

## Como verificar
Abra as três opções na referência de configuração e confirme os padrões 30000, 2000 e 0 e as descrições citadas, incluindo a referência a Travis.

## Conexões
- [[karma-browsers-capture]] — Veja também: Captura de navegadores: launchers, a porta 9876 e o timeout de capture.
- [[karma-watch-run-once]] — Veja também: Watch contínuo no dev, single run no CI.

## Fontes
- [Karma — Configuration file reference](https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md) — descoberta do arquivo, File Patterns e opções do objeto de configuração; consultado em 2026-10-03.
- [Travis CI — GUI and headless browsers](https://docs.travis-ci.com/user/gui-and-headless-browsers/#karma-and-firefox-inactivity-timeouts) — página citada pela referência do browserNoActivityTimeout; consultado em 2026-10-03.
