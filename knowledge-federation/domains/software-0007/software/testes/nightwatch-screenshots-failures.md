---
id: software.testes.tranche21.001469
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://nightwatchjs.org/guide/reference/settings.html", "https://github.com/nightwatchjs/nightwatch"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nightwatch: capturas de tela em falha

## Em uma frase
O objeto screenshots controla a geração de imagens quando um comando erra ou um teste falha, com chaves enabled, on_failure, on_error e path.

## Por que importa
A diferença entre reler o log e ver a tela exata do momento da falha costuma ser o tempo inteiro do diagnóstico em testes de UI.

## Como funciona
Habilite as capturas, defina o diretório de saída e decida entre salvar em erro, em falha ou em ambos conforme o barulho aceito no artefato.

## Exemplo
Um teste de checkout quebrado por layout regressivo gera automaticamente a imagem que prova a sobreposição do botão.

## Limites e trade-offs
Capturas para toda flutuação de rede enchem o disco da esteira; on_error sem on_failure deixa passar a falha de asserção sem imagem.

## Como verificar
Provoque uma asserção falsa e confirme que o arquivo de imagem é gravado no caminho configurado.

## Conexões
- [[nightwatch-runner-mocha-unit]] — Veja também: Nightwatch: escolher runner e modo de unidade.

## Fontes
- [Nightwatch — Referência de Config Settings](https://nightwatchjs.org/guide/reference/settings.html) — chaves de configuração, ambientes, runner, workers e capturas; consultado em 2026-10-03.
- [Nightwatch — repositório oficial](https://github.com/nightwatchjs/nightwatch) — código-fonte, releases e documentação do projeto; consultado em 2026-10-03.
