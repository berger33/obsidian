---
id: software.testes.tranche23.001666
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
fontes: ["https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md", "https://karma-runner.github.io/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Captura de navegadores: launchers, a porta 9876 e o timeout de capture

## Em uma frase
A lista browsers inicializa e captura cada navegador listado; ChromeHeadless exige o plugin karma-chrome-launcher, Firefox o karma-firefox-launcher, e assim por diante — e dá para capturar qualquer navegador manualmente abrindo http://localhost:9876/ na mão.

## Por que importa
Em CI e máquinas sem perfil de navegador configurado, saber que a captura é negociada por launcher é o que destrava a execução: sem plugin, o navegador no config simplesmente não existe.

## Como funciona
O captureTimeout padrão de 60000 ms limita o boot de cada navegador; se um navegador não conectar a tempo, o Karma o mata e tenta de novo, desistindo após três tentativas de captura.

## Exemplo
Adicione browsers: [ChromeHeadless] com o launcher instalado e veja o log "Connected on socket ..."; em seguida, abra outro navegador no mesmo endereço e veja a linha "DEBUG ... /karma-debug.html" — a captura manual funciona sem launcher.

## Limites e trade-offs
Cada navegador tem um plugin launcher próprio e nem todo navegador está coberto por um; a referência lista exatamente os suportados (incluindo PhantomJS, hoje legatório), e lançadores adicionais pedem plugin customizado.

## Como verificar
Abra a opção browsers da referência de configuração e confirme os valores possíveis com seus plugins e a descrição do captureTimeout com as três tentativas.

## Conexões
- [[karma-file-patterns]] — Veja também: files, exclude e basePath: minimatch define o que entra na página.
- [[karma-timeouts-flakiness]] — Veja também: Três opções para conexões instáveis com o navegador.

## Fontes
- [Karma — Configuration file reference](https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md) — descoberta do arquivo, File Patterns e opções do objeto de configuração; consultado em 2026-10-03.
- [Karma — página inicial da documentação](https://karma-runner.github.io/latest/index.html) — destaques: real devices, remote control, frameworks, CI; consultado em 2026-10-03.
