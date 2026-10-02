---
id: software.testes.tranche09.000310
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
fontes: ["https://opentelemetry.io/docs/languages/java/sdk/", "https://opentelemetry.io/docs/specs/otel/trace/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OpenTelemetry: inspecionar spans com exporter em memória

## Em uma frase
Um exporter em memória permite que testes verifiquem spans produzidos sem enviar tráfego a um backend externo.

## Por que importa
Testes de observabilidade verificam os dados produzidos pela aplicação antes de depender de um collector ou backend remoto. Backend remoto acrescenta rede, custo e configuração que não são necessários para validar o nome e os atributos emitidos pela instrumentação.

## Como funciona
Use SDK e exporters de memória em testes curtos, inspecione nomes, atributos, status e valores, e isole providers entre casos. Registre spans do provider de teste e inspecione nome, parent, atributos, eventos e status após a operação observada.

## Exemplo
O teste chama serviço de catálogo e valida que span inclui operação sem guardar endereço de usuário como atributo.

## Limites e trade-offs
Representação final depende de SDK, exporter, pipeline e convenções semânticas; teste local não prova ingestão, retenção ou consulta no backend. Exporter em memória valida somente pipeline configurado no teste e precisa ser compatível com versão do SDK.

## Como verificar
Confirme que span esperado foi finalizado, compare atributos permitidos e zere o estado do exporter entre casos.

## Conexões
- [[otel-span-error-status-exception]] — Veja também: OpenTelemetry: testar exceção e status de span separadamente.

## Fontes
- [OpenTelemetry Java — SDK](https://opentelemetry.io/docs/languages/java/sdk/) — SDK Java, configuração e utilitários de teste; consultado em 2026-10-02.
- [OpenTelemetry — Trace API](https://opentelemetry.io/docs/specs/otel/trace/api/) — spans, eventos, atributos e status de trace; consultado em 2026-10-02.
