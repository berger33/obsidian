---
id: software.testes.tranche25.001878
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

# Integrações oficiais: Behat MinkExtension e phpunit-mink

## Em uma frase
Na seção Testing Tools Integration, a documentação oficial aponta as duas integrações mantidas para conectar o Mink a frameworks de teste: com o Behat através da Behat MinkExtension (github.com/Behat/MinkExtension) e com o PHPUnit através do pacote phpunit-mink (github.com/minkphp/phpunit-mink).

## Por que importa
Em projetos reais raramente se instancia new Mink(...) manualmente em cada arquivo de teste; usar a extensão correspondente injeta o gerenciamento de sessões, a limpeza entre cenários e os passos ou traits prontos no runner escolhido.

## Como funciona
Se a suíte usa BDD com Gherkin, integre via Behat MinkExtension para obter contextos e steps de navegação; se a suíte é xUnit clássica, use o pacote de integração com PHPUnit ou encapsule o Mink no TestCase base.

## Exemplo
Com a MinkExtension no Behat, cenários marcados com @javascript podem trocar automaticamente da sessão headless para a sessão Selenium configurada no behat.yml, usando o mesmo modelo de múltiplas sessões do Mink.

## Limites e trade-offs
A página inicial apenas referencia os dois repositórios de integração; a configuração detalhada de cada um vive na documentação própria da MinkExtension e do phpunit-mink.

## Como verificar
Conferi a seção Testing Tools Integration em mink.behat.org.

## Conexões
- [[mink-topical-guides-map]] — Veja também: Os oito guias temáticos da documentação oficial.
- [[mink-governance-contributors-and-channels]] — Veja também: Governança, canais comunitários e desenvolvimento do repositório.

## Fontes
- [Mink — documentação oficial (en/latest)](https://mink.behat.org/en/latest/) — Página inicial da documentação oficial do Mink com definição como browser controller/emulator, instalação via Composer, catálogo de oito drivers, oito guias temáticos e integrações com Behat e PHPUnit.; consultado em 2026-10-03.
- [Mink — README oficial](https://raw.githubusercontent.com/minkphp/Mink/master/README.md) — README oficial do Mink com links úteis, exemplo de múltiplas sessões GoutteDriver e driver customizado, setDefaultSessionName, getSession e contribuidores.; consultado em 2026-10-03.
