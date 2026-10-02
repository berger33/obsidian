---
id: software.testes.tranche11.000465
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
fontes: ["https://wiremock.org/docs/verifying/", "https://wiremock.org/docs/request-matching/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: verificar request recebida sem confundir com resposta

## Em uma frase
O request journal mantém requests recebidas em memória para verificação e consulta após as chamadas do sistema sob teste.

## Por que importa
Validar apenas a resposta do mock pode não detectar chamadas duplicadas, headers ausentes ou sequência incorreta.

## Como funciona
Use verify com matcher alinhado ao contrato e, quando necessário, consulte requests registradas para diagnosticar a interação.

## Exemplo
Após criar pedido, o teste verifica um POST com Authorization e corpo contendo o id esperado.

## Limites e trade-offs
O journal pode ser desabilitado para carga; nesse modo verificações baseadas em journal não são evidência disponível.

## Como verificar
Confirme a configuração do journal e prove que uma chamada duplicada ou incompleta faz a verificação falhar.

## Conexões
- [[wiremock-scenario-maquina-de-estados]] — Veja também: WireMock: modelar fluxo stateful com cenário explícito.
- [[wiremock-unmatched-requests-near-miss]] — Veja também: WireMock: diagnosticar request não mapeada com near miss.

## Fontes
- [WireMock — Verifying](https://wiremock.org/docs/verifying/) — request journal, verificações, requests não correspondidos e near misses; consultado em 2026-10-02.
- [WireMock — Request Matching](https://wiremock.org/docs/request-matching/) — matching de URL, método, query, headers, cookies, body, JSON e formulários; consultado em 2026-10-02.
