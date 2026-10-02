---
id: software.testes.tranche11.000466
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://wiremock.org/docs/verifying/", "https://wiremock.org/docs/stubbing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: diagnosticar request não mapeada com near miss

## Em uma frase
Requests sem mapping normalmente recebem 404 e podem ser consultadas como unmatched; near misses apontam mappings parecidos.

## Por que importa
WireMock devolve respostas configuradas para requests correspondentes e mantém evidência de tráfego recebido, permitindo isolar dependências sem substituir assertions do sistema testado. Um 404 genérico pode esconder diferença pequena de método, header ou corpo entre o teste e o matcher configurado.

## Como funciona
Configure mappings próximos do caso, use matchers que expressem o contrato observado e isole servidor, request journal e cenários entre testes; verifique requests e respostas em vez de testar somente o stub. Inspecione a request unmatched e use near-miss para localizar qual stub ficou mais próximo antes de ampliar o matcher.

## Exemplo
O cliente envia /v2/orders enquanto stub espera /v1/orders; a consulta mostra a rota e o mapping candidato.

## Limites e trade-offs
Um mock não prova a compatibilidade com serviço real. Journal e cenários possuem estado, matchers genéricos podem aceitar requests incorretos e extensões como templating exigem configuração explícita. Near miss é sugestão de diferença, não prova que o mapping candidato seja correto para o contrato.

## Como verificar
Force mismatch conhecido e verifique que a resposta diagnóstica identifica request e stub próximos sem aceitar a chamada inválida.

## Conexões
- [[wiremock-verificacao-de-request-journal]] — Veja também: WireMock: verificar request recebida sem confundir com resposta.
- [[wiremock-faults-para-resiliencia]] — Veja também: WireMock: usar faults controlados para testar tolerância a falha.

## Fontes
- [WireMock — Verifying](https://wiremock.org/docs/verifying/) — request journal, verificações, requests não correspondidos e near misses; consultado em 2026-10-02.
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de request/response, prioridade, defaults, reset e persistência de stubs; consultado em 2026-10-02.
