---
id: software.testes.tranche21.001526
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

# mutmut: configuração em setup.cfg ou pyproject

## Em uma frase
Quando o layout foge do óbvio, a seção [mutmut] do setup.cfg (ou tool.mutmut no pyproject.toml) define source_paths e pytest_add_cli_args_test_selection; no TOML os caminhos viram lista.

## Por que importa
Separar o código a mutar do código de teste é justamente onde os projetos fora do padrão quebram a descoberta automática.

## Como funciona
Declare a raiz do pacote em source_paths e o diretório de testes na seleção de pytest, mantendo as duas configurações equivalentes.

## Exemplo
source_paths=["src/"] com pytest_add_cli_args_test_selection=["tests/"] no pyproject cobre o layout src/.

## Limites e trade-offs
As sintaxes dos dois arquivos diferem (string com quebras versus array), e migrar de um para o outro sem conferir deixa o filtro silenciosamente vazio.

## Como verificar
Mude source_paths para um caminho inexistente e confirme que a corrida reclama em vez de mutar o nada.

## Conexões
- [[mutmut-fork-requirement]] — Veja também: mutmut: requisito de fork e plataformas.
- [[mutmut-copy-stack-depth]] — Veja também: mutmut: also_copy e profundidade máxima de pilha.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — repositório oficial](https://github.com/boxed/mutmut/blob/main/README.rst) — material-fonte do README e das releases; consultado em 2026-10-03.
