---
id: software.testes.tranche15.000894
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
fontes: ["https://docs.deno.com/runtime/test/", "https://docs.deno.com/runtime/reference/cli/test/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Deno test: colocar deadline em testes que podem pendurar

## Em uma frase
A opção `timeout` limita a duração de um teste e a documentação afirma que detecta tanto promises que nunca resolvem quanto loops síncronos que não cedem controle.

## Por que importa
Testes de concorrência, polling e rede externa podem permanecer ativos indefinidamente se nenhuma condição terminal chegar.

## Como funciona
Um limite local converte esse estado em falha visível e evita consumir o worker inteiro até o timeout do pipeline.

## Exemplo
Defina `timeout: 5000` no teste que valida um cliente sujeito a latência e dê ao caso uma assertion clara sobre resposta, sem transformar o timeout em substituto de cancelamento.

## Limites e trade-offs
Um deadline amplo não aborta necessariamente serviços remotos ou side effects iniciados pelo teste; a rotina de cancelamento e limpeza continua necessária ao falhar.

## Como verificar
Faça uma promise nunca resolvida e um loop curto de laboratório excederem o prazo, confirmando que ambos terminam como falha e que o restante do run continua de acordo com a política.

## Conexões
- [[deno-test-sanitizers-recursos-e-operacoes]] — Veja também: Deno test: reativar sanitizers para detectar recursos e operações vazados.
- [[deno-test-affected-tests-nao-substituem-ci-completa]] — Veja também: Deno test: usar affected tests como feedback incremental, não como cobertura final.

## Fontes
- [Deno Runtime — Testing](https://docs.deno.com/runtime/test/) — steps, timeouts, affected tests, permissões, snapshots, sanitizers e reporters; consultado em 2026-10-02.
- [Deno Runtime — deno test](https://docs.deno.com/runtime/reference/cli/test/) — flags de filtro, shard, cobertura, snapshots e execução do runner; consultado em 2026-10-02.
