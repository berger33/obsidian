---
id: software.testes.tranche15.000859
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
fontes: ["https://pytest-xdist.readthedocs.io/en/stable/remote.html", "https://pytest-xdist.readthedocs.io/en/stable/how-it-works.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest-xdist: tratar workers remotos como ambientes de teste reais

## Em uma frase
Workers remotos permitem distribuir a suíte, mas o antigo mecanismo rsync do pytest-xdist está depreciado desde 3.0 e previsto para remoção em 4.0.

## Por que importa
A documentação aponta que o rsync não reproduz fielmente o ambiente remoto; SSH e socket server seguem no conjunto de recursos e não estão previstos para remoção.

## Como funciona
Provisione checkout, Python, dependências e dados por um fluxo de implantação próprio antes de despachar testes.

## Exemplo
Prepare o mesmo checkout e ambiente em dois hosts; valide conectividade e smoke tests e depois distribua pelos gateways SSH ou socket do execnet, sem depender do rsync depreciado.

## Limites e trade-offs
Manter SSH ou socket server não restaura a sincronização automática do rsync, e ainda é necessário controlar versões, credenciais, segredos, caminhos e limpeza em cada host.

## Como verificar
Fixe a versão do xdist, confirme que o fluxo não depende de --rsyncdir e execute um teste de fumaça por host antes da suíte distribuída; compare versão, checkout e identidade do worker.

## Conexões
- [[pytest-xdist-ordem-global-nao-garantida]] — Veja também: pytest-xdist: remover dependência de ordem na distribuição load.

## Fontes
- [pytest-xdist — Sending tests to remote SSH accounts](https://pytest-xdist.readthedocs.io/en/stable/remote.html) — workers remotos, gateways SSH e requisitos de execução distribuída; consultado em 2026-10-02.
- [pytest-xdist — How it works](https://pytest-xdist.readthedocs.io/en/stable/how-it-works.html) — arquitetura de controlador/workers, coleta e protocolo de execução; consultado em 2026-10-02.
