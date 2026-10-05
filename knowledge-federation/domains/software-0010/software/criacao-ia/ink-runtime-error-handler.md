---
id: software.criacao_ia.tranche05.000490
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
fontes: ["https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#error-handling", "https://github.com/inkle/ink/blob/master/ink-engine-runtime/Story.cs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ink runtime: registrar onError para erros que só aparecem durante a narrativa

## Em uma frase
Alguns erros do roteiro só surgem quando conteúdo é executado, então o runtime recomenda registrar `Story.onError` ao criar cada Story.

## Por que importa
Sem handler, um problema de script pode virar exceção inesperada no loop de diálogo em vez de log ou estado controlado pela aplicação.

## Como funciona
Assine `onError` logo após instanciar Story e encaminhe warning e error a canais distintos; use logs com story ID, versão e posição do jogador para investigação.

## Exemplo
Um wrapper registra warning em log amarelo e erros de runtime como erro de build de narrativa, bloqueando envio de escolhas inválidas ao jogador.

## Limites e trade-offs
O handler captura problemas do Ink detectados durante execução, não substitui erros de compilação ou validação da aplicação; comportamento de recuperação depende do runtime e da versão.

## Como verificar
Crie um erro de script que compilador não detecta, confirme callback e categorização Warning/Error e valide que o jogo não expõe stack trace interno à UI.

## Conexões
- [[ink-precompile-include-filehandler]] — Ink: preferir compilação prévia e configurar includes no fluxo de compilação C#.

## Fontes
- [Ink — Running your ink: error handling](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#error-handling) — Recomenda onError para erros detectados somente ao executar o Story e mostra warnings/errors. Consulta: 2026-10-04.
- [Ink — Story runtime source](https://github.com/inkle/ink/blob/master/ink-engine-runtime/Story.cs) — Define handler de erros e coleções de erros e warnings de runtime. Consulta: 2026-10-04.
