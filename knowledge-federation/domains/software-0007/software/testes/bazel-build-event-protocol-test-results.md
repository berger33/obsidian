---
id: software.testes.tranche14.000758
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://bazel.build/remote/bep/", "https://bazel.build/docs/user-manual"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Bazel: consumir resultados de testes via BEP

## Em uma frase
Build Event Protocol representa a invocação como eventos estruturados e inclui resultados e progresso de testes para ferramentas consumidoras.

## Por que importa
Scripts que analisam texto de console quebram com mudanças de formatação; eventos tipados oferecem um contrato mais adequado para dashboards e integrações.

## Como funciona
Ative a saída BEP no formato binário, texto ou JSON disponível e consuma a sequência respeitando identificadores, relações entre eventos e término da invocação.

## Exemplo
Uma integração de CI pode ler eventos de teste e publicar o status por target sem extrair frases do console que também contêm progresso de build.

## Limites e trade-offs
O grafo pode terminar incompleto se Bazel cair ou o transporte falhar; eventos de resultado não substituem logs e artefatos detalhados.

## Como verificar
Compare contagens e status produzidos pelo consumidor com o resumo de uma execução conhecida, incluindo uma execução interrompida.

## Conexões
- [[bazel-test-target-selection-patterns]] — Veja também: Bazel: selecionar alvos de teste por padrões.
- [[bazel-remote-test-environment]] — Veja também: Bazel: projetar testes compatíveis com execução remota.

## Fontes
- [Bazel — Build Event Protocol](https://bazel.build/remote/bep/) — eventos estruturados de invocação e resultados de testes para consumidores; consultado em 2026-10-02.
- [Bazel — Commands and Options](https://bazel.build/docs/user-manual) — opções de bazel test, seleção de alvos, variáveis, saída e argumentos; consultado em 2026-10-02.
