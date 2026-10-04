---
id: software.testes.tranche09.000319
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://opentelemetry.io/docs/specs/semconv/", "https://opentelemetry.io/docs/concepts/instrumentation/libraries/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OpenTelemetry: versionar assertions de semantic conventions

## Em uma frase
Semantic conventions padronizam nomes e atributos, mas podem evoluir e depender da versão de instrumentação adotada.

## Por que importa
Testes de observabilidade verificam os dados produzidos pela aplicação antes de depender de um collector ou backend remoto. Assertion rígida em atributo legado pode quebrar após atualização compatível ou permitir migração parcial sem diagnóstico.

## Como funciona
Use SDK e exporters de memória em testes curtos, inspecione nomes, atributos, status e valores, e isole providers entre casos. Fixe versão de instrumentação, centralize expectativas semânticas e atualize-as junto ao upgrade planejado.

## Exemplo
Teste de HTTP verifica atributo de método e status para a convenção selecionada no SDK do projeto.

## Limites e trade-offs
Representação final depende de SDK, exporter, pipeline e convenções semânticas; teste local não prova ingestão, retenção ou consulta no backend. Sem convention adotada, nome parecido não prova semântica idêntica entre bibliotecas e versões.

## Como verificar
Revise versão do pacote e schema, execute caso com erro e sucesso e documente atributo requerido pelo produto.

## Conexões
- [[otel-test-provider-exporter-lifecycle]] — Veja também: OpenTelemetry: isolar exporter e provider entre testes.

## Fontes
- [OpenTelemetry — Semantic conventions](https://opentelemetry.io/docs/specs/semconv/) — convenções semânticas e atributos de telemetria; consultado em 2026-10-02.
- [OpenTelemetry — Instrumentation libraries](https://opentelemetry.io/docs/concepts/instrumentation/libraries/) — instrumentação, API/SDK e geração de telemetria; consultado em 2026-10-02.
