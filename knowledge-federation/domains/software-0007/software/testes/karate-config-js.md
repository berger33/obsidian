---
id: software.testes.tranche15.000912
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://karatelabs.github.io/karate/#configuration", "https://karatelabs.github.io/karate/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karate: separar configuração por ambiente

## Em uma frase
O arquivo `karate-config.js` é avaliado antes das features e devolve um objeto de configuração que pode variar conforme o ambiente selecionado.

## Por que importa
Endereços de serviço, credenciais de teste e parâmetros por ambiente não pertencem às features, e espalhá-los pelos cenários torna a suíte dependente da máquina de quem executa.

## Como funciona
Centralize valores por ambiente na configuração, defina um padrão seguro para execução local e selecione o perfil pela variável de ambiente do processo.

## Exemplo
Uma função de configuração pode montar URLs e credenciais distintas para local, integração e teste, expondo o objeto correto ao runtime das features.

## Limites e trade-offs
Configuração dinâmica sem valor padrão falha de forma obscura quando a variável não está definida, e segredos não devem ser gravados no arquivo versionado.

## Como verificar
Execute a mesma feature com dois perfis de ambiente e confirme no relatório que os valores aplicados foram os esperados em cada caso.

## Conexões
- [[karate-match-assertions]] — Veja também: Karate: usar match e marcadores fuzzy.
- [[karate-call-and-read]] — Veja também: Karate: reutilizar features com call e read.

## Fontes
- [Karate — Configuration](https://karatelabs.github.io/karate/#configuration) — karate-config.js, perfis por ambiente e variáveis compartilhadas; consultado em 2026-10-02.
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
