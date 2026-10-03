---
id: software.testes.tranche23.001669
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
fontes: ["https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md", "https://github.com/karma-runner/karma/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Launchers, reporters e preprocessors são todos plugins

## Em uma frase
O aviso no topo da referência de configuração é prático: a maioria dos adaptadores de framework, reporters, preprocessors e launchers precisa ser carregada como plugin; o objeto de configuração não ganha recursos sozinho instalando apenas o pacote karma.

## Por que importa
Verificar que o teste de cobertura não roda "por mágica" economiza horas: sem karma-coverage instalado como plugin, a opção coverage no preprocessors não existe, e a suíte de CI publica zero relatórios.

## Como funciona
A página "When should I use Karma?" aponta o Istanbul como razão para adotar o runner; na prática isso significa karma-coverage mais configuração de preprocessors e reporter — o trio plugin-configuração-reporter se repete para qualquer extensão.

## Exemplo
Rode npm install karma-coverage, habilite-a em plugins e reporters e confirme que a linha "Coverage: ..." aparece na saída do terminal após uma execução single run.

## Limites e trade-offs
O README descreve a arquitetura como aberta a qualquer framework via adaptador, mas a doc não garante paridade de recursos entre plugins nem manutenção ativa de todos os da lista npm — o status de deprecação também se reflete nos plugins do ecossistema.

## Como verificar
Abra a nota inicial da referência de configuração ("Most of the framework adapters... as plugins") e a menção ao Istanbul na seção de quando usar, no README oficial.

## Conexões
- [[karma-watch-run-once]] — Veja também: Watch contínuo no dev, single run no CI.

## Fontes
- [Karma — Configuration file reference](https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md) — descoberta do arquivo, File Patterns e opções do objeto de configuração; consultado em 2026-10-03.
- [Karma — README oficial](https://github.com/karma-runner/karma/blob/master/README.md) — proposta, descontinuação, adaptadores e quando usar; consultado em 2026-10-03.
