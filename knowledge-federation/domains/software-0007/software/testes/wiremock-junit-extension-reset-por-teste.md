---
id: software.testes.tranche11.000468
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
fontes: ["https://wiremock.org/docs/junit-jupiter/", "https://wiremock.org/docs/verifying/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: confirmar lifecycle e reset da extensão JUnit

## Em uma frase
A extensão WireMock para JUnit Jupiter inicia e encerra servidor conforme lifecycle e, por padrão, reseta mappings e requests entre métodos.

## Por que importa
Servidor ou journal compartilhado sem limpeza pode fazer um caso depender de stubs e tráfego de outro.

## Como funciona
Use porta dinâmica fornecida pela extensão e teste cada método com seus próprios mappings; altere reset automático somente se justificar o compartilhamento.

## Exemplo
Dois métodos registram stubs diferentes e cada um usa URL/porta obtida da instância da extensão.

## Limites e trade-offs
Desabilitar reset exige limpeza explícita e cuidado com paralelismo e estado de cenários.

## Como verificar
Execute métodos em ordem aleatória e confirme que cada request tem apenas o mapping e o journal esperados.

## Conexões
- [[wiremock-faults-para-resiliencia]] — Veja também: WireMock: usar faults controlados para testar tolerância a falha.
- [[wiremock-response-template-dados-da-request]] — Veja também: WireMock: tornar resposta dinâmica com response templating configurado.

## Fontes
- [WireMock — JUnit Jupiter](https://wiremock.org/docs/junit-jupiter/) — ciclo de vida da extensão, portas dinâmicas e reset entre testes; consultado em 2026-10-02.
- [WireMock — Verifying](https://wiremock.org/docs/verifying/) — request journal, verificações, requests não correspondidos e near misses; consultado em 2026-10-02.
