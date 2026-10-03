---
id: software.testes.tranche23.001663
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
fontes: ["https://github.com/karma-runner/karma/blob/master/docs/intro/02-configuration.md", "https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# karma init: um assistente que escreve o arquivo de configuração

## Em uma frase
O comando karma init my.conf.js abre um assistente interativo que pergunta, nesta ordem: framework de teste, uso de Require.js, navegadores a capturar automaticamente, localização dos arquivos de código e teste, exclusões, e se o Karma deve observar arquivos e reexecutar ao mudar; no fim grava o arquivo gerado.

## Por que importa
Configurar o Karma à mão exige saber quais campos o objeto aceita; o assistente elimina a tela em branco e produz um ponto de partida válido e comentado, recomendado pela própria documentação de configuração.

## Como funciona
As respostas aceitam tabulação para listar opções e a tecla Enter para avançar; padrões glob como js/*.js e test/**/*Spec.js são aceitos nas perguntas de localização, e passar Enter vazio numa pergunta de lista avança para a seguinte.

## Exemplo
Gere a configuração em um projeto com testes, abra o my.conf.js resultante e confira que cada resposta virou um campo do config.set, por exemplo frameworks e browsers preenchidos.

## Limites e trade-offs
O assistente cobre apenas o esqueleto; ajustes finos (reporters, preprocessors, plugins) continuam manuais, e o README avisa que dá para escrever o arquivo à mão ou copiar de outro projeto.

## Como verificar
Abra a seção "Generating the config file" da página de configuração na documentação do Karma e confira a ordem exata das perguntas do assistente.

## Conexões
- [[karma-not-a-framework]] — Veja também: Karma não é framework de teste nem biblioteca de asserção.
- [[karma-config-discovery]] — Veja também: Onde o Karma procura o karma.conf.js (inclusive TypeScript).

## Fontes
- [Karma — Configuration (intro)](https://github.com/karma-runner/karma/blob/master/docs/intro/02-configuration.md) — assistente karma init, start e overrides de CLI; consultado em 2026-10-03.
- [Karma — Configuration file reference](https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md) — descoberta do arquivo, File Patterns e opções do objeto de configuração; consultado em 2026-10-03.
