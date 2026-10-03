---
id: software.testes.tranche21.001529
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
fontes: ["https://github.com/boxed/mutmut", "https://github.com/boxed/mutmut/blob/main/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# mutmut: filtrar mutantes por tipos e ativar verbosidade

## Em uma frase
O parâmetro type_check_command permite usar mypy ou pyrefly em JSON para descartar mutantes que nem sequer tipam, e debug=true despeja todo o detalhe que a interface limpa engole.

## Por que importa
Mutantes que violam o sistema de tipos não ensinam nada sobre os testes; filtra-los poupa CPU e ruído de leitura.

## Como funciona
Configure type_check_command=['mypy', 'your_source_dir', '--output', 'json', '--disable-error-code', 'unused-ignore'] e ative debug ao depurar um caso estranho.

## Exemplo
A troca x: str = 'foo' por None é capturada pelo verificador e some da sua triagem de sobreviventes.

## Limites e trade-offs
O filtro esconde mutantes validos em casos de inferência difícil (propriedades em __init__), e a nota sobre pyright/ty declara o problema sem suporte.

## Como verificar
Compare a contagem de mutantes com e sem type_check_command e confirme a diferença explicada pelos erros de tipo.

## Conexões
- [[mutmut-mutate-selection]] — Veja também: mutmut: escolher linhas com cobertura ou glob.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — repositório oficial](https://github.com/boxed/mutmut/blob/main/README.rst) — material-fonte do README e das releases; consultado em 2026-10-03.
