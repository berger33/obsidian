---
id: software.testes.tranche25.001876
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
fontes: ["https://raw.githubusercontent.com/minkphp/Mink/master/README.md", "https://mink.behat.org/en/latest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Arquitetura extensível por DriverInterface: o caso MyCustomDriver

## Em uma frase
No exemplo do README oficial, ao lado de duas sessões GoutteDriver, o array de inicialização registra 'custom' => new Session(new MyCustomDriver($startUrl)) e depois executa exatamente a mesma cadeia $mink->getSession('custom')->getPage()->findLink('Downloads')->click() e getContent().

## Por que importa
Como Session depende apenas do contrato do driver, equipes com stacks específicos (um kernel HTTP interno, um navegador embarcado ou um cliente de API HTML) podem implementar seu próprio driver sem alterar uma única linha da API consumida pelos testes.

## Como funciona
Implemente o contrato de driver do Mink encapsulando o transporte desejado, passe a instância para new Session(new MeuDriver(...)) e registre-a no contêiner Mink com um nome próprio.

## Exemplo
O código que consome $mink->getSession('custom')->getPage()->findLink('Downloads')->click() no README é idêntico ao código que consome a sessão padrão goutte2.

## Limites e trade-offs
Nem todo driver suporta todas as capacidades do contrato (por exemplo, execução de JavaScript, avaliação de expressões no browser ou manipulação de janelas); drivers sem navegador lançam exceção se o teste invocar recursos exclusivos de browser real.

## Como verificar
Conferi o registro e o uso da sessão 'custom' com MyCustomDriver no README oficial.

## Conexões
- [[mink-visit-page-findlink-click]] — Veja também: Fluxo básico de navegação e interação: visit, getPage, findLink, click e getContent.
- [[mink-topical-guides-map]] — Veja também: Os oito guias temáticos da documentação oficial.

## Fontes
- [Mink — README oficial](https://raw.githubusercontent.com/minkphp/Mink/master/README.md) — README oficial do Mink com links úteis, exemplo de múltiplas sessões GoutteDriver e driver customizado, setDefaultSessionName, getSession e contribuidores.; consultado em 2026-10-03.
- [Mink — documentação oficial (en/latest)](https://mink.behat.org/en/latest/) — Página inicial da documentação oficial do Mink com definição como browser controller/emulator, instalação via Composer, catálogo de oito drivers, oito guias temáticos e integrações com Behat e PHPUnit.; consultado em 2026-10-03.
