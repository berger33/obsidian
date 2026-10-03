---
id: software.testes.tranche15.000854
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
fontes: ["https://pytest-xdist.readthedocs.io/en/stable/distribution.html", "https://pytest-xdist.readthedocs.io/en/stable/how-to.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest-xdist: manter testes relacionados no mesmo worker com loadgroup

## Em uma frase
O marcador `xdist_group` permite declarar afinidade entre testes que precisam compartilhar processo ou recurso, desde que a execução use o distribuidor `loadgroup`.

## Por que importa
O worker recebe o grupo como unidade; marcadores com nomes iguais unem casos, e casos sem marcador continuam distribuídos normalmente.

## Como funciona
Um teste pode ganhar grupos via marcador direto, fixture ou configuração de módulo, permitindo descrever o vínculo próximo da dependência.

## Exemplo
Marque testes que usam a mesma instância descartável de navegador com `pytest.mark.xdist_group("browser")` e rode `pytest -n auto --dist=loadgroup`; o plugin entrega aquele grupo a um worker.

## Limites e trade-offs
Afinidade não serializa testes dentro do grupo nem protege o recurso contra outros processos ou runs; um grupo muito grande também pode prejudicar o balanceamento.

## Como verificar
Inspecione a coleta e os logs com vários workers, confirme que os casos relacionados exibem o mesmo worker e provoque uma execução concorrente de outro run para testar isolamento externo.

## Conexões
- [[pytest-xdist-testrun-uid-para-concorrencia]] — Veja também: pytest-xdist: combinar testrun_uid e worker_id para separar execuções.
- [[pytest-xdist-coleta-deterministica-entre-workers]] — Veja também: pytest-xdist: manter a coleta idêntica em todos os workers.

## Fontes
- [pytest-xdist — Distribution](https://pytest-xdist.readthedocs.io/en/stable/distribution.html) — algoritmos load, loadscope, loadfile, loadgroup e worksteal, identidade de workers e afinidade; consultado em 2026-10-02.
- [pytest-xdist — How-tos](https://pytest-xdist.readthedocs.io/en/stable/how-to.html) — fixtures worker_id/testrun_uid, variáveis de ambiente e coordenação de fixtures de sessão; consultado em 2026-10-02.
