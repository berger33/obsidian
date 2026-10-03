---
id: software.testes.tranche15.000858
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

# pytest-xdist: remover dependência de ordem na distribuição load

## Em uma frase
Com `--dist=load`, os itens pendentes são enviados ao worker disponível, sem garantia de ordem global; a execução paralela deve ser correta para qualquer escalonamento admissível.

## Por que importa
Uma sequência que funciona no modo serial pode deixar dados residuais, consumir fixtures compartilhadas ou depender do teste anterior, e então falhar de modo intermitente quando workers recebem cargas diferentes.

## Como funciona
O plugin não transforma um grafo de dependência implícita em ordem garantida.

## Exemplo
Faça cada caso preparar seu próprio estado e finalizar recursos; se houver dependência real, una a operação em um teste coerente ou modele uma afinidade conscientemente, em vez de usar atraso ou ordenação acidental.

## Limites e trade-offs
`loadscope` e `loadgroup` oferecem afinidade de coleção, não uma promessa universal de sequência entre grupos ou workers; preservar a ordem dentro de um arquivo não corrige estado global externo.

## Como verificar
Execute repetidamente com `-n auto` e diferentes algoritmos, também usando shuffle do pytest se disponível, e investigue qualquer resultado que dependa de um teste anterior.

## Conexões
- [[pytest-xdist-captura-de-saida-nao-e-stdout-direto]] — Veja também: pytest-xdist: planejar diagnósticos sem depender de -s.
- [[pytest-xdist-workers-remotos-exigem-ambiente-equivalente]] — Veja também: pytest-xdist: tratar workers remotos como ambientes de teste reais.

## Fontes
- [pytest-xdist — Distribution](https://pytest-xdist.readthedocs.io/en/stable/distribution.html) — algoritmos load, loadscope, loadfile, loadgroup e worksteal, identidade de workers e afinidade; consultado em 2026-10-02.
- [pytest-xdist — Documentation](https://pytest-xdist.readthedocs.io/en/stable/) — visão geral, execução paralela, recursos suportados e limitações de captura; consultado em 2026-10-02.
