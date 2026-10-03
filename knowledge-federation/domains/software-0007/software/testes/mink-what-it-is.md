---
id: software.testes.tranche25.001870
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://mink.behat.org/en/latest/", "https://raw.githubusercontent.com/minkphp/Mink/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mink: controlador e emulador de navegador para aplicações web em PHP

## Em uma frase
A documentação oficial em mink.behat.org define o Mink como um controlador e emulador de navegador em código aberto para aplicações web, escrito em PHP, criado para simular nos testes a interação entre o navegador e a aplicação web.

## Por que importa
Na web existem duas famílias de ferramentas de teste — emuladores headless puros em processo/HTTP e controladores de navegadores reais para JavaScript — que historicamente tinham APIs incompatíveis; o Mink unifica ambas sob uma mesma API de sessão e página.

## Como funciona
O código de teste interage com objetos Session e DocumentElement (getPage(), findLink(), click(), getContent()), enquanto o driver escolhido por baixo traduz essas chamadas em requisições HTTP simuladas ou em comandos de automação de navegador.

## Exemplo
Ao chamar $mink->getSession()->visit($startUrl) seguido de $mink->getSession()->getPage()->findLink('Downloads')->click(), o teste navega e clica no link sem depender de qual driver executa a ação.

## Limites e trade-offs
O Mink é uma biblioteca PHP para uso dentro de suítes ou projetos, não um test runner autônomo; a orquestração de cenários ou casos de teste vem de ferramentas como Behat ou PHPUnit.

## Como verificar
Conferi a seção de abertura da documentação oficial em mink.behat.org e o exemplo do README oficial.

## Conexões
- [[mink-composer-install-no-drivers]] — Veja também: Instalação via Composer: pacote base sem drivers por padrão.

## Fontes
- [Mink — documentação oficial (en/latest)](https://mink.behat.org/en/latest/) — Página inicial da documentação oficial do Mink com definição como browser controller/emulator, instalação via Composer, catálogo de oito drivers, oito guias temáticos e integrações com Behat e PHPUnit.; consultado em 2026-10-03.
- [Mink — README oficial](https://raw.githubusercontent.com/minkphp/Mink/master/README.md) — README oficial do Mink com links úteis, exemplo de múltiplas sessões GoutteDriver e driver customizado, setDefaultSessionName, getSession e contribuidores.; consultado em 2026-10-03.
