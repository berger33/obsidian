---
id: software.testes.tranche17.001102
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
fontes: ["https://www.selenium.dev/documentation/grid/", "https://github.com/SeleniumHQ/selenium"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: configurar opções do navegador

## Em uma frase
Cada navegador aceita opções de inicialização, como modo sem interface, argumentos de segurança, tamanho de janela e preferências de download.

## Por que importa
O comportamento do navegador precisa ser reproduzível no ambiente automatizado, e as opções corretas evitam falhas específicas de contêiner.

## Como funciona
Declare as opções na criação do driver, restrinja-as ao processo de teste e documente as que existem por limitação de ambiente.

## Exemplo
Em contêiner, a opção de sandbox precisa ser desativada explicitamente para o navegador iniciar sem privilégios elevados.

## Limites e trade-offs
Opções relaxadas de segurança não devem sair do ambiente de teste, e argumentos desnecessários podem alterar o comportamento observado.

## Como verificar
Execute o mesmo teste com e sem o modo sem interface e confirme que o resultado funcional é o mesmo antes de adotá-lo.

## Conexões
- [[selenium-grid-distributed]] — Veja também: Selenium: distribuir sessões com a grade.
- [[selenium-screenshot-and-evidence]] — Veja também: Selenium: registrar evidências de falha.

## Fontes
- [Selenium — Grid](https://www.selenium.dev/documentation/grid/) — servidor, nós, capacidades e sessões distribuídas; consultado em 2026-10-03.
- [Selenium — repositório oficial](https://github.com/SeleniumHQ/selenium) — código-fonte e documentação das ligações por linguagem; consultado em 2026-10-03.
