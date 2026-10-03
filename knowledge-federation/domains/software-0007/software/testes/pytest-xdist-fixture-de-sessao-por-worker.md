---
id: software.testes.tranche15.000851
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
fontes: ["https://pytest-xdist.readthedocs.io/en/stable/how-to.html", "https://pytest-xdist.readthedocs.io/en/stable/how-it-works.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest-xdist: não confundir escopo de sessão com execução única

## Em uma frase
O escopo `session` do pytest descreve a duração dentro de um processo worker; não cria, por si só, um singleton compartilhado entre todos os processos de pytest-xdist.

## Por que importa
Cada worker coleta a suíte e mantém seu próprio cache de fixtures, portanto uma fixture de sessão pode executar uma vez em cada worker que a solicita.

## Como funciona
Se o preparo caro deve ocorrer somente uma vez, a documentação mostra coordenação entre processos com arquivo e lock, seguida de leitura do resultado comum.

## Exemplo
Grave um artefato temporário sob lock de arquivo: o primeiro worker produz e persiste os dados; os demais leem o mesmo arquivo depois de adquirir o lock. Faça a fixture retornar o valor decodificado em todos os casos.

## Limites e trade-offs
O lock precisa proteger uma localização realmente compartilhada e o artefato deve ser válido após interrupção; a solução acrescenta protocolo de serialização e não substitui escopo de sessão em cada worker.

## Como verificar
Execute a fixture com pelo menos dois workers e registre quantas vezes o produtor roda; remova o arquivo temporário entre execuções para distinguir cache do teste de cache antigo.

## Conexões
- [[pytest-xdist-algoritmos-de-distribuicao]] — Veja também: pytest-xdist: escolher o algoritmo de distribuição pela afinidade do teste.
- [[pytest-xdist-worker-id-para-recursos-isolados]] — Veja também: pytest-xdist: derivar recursos temporários da identidade do worker.

## Fontes
- [pytest-xdist — How-tos](https://pytest-xdist.readthedocs.io/en/stable/how-to.html) — fixtures worker_id/testrun_uid, variáveis de ambiente e coordenação de fixtures de sessão; consultado em 2026-10-02.
- [pytest-xdist — How it works](https://pytest-xdist.readthedocs.io/en/stable/how-it-works.html) — arquitetura de controlador/workers, coleta e protocolo de execução; consultado em 2026-10-02.
