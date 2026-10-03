---
id: software.testes.tranche15.000852
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
fontes: ["https://pytest-xdist.readthedocs.io/en/stable/how-to.html", "https://pytest-xdist.readthedocs.io/en/stable/distribution.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest-xdist: derivar recursos temporários da identidade do worker

## Em uma frase
Fixtures e variáveis de identidade do xdist permitem distinguir processos durante a execução, útil quando cada worker precisa de um banco, arquivo de log ou namespace descartável.

## Por que importa
`worker_id` identifica o worker, enquanto o valor especial `master` é usado quando não há distribuição; a variável de ambiente `PYTEST_XDIST_WORKER` expõe a identidade correspondente ao processo.

## Como funciona
O nome do worker é uma partição local ao run, não um identificador global durável.

## Exemplo
Construa o nome de um banco de teste como `app_test_{worker_id}` e use a mesma função para criar, selecionar e remover o banco. Para logs, inclua o worker no nome do arquivo para evitar gravações concorrentes no mesmo destino.

## Limites e trade-offs
Worker ID sozinho pode colidir entre runs simultâneos, e nomes previsíveis exigem limpeza segura; combine-o com a identidade da execução quando houver compartilhamento entre jobs.

## Como verificar
Rode em paralelo duas cópias independentes da suíte e confirme que cada worker escreve apenas em seu recurso, sem sobrescrever dados ou relatórios do outro.

## Conexões
- [[pytest-xdist-fixture-de-sessao-por-worker]] — Veja também: pytest-xdist: não confundir escopo de sessão com execução única.
- [[pytest-xdist-testrun-uid-para-concorrencia]] — Veja também: pytest-xdist: combinar testrun_uid e worker_id para separar execuções.

## Fontes
- [pytest-xdist — How-tos](https://pytest-xdist.readthedocs.io/en/stable/how-to.html) — fixtures worker_id/testrun_uid, variáveis de ambiente e coordenação de fixtures de sessão; consultado em 2026-10-02.
- [pytest-xdist — Distribution](https://pytest-xdist.readthedocs.io/en/stable/distribution.html) — algoritmos load, loadscope, loadfile, loadgroup e worksteal, identidade de workers e afinidade; consultado em 2026-10-02.
