---
id: software.testes.tranche25.001872
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
fontes: ["https://mink.behat.org/en/latest/", "https://github.com/minkphp/Mink"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# O catálogo de oito drivers na documentação e a dupla recomendada

## Em uma frase
A documentação oficial lista oito pacotes de driver instaláveis via Composer: GoutteDriver (behat/mink-goutte-driver), Selenium2Driver (behat/mink-selenium2-driver), BrowserKitDriver (behat/mink-browserkit-driver), ChromeDriver (dmore/chrome-mink-driver), ZombieDriver (behat/mink-zombie-driver), SeleniumDriver (behat/mink-selenium-driver), SahiDriver (behat/mink-sahi-driver) e WUnitDriver (behat/mink-wunit-driver), recomendando a quem está começando iniciar com GoutteDriver e Selenium2Driver.

## Por que importa
Essa combinação inicial cobre os dois extremos: um emulador HTTP rápido sem navegador para a massa de testes de servidor e um controlador de navegador real para os fluxos que dependem de JavaScript no cliente.

## Como funciona
Para começar uma suíte nova seguindo o guia oficial, instale um driver de emulação rápida e um driver de navegador real, registrando ambos no gerenciador Mink para alternar conforme a necessidade do cenário.

## Exemplo
Enquanto BrowserKitDriver e GoutteDriver operam sem abrir janela de navegador, Selenium2Driver e ChromeDriver (dmore/chrome-mink-driver) controlam instâncias reais de browser.

## Limites e trade-offs
Como cada driver vive em seu próprio pacote no Packagist, versões suportadas de PHP, dependências de sistema e estado de manutenção variam de driver para driver e devem ser verificados no pacote específico.

## Como verificar
Conferi a lista dos oito drivers e a recomendação para iniciantes na seção Installation de mink.behat.org.

## Conexões
- [[mink-composer-install-no-drivers]] — Veja também: Instalação via Composer: pacote base sem drivers por padrão.
- [[mink-sessions-and-default-session]] — Veja também: Registro de múltiplas sessões e setDefaultSessionName.

## Fontes
- [Mink — documentação oficial (en/latest)](https://mink.behat.org/en/latest/) — Página inicial da documentação oficial do Mink com definição como browser controller/emulator, instalação via Composer, catálogo de oito drivers, oito guias temáticos e integrações com Behat e PHPUnit.; consultado em 2026-10-03.
- [Repositório oficial minkphp/Mink](https://github.com/minkphp/Mink) — Repositório oficial do Mink no GitHub com classes Mink, Session, DocumentElement, DriverInterface e workflows de CI.; consultado em 2026-10-03.
