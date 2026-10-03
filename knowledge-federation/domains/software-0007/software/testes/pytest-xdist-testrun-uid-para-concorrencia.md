---
id: software.testes.tranche15.000853
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

# pytest-xdist: combinar testrun_uid e worker_id para separar execuções

## Em uma frase
`testrun_uid` distingue uma sessão xdist inteira, enquanto a identidade do worker distingue processos dentro dela; juntos formam uma chave mais segura para recursos em CI concorrente.

## Por que importa
Todos os workers do mesmo run precisam compartilhar o identificador de execução para cooperar, mas dois runs simultâneos não devem apontar para o mesmo banco temporário.

## Como funciona
A fixture `testrun_uid` e a variável `PYTEST_XDIST_TESTRUNUID` atendem ao primeiro propósito; a partição por worker atende ao segundo.

## Exemplo
Nomeie o banco compartilhado com o UID do run se os workers realmente colaboram sobre os mesmos dados, ou derive bancos independentes do UID mais `worker_id` se cada worker precisa de isolamento.

## Limites e trade-offs
O UID evita colisão entre execuções, mas não cria o banco nem resolve limpeza após cancelamento; credenciais e nomes também precisam respeitar limites do backend.

## Como verificar
Inicie duas execuções xdist em paralelo e verifique que os UIDs divergem, que workers do mesmo run concordam e que a rotina de teardown remove apenas os recursos daquele UID.

## Conexões
- [[pytest-xdist-worker-id-para-recursos-isolados]] — Veja também: pytest-xdist: derivar recursos temporários da identidade do worker.
- [[pytest-xdist-grupos-de-testes-com-estado-compartilhado]] — Veja também: pytest-xdist: manter testes relacionados no mesmo worker com loadgroup.

## Fontes
- [pytest-xdist — How-tos](https://pytest-xdist.readthedocs.io/en/stable/how-to.html) — fixtures worker_id/testrun_uid, variáveis de ambiente e coordenação de fixtures de sessão; consultado em 2026-10-02.
- [pytest-xdist — Distribution](https://pytest-xdist.readthedocs.io/en/stable/distribution.html) — algoritmos load, loadscope, loadfile, loadgroup e worksteal, identidade de workers e afinidade; consultado em 2026-10-02.
