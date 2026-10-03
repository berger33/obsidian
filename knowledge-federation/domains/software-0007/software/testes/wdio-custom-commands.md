---
id: software.testes.tranche18.001172
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://webdriver.io/docs/api", "https://webdriver.io/docs/gettingstarted"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: definir comandos próprios

## Em uma frase
Comandos personalizados podem ser adicionados ao navegador ou aos elementos, encapsulando sequências usadas em vários testes.

## Por que importa
Centralizar interações repetidas reduz duplicação e documenta a intenção da operação em um único lugar.

## Como funciona
Registre o comando com nome que expresse a intenção, receba parâmetros explícitos e reutilize comandos existentes internamente.

## Exemplo
Um comando de acesso pode combinar navegação, preenchimento e verificação da tela inicial.

## Limites e trade-offs
Comandos que escondem verificações importantes dificultam o diagnóstico, e nomes genéricos colidem com comandos do próprio framework.

## Como verificar
Substitua a implementação do comando próprio e confirme que os testes que o usam passam a refletir a mudança.

## Conexões
- [[wdio-services]] — Veja também: WebdriverIO: orquestrar serviços de teste.
- [[wdio-configuration]] — Veja também: WebdriverIO: estruturar a configuração.

## Fontes
- [WebdriverIO — API](https://webdriver.io/docs/api) — comandos de navegador e de elemento e comandos próprios; consultado em 2026-10-03.
- [WebdriverIO — Documentation](https://webdriver.io/docs/gettingstarted) — configuração, modos de execução, serviços e paralelismo; consultado em 2026-10-03.
