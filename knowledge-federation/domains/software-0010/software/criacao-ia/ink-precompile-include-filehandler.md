---
id: software.criacao_ia.tranche05.000489
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
fontes: ["https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#using-the-compiler", "https://github.com/inkle/ink/blob/master/README.md#advanced-using-inklecate-on-the-command-line"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ink: preferir compilação prévia e configurar includes no fluxo de compilação C#

## Em uma frase
Compilar previamente o roteiro costuma ser mais eficiente que carregar fontes `.ink` em runtime, mas compilação C# em execução pode atender ferramentas ou fluxos especiais.

## Por que importa
A aplicação de jogo pode carregar um asset JSON já compilado, enquanto ferramentas de editor precisam compilar texto de autoria e composições com múltiplos arquivos.

## Como funciona
Use inklecate para gerar JSON em build ou compile Ink fonte por `Ink.Compiler`; se usar `INCLUDE` em múltiplos arquivos, configure `fileHandler` com diretório base adequado.

## Exemplo
Pipeline de build executa inklecate sobre fonte principal para produzir JSON; ferramenta de preview usa Compiler com UnityInkFileHandler para resolver includes em pasta de trabalho.

## Limites e trade-offs
A documentação chama precompilation mais eficiente e mostra `fileHandler` para includes; caminhos de arquivo e suporte variam por ambiente e integração.

## Como verificar
Compile a narrativa por pipeline de produção e runtime editor, teste includes aninhados e compare runtime com saída esperada antes de empacotar.

## Conexões
- [[ink-evaluationfunction-call-from-game]] — Ink runtime: chamar função do roteiro com EvaluationFunction sem consumir diálogo.
- [[ink-runtime-error-handler]] — Ink runtime: registrar onError para erros que só aparecem durante a narrativa.

## Fontes
- [Ink — Running your ink: using the compiler](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#using-the-compiler) — Compara precompilação e compilação C# e mostra opções de fileHandler para INCLUDE. Consulta: 2026-10-04.
- [Ink — README: inklecate command line](https://github.com/inkle/ink/blob/master/README.md#advanced-using-inklecate-on-the-command-line) — Mostra geração de JSON e uso do compilador CLI oficial. Consulta: 2026-10-04.
