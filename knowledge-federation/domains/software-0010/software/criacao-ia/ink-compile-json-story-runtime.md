---
id: software.criacao_ia.tranche05.000481
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#getting-started-with-the-runtime-api", "https://github.com/inkle/ink/blob/master/README.md#integrating-into-your-game"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ink: compilar arquivos .ink para JSON e carregar uma instância Story

## Em uma frase
Ink transforma fontes `.ink` em um JSON de runtime que o engine C# carrega em uma instância `Ink.Runtime.Story`.

## Por que importa
Separar autoria da narrativa da aplicação permite editar o fluxo sem transformar Ink em um engine completo de UI ou gameplay.

## Como funciona
Compile por integração Unity, Inky, inklecate ou compilador C# e passe o JSON à classe `Story`; mantenha um wrapper próprio responsável por UI, input e integração ao jogo.

## Exemplo
Unity carrega o arquivo compilado como `TextAsset`, cria `new Story(inkAsset.text)` no início do controlador e encaminha conteúdo e escolhas ao diálogo visual.

## Limites e trade-offs
A documentação descreve Unity no exemplo, mas observa que runtime pode ser usado fora de Unity em C#; versões de engine e formatos de story devem ser compatíveis.

## Como verificar
Compile um arquivo mínimo, instancie o runtime com JSON produzido e confirme que primeira linha e primeira escolha correspondem ao arquivo `.ink`.

## Conexões
- [[ink-continue-output-granularity]] — Ink runtime: escolher Continue ou ContinueMaximally pela granularidade da interface.

## Fontes
- [Ink — Running your ink: runtime API](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#getting-started-with-the-runtime-api) — Mostra JSON compilado, instanciação de Story e TextAsset como entrada de Unity. Consulta: 2026-10-04.
- [Ink — README: integrating into your game](https://github.com/inkle/ink/blob/master/README.md#integrating-into-your-game) — Resume export JSON, integração Unity e papel do runtime C# na aplicação. Consulta: 2026-10-04.
