---
id: software.testes.tranche17.001101
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

# Selenium: distribuir sessões com a grade

## Em uma frase
A grade recebe sessões, escolhe um nó compatível com as capacidades pedidas e devolve o endereço da sessão para o cliente.

## Por que importa
A execução distribuída reduz o tempo total da suíte e permite cobrir navegadores e sistemas que não estão disponíveis na máquina local.

## Como funciona
Suba o servidor da grade, registre os nós com as capacidades desejadas, aponte o cliente para o endereço e mantenha a mesma versão entre cliente e servidor.

## Exemplo
Um nó com navegador móvel simulado pode atender testes de layout, enquanto outro executa os fluxos no navegador principal.

## Limites e trade-offs
Diferenças de versão entre cliente e servidor causam erros de protocolo, e sessões órfãs consomem recursos até expirarem.

## Como verificar
Execute o mesmo teste apontando para a grade e para um navegador local e compare o resultado antes de atribuir instabilidade à grade.

## Conexões
- [[selenium-frames-windows-alerts]] — Veja também: Selenium: alternar entre contextos.
- [[selenium-browser-options]] — Veja também: Selenium: configurar opções do navegador.

## Fontes
- [Selenium — Grid](https://www.selenium.dev/documentation/grid/) — servidor, nós, capacidades e sessões distribuídas; consultado em 2026-10-03.
- [Selenium — repositório oficial](https://github.com/SeleniumHQ/selenium) — código-fonte e documentação das ligações por linguagem; consultado em 2026-10-03.
