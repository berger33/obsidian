---
id: software.testes.tranche15.000850
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pytest-xdist.readthedocs.io/en/stable/distribution.html", "https://pytest-xdist.readthedocs.io/en/stable/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest-xdist: escolher o algoritmo de distribuição pela afinidade do teste

## Em uma frase
`--dist` define como o controlador entrega itens coletados aos workers; não é apenas um ajuste de velocidade, porque alguns modos preservam afinidade por módulo, arquivo ou grupo.

## Por que importa
`load` procura manter workers ocupados, enquanto `loadscope`, `loadfile` e `loadgroup` agrupam unidades diferentes; `worksteal` redistribui trabalho restante quando há grande variação de duração.

## Como funciona
A escolha deve seguir dependências reais de setup e estado compartilhado, não uma preferência estética.

## Exemplo
Em uma suíte com fixture cara no módulo, `pytest -n auto --dist=loadscope` mantém os testes do módulo juntos; testes que compartilham um container nomeado podem usar `--dist=loadgroup` e `xdist_group`.

## Limites e trade-offs
Agrupar reduz liberdade de balanceamento e pode criar um worker lento se uma unidade concentrar muitos casos; `load` não promete ordem global nem afinidade.

## Como verificar
Compare duração por worker, equilíbrio do fim da execução e comportamento de fixtures nos modos candidatos, usando uma suíte representativa em vez de inferir ganho pelo número de CPUs.

## Conexões
- [[pytest-xdist-fixture-de-sessao-por-worker]] — Veja também: pytest-xdist: não confundir escopo de sessão com execução única.

## Fontes
- [pytest-xdist — Distribution](https://pytest-xdist.readthedocs.io/en/stable/distribution.html) — algoritmos load, loadscope, loadfile, loadgroup e worksteal, identidade de workers e afinidade; consultado em 2026-10-02.
- [pytest-xdist — Documentation](https://pytest-xdist.readthedocs.io/en/stable/) — visão geral, execução paralela, recursos suportados e limitações de captura; consultado em 2026-10-02.
